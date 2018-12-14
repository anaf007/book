第八章：用户认证
====================================

大多数程序都要进行用户跟踪。用户连接程序时会进行身份认证,通过这一过程,让程序 知道自己的身份。程序知道用户是谁后,就能提供有针对性的体验。

最常用的认证方法要求用户提供一个身份证明(用户的电子邮件或用户名)和一个密码。 本章要为 Flasky 开发一个完整的认证系统。

Flask的认证扩展
---------------------

优秀的 Python 认证包很多,但没有一个能实现所有功能。本章介绍的认证方案使用了多个
包,并编写了胶水代码让其良好协作。本章使用的包列表如下

 - Flask-Login:管理已登录用户的用户会话。 
 - Werkzeug:计算密码散列值并进行核对。 
 - itsdangerous:生成并核对加密安全令牌。

除了认证相关的包之外,本章还用到如下常规用途的扩展

 - Flask-Mail:发送与认证相关的电子邮件。
 - Flask-Bootstrap:HTML 模板。
 - Flask-WTF:Web 表单。

密码安全性
---------------

设计 Web 程序时,人们往往会高估数据库中用户信息的安全性。如果攻击者入侵服务器获取了数据库,用户的安全就处在风险之中,这个风险比你想象的要大。众所周知,大多数 用户都在不同的网站中使用相同的密码,因此,即便不保存任何敏感信息,攻击者获得存 储在数据库中的密码之后,也能访问用户在其他网站中的账户。

若想保证数据库中用户密码的安全,关键在于不能存储密码本身,而要存储密码的散列 值。计算密码散列值的函数接收密码作为输入,使用一种或多种加密算法转换密码,最终 得到一个和原始密码没有关系的字符序列。核对密码时,密码散列值可代替原始密码,因 为计算散列值的函数是可复现的:只要输入一样,结果就一样。

**计算密码散列值是个复杂的任务,很难正确处理。因此强烈建议你不要自己 实现,而是使用经过社区成员审查且声誉良好的库。如果你对生成安全密码 散列值的过程感兴趣,“Salted Password Hashing - Doing it Right”(计算加盐 密码散列值的正确方法,https://crackstation.net/hashing-security.htm)这篇文 章值得一读。**

使用Werkzeug实现密码散列
------------------------------

Werkzeug 中的 security 模块能够很方便地实现密码散列值的计算。这一功能的实现只需要
两个函数,分别用在注册用户和验证用户阶段。

 - generate_password_hash(password, method=pbkdf2:sha1, salt_length=8):这个函数将 原始密码作为输入,以字符串形式输出密码的散列值,输出的值可保存在用户数据库中。 method 和 salt_length 的默认值就能满足大多数需求。
 - check_password_hash(hash, password):这个函数的参数是从数据库中取回的密码散列 值和用户输入的密码。返回值为 True 表明密码正确。

app/models.py:在 User 模型中加入密码散列

 .. literalinclude:: code/code8-1.py
    :language: python

计算密码散列值的函数通过名为 password 的只写属性实现。设定这个属性的值时,赋值 方法会调用 Werkzeug 提供的 generate_password_hash() 函数,并把得到的结果赋值给 password_hash 字段。如果试图读取 password 属性的值,则会返回错误,原因很明显,因 为生成散列值后就无法还原成原来的密码了。

verify_password 方法接受一个参数(即密码),将其传给 Werkzeug 提供的 check_password_hash() 函数,和存储在 User 模型中的密码散列值进行比对。如果这个方法返回 True,就表明密码是正确的。

密码散列功能已经完成,可以在 shell 中进行测试::

    (venv) $ python manage.py shell
    >>> u = User()
    >>> u.password = 'cat'
    >>> u.password_hash
    'pbkdf2:sha1:1000$duxMk0OF$4735b293e397d6eeaf650aaf490fd9091f928bed'
    >>> u.verify_password('cat')
    True
    >>> u.verify_password('dog')
    False
    >>> u2 = User()
    >>> u2.password = 'cat'
    >>> u2.password_hash
    'pbkdf2:sha1:1000$UjvnGeTP$875e28eb0874f44101d6b332442218f66975ee89'

注意,即使用户 u 和 u2 使用了相同的密码,它们的密码散列值也完全不一样。为了确保 这个功能今后可持续使用,我们可以把上述测试写成单元测试,以便于重复执行。

tests/test_user_model.py:密码散列化测试::

    import unittest
    from app.models import User
    class UserModelTestCase(unittest.TestCase):

        def test_password_setter(self):
            u = User(password = 'cat')
            self.assertTrue(u.password_hash is not None)
        def test_no_password_getter(self):
            u = User(password = 'cat')
            with self.assertRaises(AttributeError):
                u.password

        def test_password_verification(self):
            u = User(password = 'cat') 
            self.assertTrue(u.verify_password('cat')) 
            self.assertFalse(u.verify_password('dog'))

        def test_password_salts_are_random(self):
            u = User(password='cat')
            u2 = User(password='cat')
            self.assertTrue(u.password_hash != u2.password_hash)

创建认证蓝本
-----------------

我们在第 7 章介绍过蓝本,把创建程序的过程移入工厂函数后,可以使用蓝本在全局作用 域中定义路由。与用户认证系统相关的路由可在 auth 蓝本中定义。对于不同的程序功能, 我们要使用不同的蓝本,这是保持代码整齐有序的好方法。

auth 蓝本保存在同名 Python 包中。蓝本的包构造文件创建蓝本对象,再从 views.py 模块 中引入路由.

app/auth/__init__.py:创建蓝本::

    from flask import Blueprint
    auth = Blueprint('auth', __name__)
    from . import views

app/auth/views.py 模块引入蓝本,然后使用蓝本的 route 修饰器定义与认证相关的路由,这段代码中添加了一个 /login 路由,渲染同名占位模板
::

    from flask import render_template
    from . import auth

    @auth.route('/login')
    def login():
        return render_template('auth/login.html')


注意,为 render_template() 指定的模板文件保存在 auth 文件夹中。这个文件夹必须在 app/templates 中创建,因为 Flask 认为模板的路径是相对于程序模板文件夹而言的。为避 免与 main 蓝本和后续添加的蓝本发生模板命名冲突,可以把蓝本使用的模板保存在单独的文件夹中。

我们也可将蓝本配置成使用其独立的文件夹保存模板。如果配置了多个模板 文件夹,render_template() 函数会首先搜索程序配置的模板文件夹,然后再 搜索蓝本配置的模板文件夹。

auth 蓝本要在 create_app() 工厂函数中附加到程序上

app/__init__.py:附加蓝本::

    def create_app(config_name):
        # ...
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')
        return app

**注册蓝本时使用的 url_prefix 是可选参数**
。如果使用了这个参数,注册后蓝本中定义的 所有路由都会加上指定的前缀,即这个例子中的 /auth。例如,/login 路由会注册成 /auth/ login,在开发 Web 服务器中,完整的 URL 就变成了 http://localhost:5000/auth/login。

使用Flask-Login认证用户
--------------------------------

用户登录程序后,他们的认证状态要被记录下来,这样浏览不同的页面时才能记住这个状 态。Flask-Login 是个非常有用的小型扩展,专门用来管理用户认证系统中的认证状态,且 不依赖特定的认证机制。

使用之前,我们要在虚拟环境中安装这个扩展::

    (venv) $ pip install flask-login

准备用于登录的用户模型
-------------------------

要想使用 Flask-Login 扩展,程序的 User 模型必须实现几个方法。需要实现的方法如表 8-1 所示。

Flask-Login要求实现的用户方法::

    is_authenticated #如果用户已经登录,必须返回True,否则返回False
    is_active() #如果允许用户登录,必须返回 True,否则返回 False。如果要禁用账户,可以返回 False
    is_anonymous() #对普通用户必须返回 False
    get_id() #必须返回用户的唯一标识符,使用 Unicode 编码字符串

这 4个方法可以在模型类中作为方法直接实现,不过还有一种更简单的替代方案。Flask- Login 提供了一个 UserMixin 类,其中包含这些方法的默认实现,且能满足大多数需求。修 改后的 User 模型如示例 8-6 所示。

app/models.py:修改 User 模型,支持用户登录::

    from flask.ext.login import UserMixin

    class User(UserMixin, db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key = True)
        email = db.Column(db.String(64), unique=True, index=True)
        username = db.Column(db.String(64), unique=True, index=True)
        password_hash = db.Column(db.String(128))
        role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

注意,示例中同时还添加了 email 字段。在这个程序中,用户使用电子邮件地址登录,因 为相对于用户名而言,用户更不容易忘记自己的电子邮件地址。

Flask-Login 在程序的工厂函数中初始化

app/__init__.py:初始化 Flask-Login::

    from flask.ext.login import LoginManager
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'

    def create_app(config_name): 
        # ...
        login_manager.init_app(app)
        # ...

LoginManager 对象的 session_protection 属性可以设为 None、'basic' 或 'strong',以提 供不同的安全等级防止用户会话遭篡改。设为 'strong' 时,Flask-Login 会记录客户端 IP 地址和浏览器的用户代理信息,如果发现异动就登出用户。login_view 属性设置登录页面 的端点。回忆一下,登录路由在蓝本中定义,因此要在前面加上蓝本的名字。

最后,Flask-Login 要求程序实现一个回调函数,使用指定的标识符加载用户。

app/models.py:加载用户的回调函数::

    from . import login_manager
    @login_manager.user_loader

    def load_user(user_id):
        return User.query.get(int(user_id))

加载用户的回调函数接收以 Unicode 字符串形式表示的用户标识符。如果能找到用户,这 个函数必须返回用户对象;否则应该返回 None。

保护路由
---------------

为了保护路由只让认证用户访问,Flask-Login 提供了一个 login_required 修饰器。用法演示如下::

    from flask.ext.login import login_required
    @app.route('/secret')
    @login_required

    def secret():
        return 'Only authenticated users are allowed!'

如果未认证的用户访问这个路由,Flask-Login 会拦截请求,把用户发往登录页面。

添加登录表单
---------------

呈现给用户的登录表单中包含一个用于输入电子邮件地址的文本字段、一个密码字段、一 个“记住我”复选框和提交按钮。这个表单使用的 Flask-WTF 类

app/auth/forms.py:登录表单::

    from flask.ext.wtf import Form
    from wtforms import StringField, PasswordField, BooleanField,SubmitField 
    from wtforms.validators import Required, Length, Email
    class LoginForm(Form):
        email = StringField('Email', validators=[Required(),(1, 64),Email()])
        password = PasswordField('Password', validators=[Required()])
        remember_me = BooleanField('Keep me logged in') 
        submit = SubmitField('Log In')

电子邮件字段用到了 WTForms 提供的 Length() 和 Email() 验证函数。PasswordField 类表 示属性为 type="password" 的 <input> 元素。BooleanField 类表示复选框。

登录页面使用的模板保存在 auth/login.html 文件中。这个模板只需使用 Flask-Bootstrap 提 供的 wtf.quick_form() 宏渲染表单即可。

base.html 模板中的导航条使用 Jinja2 条件语句,并根据当前用户的登录状态分别显示 “Sign In”或“Sign Out”链接。

app/templates/base.html:导航条中的 Sign In 和 Sign Out 链接::

    <ul class="nav navbar-nav navbar-right">
        {% if current_user.is_authenticated() %}
        <li>
            <a href="{{ url_for('auth.logout') }}">Sign Out</a></li> 
        {% else %}
        <li>
            <a href="{{ url_for('auth.login') }}">Sign In</a>
        </li> 
        {% endif %}
    </ul>

判断条件中的变量 current_user 由 Flask-Login 定义,且在视图函数和模板中自动可用。 这个变量的值是当前登录的用户,如果用户尚未登录,则是一个匿名用户代理对象。如果 是匿名用户,is_authenticated() 方法返回 False。所以这个方法可用来判断当前用户是否 已经登录。


**这里其实已经更新了is_authenticated少了括号**


登入用户
-------------

app/auth/views.py:登录路由:

 .. literalinclude:: code/code8-2.py
    :language: python

这个视图函数创建了一个 LoginForm 对象,用法和第 4 章中的那个简单表单一样。当请 求类型是 GET 时,视图函数直接渲染模板,即显示表单。当表单在 POST 请求中提交时, Flask-WTF 中的 validate_on_submit() 函数会验证表单数据,然后尝试登入用户。

为了登入用户,视图函数首先使用表单中填写的 email 从数据库中加载用户。如果电子邮 件地址对应的用户存在,再调用用户对象的 verify_password() 方法,其参数是表单中填 写的密码。如果密码正确,则调用 Flask-Login 中的 login_user() 函数,在用户会话中把 用户标记为已登录。login_user() 函数的参数是要登录的用户,以及可选的“记住我”布 尔值,“记住我”也在表单中填写。如果值为 False,那么关闭浏览器后用户会话就过期 了,所以下次用户访问时要重新登录。如果值为 True,那么会在用户浏览器中写入一个长 期有效的 cookie,使用这个 cookie 可以复现用户会话。

按照第 4 章介绍的“Post/ 重定向 /Get 模式”,提交登录密令的 POST 请求最后也做了重定 向,不过目标 URL 有两种可能。用户访问未授权的 URL 时会显示登录表单,Flask-Login 会把原地址保存在查询字符串的 next 参数中,这个参数可从 request.args 字典中读取。 如果查询字符串中没有 next 参数,则重定向到首页。如果用户输入的电子邮件或密码不正 确,程序会设定一个 Flash 消息,再次渲染表单,让用户重试登录。

在生产服务器上,登录路由必须使用安全的 HTTP,从而加密传送给服务器 的表单数据。如果没使用安全的 HTTP,登录密令在传输过程中可能会被截 取,在服务器上花再多的精力用于保证密码安全都无济于事。

我们需要更新登录模板以渲染表单。

app/templates/auth/login.html:渲染登录表单::

    {% extends "base.html" %}
    {% import "bootstrap/wtf.html" as wtf %}
    {% block title %}Flasky - Login{% endblock %}
    {% block page_content %} 
    <div class="page-header">
        <h1>Login</h1>
    </div>
    <div class="col-md-4">
        {{ wtf.quick_form(form) }}
    </div>
    {% endblock %}

    
登出用户
-------------

app/auth/views.py:退出路由::

    from flask.ext.login import logout_user, login_required
    
    @auth.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You have been logged out.') 
        return redirect(url_for('main.index'))

为了登出用户,这个视图函数调用 Flask-Login 中的 logout_user() 函数,删除并重设用户 会话。随后会显示一个 Flash 消息,确认这次操作,再重定向到首页,这样登出就完成了。

测试登录
----------------

略过

注册新用户
-----------------

如果新用户想成为程序的成员,必须在程序中注册,这样程序才能识别并登入用户。程序 的登录页面中要显示一个链接,把用户带到注册页面,让用户输入电子邮件地址、用户名 和密码。

添加用户注册表单
----------------------

注册页面使用的表单要求用户输入电子邮件地址、用户名和密码。

app/auth/forms.py:用户注册表单

 .. literalinclude:: code/code8-3.py
    :language: python

这个表单使用 WTForms 提供的 Regexp 验证函数,确保 username 字段只包含字母、数字、 下划线和点号。这个验证函数中正则表达式后面的两个参数分别是正则表达式的旗标和验 证失败时显示的错误消息。

安全起见,密码要输入两次。此时要验证两个密码字段中的值是否一致,这种验证可使用 WTForms 提供的另一验证函数实现,即 EqualTo。这个验证函数要附属到两个密码字段中 的一个上,另一个字段则作为参数传入。

这个表单还有两个自定义的验证函数,以方法的形式实现。如果表单类中定义了以 validate_开头且后面跟着字段名的方法,这个方法就和常规的验证函数一起调用。本例 分别为 email 和 username 字段定义了验证函数,确保填写的值在数据库中没出现过。自定 义的验证函数要想表示验证失败,可以抛出 ValidationError 异常,其参数就是错误消息。

显示这个表单的模板是 /templates/auth/register.html。和登录模板一样,这个模板也使用 wtf.quick_form() 渲染表单。

登录页面要显示一个指向注册页面的链接,让没有账户的用户能轻易找到注册页面。

app/templates/auth/login.html:链接到注册页面::

    <p>
        New user?
        <a href="{{ url_for('auth.register') }}">Click here to register</a> 
    </p>

注册新用户
----------------

处理用户注册的过程没有什么难以理解的地方。提交注册表单,通过验证后,系统就使用
用户填写的信息在数据库中添加一个新用户。


app/auth/views.py:用户注册路由

 .. literalinclude:: code/code8-4.py
    :language: python

确认账户
-------------
略过

使用itsdangerous生成确认令牌
-------------------------------------

确认邮件中最简单的确认链接是 http://www.example.com/auth/confirm/<id> 这种形式的 URL,其中 id 是数据库分配给用户的数字 id。用户点击链接后,处理这个路由的视图函 数就将收到的用户 id 作为参数进行确认,然后将用户状态更新为已确认。

但这种实现方式显然不是很安全,只要用户能判断确认链接的格式,就可以随便指定 URL 中的数字,从而确认任意账户。解决方法是把 URL 中的 id 换成将相同信息安全加密后得 到的令牌。

回忆一下我们在第 4 章对用户会话的讨论,Flask 使用加密的签名 cookie 保护用户会话, 防止被篡改。这种安全的 cookie 使用 itsdangerous 包签名。同样的方法也可用于确认令 牌上。

下面这个简短的 shell 会话显示了如何使用 itsdangerous 包生成包含用户 id 的安全令牌::

    (venv) $ python manage.py shell
    >>> from manage import app
    >>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
    >>> s = Serializer(app.config['SECRET_KEY'], expires_in = 3600)
    >>> token = s.dumps({ 'confirm': 23 })
    >>> token 
    'eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4MTcxODU1OCwiaWF0IjoxMzgxNzE0OTU4fQ.ey ...' >>> data = s.loads(token)
    >>> 
    data {u'confirm': 23}

itsdangerous 提供了多种生成令牌的方法。其中,TimedJSONWebSignatureSerializer 类生成 具有过期时间的JSON Web签名(JSON Web Signatures,JWS)。这个类的构造函数接收 的参数是一个密钥,在 Flask 程序中可使用 SECRET_KEY 设置。

dumps() 方法为指定的数据生成一个加密签名,然后再对数据和签名进行序列化,生成令 牌字符串。expires_in 参数设置令牌的过期时间,单位为秒。


为了解码令牌,序列化对象提供了 loads() 方法,其唯一的参数是令牌字符串。这个方法 会检验签名和过期时间,如果通过,返回原始数据。如果提供给 loads() 方法的令牌不正 确或过期了,则抛出异常。

我们可以将这种生成和检验令牌的功能可添加到 User 模型中。

app/models.py:确认用户账户::

    from itsdangerous import TimedJSONWebSignatureSerializer as Serializer 
    from flask import current_app
    from . import db

    class User(UserMixin, db.Model):
        # ...
        confirmed = db.Column(db.Boolean, default=False)

        def generate_confirmation_token(self, expiration=3600):
            s = Serializer(current_app.config['SECRET_KEY'], expiration) 
            return s.dumps({'confirm': self.id})

        def confirm(self, token):
            s = Serializer(current_app.config['SECRET_KEY']) 
            try:
                data = s.loads(token)
            except:
                return False
            if data.get('confirm') != self.id:
                return False 
            self.confirmed = True 
            db.session.add(self) 
            return True

generate_confirmation_token() 方法生成一个令牌,有效期默认为一小时。confirm() 方 法检验令牌,如果检验通过,则把新添加的 confirmed 属性设为 True。

除了检验令牌,confirm() 方法还检查令牌中的 id 是否和存储在 current_user 中的已登录用户匹配。如此一来,即使恶意用户知道如何生成签名令牌,也无法确认别人的账户。

发送确认邮件
------------------------------------------------------------------

略过


管理账户
------------------------------------------------------------------

拥有程序账户的用户有时可能需要修改账户信息。下面这些操作可使用本章介绍的技术添 加到验证蓝本中。


安全意识强的用户可能希望定期修改密码。这是一个很容易实现的功能,只要用户处于 登录状态,就可以放心显示一个表单,要求用户输入旧密码和替换的新密码。

为避免用户忘记密码无法登入的情况,程序可以提供重设密码功能。安全起见,有必要 使用类似于确认账户时用到的令牌。用户请求重设密码后,程序会向用户注册时提供的 电子邮件地址发送一封包含重设令牌的邮件。用户点击邮件中的链接,令牌验证后,会 显示一个用于输入新密码的表单。

程序可以提供修改注册电子邮件地址的功能,不过接受新地址之前,必须使用确认邮件 进行验证。使用这个功能时,用户在表单中输入新的电子邮件地址。为了验证这个地 址,程序会发送一封包含令牌的邮件。服务器收到令牌后,再更新用户对象。服务器收 到令牌之前,可以把新电子邮件地址保存在一个新数据库字段中作为待定地址,或者将 其和 id 一起保存在令牌中。

下一章,我们使用用户角色扩充 Flasky 的用户子系统。








.. include:: ../../../ad.rst  
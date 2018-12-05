第四章：web表单
===========================

Flask-WTF(http://pythonhosted.org/Flask-WTF/)扩展可以把处理 Web 表单的过程变成一 种愉悦的体验。这个扩展对独立的 WTForms(http://wtforms.simplecodes.com)包进行了包 装,方便集成到 Flask 程序中。

安装::
    
    (venv) $ pip install flask-wtf

跨站请求伪造保护
----------------------

默认情况下,Flask-WTF能保护所有表单免受跨站请求伪造(Cross-Site Request Forgery,CSRF)的攻击。恶意网站把请求发送到被攻击者已登录的其他网站时就会引发 CSRF 攻击。 

为了实现 CSRF 保护,Flask-WTF 需要程序设置一个密钥。Flask-WTF 使用这个密钥生成加密令牌,再用令牌验证请求中表单数据的真伪。

::

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hard to guess string'

app.config 字典可用来存储框架、扩展和程序本身的配置变量。使用标准的字典句法就能 把配置值添加到 app.config 对象中。这个对象还提供了一些方法,可以从文件或环境中导 入配置值。

SECRET_KEY 配置变量是通用密钥,可在 Flask 和多个第三方扩展中使用。如其名所示,加 密的强度取决于变量值的机密程度。不同的程序要使用不同的密钥,而且要保证其他人不 知道你所用的字符串。

表单类
-------------

使用 Flask-WTF 时,每个 Web 表单都由一个继承自 Form 的类表示。这个类定义表单中的 一组字段,每个字段都用对象表示。字段对象可附属一个或多个验证函数。验证函数用来 验证用户提交的输入值是否符合要求。

hello.py:定义表单类::

    
    from flask.ext.wtf import Form
    from wtforms import StringField, SubmitField 
    from wtforms.validators import Required
    class NameForm(Form):
        name = StringField('What is your name?', validators=[Required()]) 
        submit = SubmitField('Submit')

**flask版本已经升级了，这里按照书上的from flask.ext.wtf import Form应该会报错，应该写成from flask_wtf import Form**

这个表单中的字段都定义为类变量,类变量的值是相应字段类型的对象。

在这个示例中, NameForm 表单中有一个名为 name 的文本字段和一个名为 submit 的提交按钮。StringField 类表示属性为 type="text" 的 <input> 元素。SubmitField 类表示属性为 type="submit" 的 <input> 元素。字段构造函数的第一个参数是把表单渲染成 HTML 时使用的标号。

StringField 构造函数中的可选参数 validators 指定一个由验证函数组成的列表,在接受 用户提交的数据之前验证数据。验证函数 Required() 确保提交的字段不为空。

WTForms支持的HTML标准字段

 - StringField  :文本字段
 - TextAreaField :多行文本字段
 - PasswordField :密码文本字段
 - HiddenField :隐藏文本字段
 - DateField :文本字段,值为 datetime.date 格式
 - DateTimeField :文本字段,值为 datetime.datetime 格式
 - IntegerField :文本字段,值为整数
 - DecimalField :文本字段,值为 decimal.Decimal
 - FloatField :文本字段,值为浮点数
 - BooleanField :复选框,值为 True 和 False
 - RadioField :一组单选框
 - SelectField :下拉列表
 - SelectMultipleField :下拉列表,可选择多个值
 - FileField :文件上传字段
 - SubmitField :表单提交按钮
 - FormField:把表单作为字段嵌入另一个表单
 - FieldList:一组指定类型的字段

WTForms验证函数:
    
 - Email :验证电子邮件地址
 - EqualTo :比较两个字段的值;常用于要求输入两次密码进行确认的情况 IPAddress 验证 IPv4 网络地址
 - Length :验证输入字符串的长度
 - NumberRange :验证输入的值在数字范围内
 - Optional :无输入值时跳过其他验证函数
 - Required :确保字段中有数据
 - Regexp :使用正则表达式验证输入值
 - URL :验证 URL
 - AnyOf :确保输入值在可选值列表中
 - NoneOf :确保输入值不在可选值列表中

把表单渲染成HTML
----------------------

::

    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.submit() }}
    </form>

要想改进表单的外观,可以把参数传入渲染字段的函数,传入 的参数会被转换成字段的 HTML 属性

::

    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name(id='my-text-field') }} 
        {{ form.submit() }}
    </form>

**渲染出来再定义有的场景不合适，还有另外一种渲染方式用render_kw**
::

    verification_code = StringField('验证码', validators=[DataRequired(), render_kw={'style':'width:100px;'})

**修改flask-bootstrap的js和css为本地，！在配置文件中设置**
::

    BOOTSTRAP_SERVE_LOCAL = True


即便能指定 HTML 属性,但按照这种方式渲染表单的工作量还是很大,所以在条件允许的 情况下最好能使用 Bootstrap 中的表单样式。Flask-Bootstrap 提供了一个非常高端的辅助函 数,可以使用 Bootstrap 中预先定义好的表单样式渲染整个 Flask-WTF 表单,而这些操作 只需一次调用即可完成。使用 Flask-Bootstrap,上述表单可使用下面的方式渲染:



::

    {% import "bootstrap/wtf.html" as wtf %} 
    {{ wtf.quick_form(form) }}

import 指令的使用方法和普通 Python 代码一样,允许导入模板中的元素并用在多个模板 中。导入的 bootstrap/wtf.html 文件中定义了一个使用 Bootstrap 渲染 Falsk-WTF 表单对象 的辅助函数。wtf.quick_form() 函数的参数为 Flask-WTF 表单对象,使用 Bootstrap 的默认 样式渲染传入的表单

 .. literalinclude:: code/code4-3.html
    :language: html

在视图函数中处理表单
--------------------------

视图函数 index() 不仅要渲染表单,还要接收表单中的数据::

    @app.route('/', methods=['GET', 'POST'])
    def index():
        name = None
        form = NameForm()
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''
        return render_template('index.html', form=form, name=name)

app.route 修饰器中添加的 methods 参数告诉 Flask 在 URL 映射中把这个视图函数注册为 GET 和 POST 请求的处理程序。如果没指定 methods 参数,就只把视图函数注册为 GET 请求 的处理程序。

把 POST 加入方法列表很有必要,因为将提交表单作为 POST 请求进行处理更加便利。表单 也可作为 GET 请求提交,不过 GET 请求没有主体,提交的数据以查询字符串的形式附加到 URL 中,可在浏览器的地址栏中看到。基于这个以及其他多个原因,提交表单大都作为 POST 请求进行处理。

重定向和用户会话
----------------------

注意使用methods=['GET', 'POST']

 .. literalinclude:: code/code4-5.py
    :language: python

Flash消息
----------------

请求完成后,有时需要让用户知道状态发生了变化。这里可以使用确认消息、警告或者错 误提醒。一个典型例子是,用户提交了有一项错误的登录表单后,服务器发回的响应重新 渲染了登录表单,并在表单上面显示一个消息,提示用户用户名或密码错误。

**这种功能是 Flask 的核心特性。**

 .. literalinclude:: code/code4-6.py
    :language: python

仅调用 flash() 函数并不能把消息显示出来,程序使用的模板要渲染这些消息。最好在 基模板中渲染 Flash 消息,因为这样所有页面都能使用这些消息。Flask 把 get_flashed_messages() 函数开放给模板,用来获取并渲染消息,

 .. literalinclude:: code/code4-7.html
    :language: html

在模板中使用循环是因为在之前的请求循环中每次调用 flash() 函数时都会生成一个消息, 所以可能有多个消息在排队等待显示。get_flashed_messages() 函数获取的消息在下次调 用时不会再次返回,因此 Flash 消息只显示一次,然后就消失了。



.. include:: ../../../ad.rst



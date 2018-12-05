第七章：大型程序的结构
=====================================


**这里组建大型项目结构，其实有更便捷的模板构建工具cookiecutter，省得每次项目都手动创建项目结构**

尽管在单一脚本中编写小型 Web 程序很方便,但这种方法并不能广泛使用。程序变复杂 后,使用单个大型源码文件会导致很多问题。
不同于大多数其他的 Web 框架,Flask 并不强制要求大型项目使用特定的组织方式,程序 结构的组织方式完全由开发者决定。在本章,我们将介绍一种使用包和模块组织大型程序 的方式。本书后续示例都将采用这种结构。

配置选项
--------------

 .. literalinclude:: code/code7-1.py
    :language: python


基类 Config 中包含通用配置,子类分别定义专用的配置。如果需要,你还可添加其他配 置类。

为了让配置方式更灵活且更安全,某些配置可以从环境变量中导入。
**例如,SECRET_KEY 的值,**
这是个敏感信息,可以在环境中设定,但系统也提供了一个默认值,以防环境中没有定义。

在 3 个子类中,SQLALCHEMY_DATABASE_URI 变量都被指定了不同的值。这样程序就可在不同 的配置环境中运行,每个环境都使用不同的数据库。

配置类可以定义 init_app() 类方法,其参数是程序实例。在这个方法中,可以执行对当前 环境的配置初始化。现在,基类 Config 中的 init_app() 方法为空。

在这个配置脚本末尾,config 字典中注册了不同的配置环境,而且还注册了一个默认配置 (本例的开发环境)。

程序包
-----------

程序包用来保存程序的所有代码、模板和静态文件。我们可以把这个包直接称为 app(应 用),如果有需求,也可使用一个程序专用名字。templates 和 static 文件夹是程序包的一部 分,因此这两个文件夹被移到了 app 中。数据库模型和电子邮件支持函数也被移到了这个 包中,分别保存为 app/models.py 和 app/email.py。

使用程序工厂函数
--------------------------

在单个文件中开发程序很方便,但却有个很大的缺点,因为程序在全局作用域中创建,所 以无法动态修改配置。运行脚本时,程序实例已经创建,再修改配置为时已晚。这一点对 单元测试尤其重要,因为有时为了提高测试覆盖度,必须在不同的配置环境中运行程序。

这个问题的解决方法是延迟创建程序实例,把创建过程移到可显式调用的工厂函数中。这 种方法不仅可以给脚本留出配置程序的时间,还能够创建多个程序实例,这些实例有时在 测试中非常有用。程序的工厂函数在 app 包的构造文件中定义

构造文件导入了大多数正在使用的 Flask 扩展。由于尚未初始化所需的程序实例,所以没 有初始化扩展,创建扩展类时没有向构造函数传入参数。create_app() 函数就是程序的工 厂函数,接受一个参数,是程序使用的配置名。配置类在 config.py 文件中定义,其中保存 的配置可以使用Flask app.config配置对象提供的from_object()方法直接导入程序。至 于配置对象,则可以通过名字从 config 字典中选择。程序创建并配置好后,就能初始化 扩展了。在之前创建的扩展对象上调用 init_app() 可以完成初始化过程。

app/__init__.py:程序包的构造文件:

 .. literalinclude:: code/code7-2.py
    :language: python


工厂函数返回创建的程序示例,不过要注意,现在工厂函数创建的程序还不完整,因为没 有路由和自定义的错误页面处理程序。这是下一节要讲的话题。

在蓝本中实现程序功能
-----------------------------

转换成程序工厂函数的操作让定义路由变复杂了。在单脚本程序中,程序实例存在于全 局作用域中,路由可以直接使用 app.route 修饰器定义。但现在程序在运行时创建,只 有调用 create_app() 之后才能使用 app.route 修饰器,这时定义路由就太晚了。和路由 一样,自定义的错误页面处理程序也面临相同的困难,因为错误页面处理程序使用 app. errorhandler 修饰器定义。

幸好 Flask 使用蓝本提供了更好的解决方法。蓝本和程序类似,也可以定义路由。不同的 是,在蓝本中定义的路由处于休眠状态,直到蓝本注册到程序上后,路由才真正成为程序 的一部分。使用位于全局作用域中的蓝本时,定义路由的方法几乎和单脚本程序一样。

和程序一样,蓝本可以在单个文件中定义,也可使用更结构化的方式在包中的多个模块中 创建。为了获得最大的灵活性,程序包中创建了一个子包,用于保存蓝本。示例 7-4 是这 个子包的构造文件,蓝本就创建于此。

app/main/__init__.py:创建蓝本::

    from flask import Blueprint
    main = Blueprint('main', __name__)
    from . import views, errors

通过实例化一个 Blueprint 类对象可以创建蓝本。这个构造函数有两个必须指定的参数: 蓝本的名字和蓝本所在的包或模块。和程序一样,大多数情况下第二个参数使用 Python 的 __name__ 变量即可。

程序的路由保存在包里的 app/main/views.py 模块中,而错误处理程序保存在 app/main/ errors.py 模块中。导入这两个模块就能把路由和错误处理程序与蓝本关联起来。注意,这 些模块在 app/main/__init__.py 脚本的末尾导入,这是为了避免循环导入依赖,因为在 views.py 和 errors.py 中还要导入蓝本 main。

蓝本在工厂函数 create_app() 中注册到程序上::

    def create_app(config_name):
        #...
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)
        return app

app/main/errors.py:蓝本中的错误处理程序::

    from flask import render_template
    from . import main        

    @main.app_errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @main.app_errorhandler(500)
    def internal_server_error(e)
        return render_template('500.html'), 500

在蓝本中编写错误处理程序稍有不同,如果使用 errorhandler 修饰器,那么只有蓝本中的错误才能触发处理程序。要想注册程序全局的错误处理程序,必须使用 app_errorhandler。


app/main/views.py:蓝本中定义的程序路由

 .. literalinclude:: code/code7-3.py
    :language: python

在蓝本中编写视图函数主要有两点不同:第一,和前面的错误处理程序一样,路由修饰器 由蓝本提供;第二,url_for() 函数的用法不同。你可能还记得,url_for() 函数的第一 个参数是路由的端点名,在程序的路由中,默认为视图函数的名字。例如,在单脚本程序 中,index() 视图函数的 URL 可使用 url_for('index') 获取。

在蓝本中就不一样了,Flask 会为蓝本中的全部端点加上一个命名空间,这样就可以在不
同的蓝本中使用相同的端点名定义视图函数,而不会产生冲突。命名空间就是蓝本的名字 (Blueprint 构造函数的第一个参数),所以视图函数 index() 注册的端点名是 main.index,其 URL 使用 url_for('main.index') 获取。

url_for() 函数还支持一种简写的端点形式,在蓝本中可以省略蓝本名,例如url_for('. index')。在这种写法中,命名空间是当前请求所在的蓝本。这意味着同一蓝本中的重定向 可以使用简写形式,但跨蓝本的重定向必须使用带有命名空间的端点名。

为了完全修改程序的页面,表单对象也要移到蓝本中,保存于 app/main/forms.py 模块。

启动脚本
---------

顶级文件夹中的 manage.py 文件用于启动程序。
manage.py:

 .. literalinclude:: code/code7-4.py
    :language: python

这个脚本先创建程序。如果已经定义了环境变量 FLASK_CONFIG,则从中读取配置名;否则 使用默认配置。然后初始化 Flask-Script、Flask-Migrate 和为 Python shell 定义的上下文。

出于便利,脚本中加入了 shebang 声明,所以在基于 Unix 的操作系统中可以通过 ./manage. py执行脚本,而不用使用复杂的python manage.py。

需求文件
------------

程序中必须包含一个 requirements.txt 文件,用于记录所有依赖包及其精确的版本号。如果 要在另一台电脑上重新生成虚拟环境,这个文件的重要性就体现出来了,例如部署程序时 使用的电脑。pip 可以使用如下命令自动生成这个文件:

::

    (venv) $ pip freeze >requirements.txt

**安装或升级包后,最好更新这个文件。**

如果你要创建这个虚拟环境的完全副本,可以创建一个新的虚拟环境,并在其上运行以下 命令::

    (venv) $ pip install -r requirements.txt

当你阅读本书时,该示例 requirements.txt 文件中的版本号可能已经过期了。如果愿意,你 可以试着使用这些包的最新版。如果遇到问题,你可以随时换回这个需求文件中的版本, 因为这些版本和程序兼容。


单元测试
--------------    


 .. literalinclude:: code/code7-5.py
    :language: python

这个测试使用 Python 标准库中的 unittest 包编写。setUp() 和 tearDown() 方法分别在各 测试前后运行,并且名字以 test_开头的函数都作为测试执行。

setUp() 方法尝试创建一个测试环境,类似于运行中的程序。首先,使用测试配置创建程 序,然后激活上下文。这一步的作用是确保能在测试中使用 current_app,像普通请求一 样。然后创建一个全新的数据库,以备不时之需。数据库和程序上下文在 tearDown() 方法 中删除。

第一个测试确保程序实例存在。第二个测试确保程序在测试配置中运行。若想把 tests 文 件夹作为包使用,需要添加 tests/__init__.py 文件,不过这个文件可以为空,因为 unittest 包会扫描所有模块并查找测试。

为了运行单元测试,你可以在 manage.py 脚本中添加一个自定义命令::

    @manager.command
    def test():
        """Run the unit tests."""
        import unittest
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner(verbosity=2).run(tests)

manager.command 修饰器让自定义命令变得简单。修饰函数名就是命令名,函数的文档字符 串会显示在帮助消息中。test() 函数的定义体中调用了 unittest 包提供的测试运行函数。

单元测试可使用下面的命令运行::

    (venv) $ python manage.py test
    test_app_exists (test_basics.BasicsTestCase) ... ok
    test_app_is_testing (test_basics.BasicsTestCase) ... ok
    .----------------------------------------------------------------------
    Ran 2 tests in 0.001s
    OK


创建数据库
-------------

重组后的程序和单脚本版本使用不同的数据库。

首选从环境变量中读取数据库的 URL,同时还提供了一个默认的 SQLite 数据库做备用。3 种配置环境中的环境变量名和 SQLite 数据库文件名都不一样。例如,在开发环境中,数据 库 URL 从环境变量 DEV_DATABASE_URL 中读取,如果没有定义这个环境变量,则使用名为 data-dev.sqlite 的 SQLite 数据库。

不管从哪里获取数据库 URL,都要在新数据库中创建数据表。如果使用 Flask-Migrate 跟 踪迁移,可使用如下命令创建数据表或者升级到最新修订版本::

    (venv) $ python manage.py db upgrade

不管你是否相信,第一部分到此就要结束了。现在你已经学到了使用 Flask 开发 Web 程序 的必备基础知识,不过可能还不确定如何把这些知识融贯起来开发一个真正的程序。本书 第二部分的目的就是解决这个问题,带着你一步一步地开发出一个完整的程序。



.. include:: ../../../ad.rst      
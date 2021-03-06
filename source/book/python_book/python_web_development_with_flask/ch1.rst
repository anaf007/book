第一章、初识Flask
=======================================================================

介绍pipenv：
    pipenv是基于pip的python的包管理工具。他的语法与pip 相似

创建虚拟环境::

    pip install virtualenv 

    python -m virtuelanv venv\

    venv\script\activate

    source venv\bin\activate


安装flask：
    pip install flask


基本程序::

    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def index():
        return "flask "

``启动开发服务器``

flask通过依赖包click内置一个CLI系统。安装flask会会自动添加一个flask命令脚本，可以直接使用 **flask run** 运行脚本。

自动发现程序实例：

自动探测有以下规则：
 - 从当前目录寻找app.py和wsgi.py模块，并从中寻找命位app或application的程序实例
 - 从环境变量FLASK_APP对应的值寻找名为app或application的程序实例。

可以这样设置环境变量赋值：

linux/mac :
    export FLASK_APP=index.py

windows:
    set FLASK_APP=index.py

管理环境变量：
    flask自动发现程序实例机制还有第三条规则，如果安装了python-dotenv，name在使用flask run命令或其他命令时会自动从.flaskenv或.env文件中加载环境变量。

外部服务器访问：
    flask run --host=0.0.0.0 -p 端口号

还可以使用ngrok、localtunnel等内网穿透工具。

``Python Shell``

shell：
    flask shell


``Flask扩展``

大部分扩展会提供一个扩展类，实例化这个类并创建我们创建的程序实例app作为参数即可完成初始化过程。

日常开发中，大多数情况下我们没有必要重复造轮子

``项目配置``

在flask中，配置变量就是一些大写形式的python变量。这些配置变量都通过flask对象的app.config属性作为统一的接口来设置获取，

配置的名称必须是全大写形式，小写的变量将不会被读取。

使用app.config.update(xxx=xxx)可以加载设置多个值

``URL与端点``

::

    @app.route('/')
    def index():
        return 'index'

以上就获得了端点 主页 “/” 连接地址

使用url_for('index',name="hello")

url_for('index',_external=True,name="hello")获得绝对路径

``Flask命令``

::

    @app.cli.command()
    def hello():
        click.echo('hello')

flask hello

这里作为初始化数据很实用

``模板与静态文件``

模板文件存放在项目目录中的templates文件夹中

静态文件存放在static文件夹中。

CDN指分布式服务器系统，，可以加速网页资源的加载速度，优化用户体验

1.10 FLask与MVC架构
---------------------------------------------------------------------

flask并不是MVC架构的框架。




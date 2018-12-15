第一章、初识Flask
=======================================================================



介绍pipenv：
    pipenv是基于pip的python的包管理工具。他的语法与pip 相似

创建虚拟环境

安装flask：
    pip install flask

基本程序::

    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def index():
        return "flask "

flask通过依赖包click内置一个CLI系统。安装flask会会自动添加一个flask命令脚本，可以直接使用**flask run**运行脚本。

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
    flask run --host=0.0.0.0

还可以使用ngrok、localtunnel等内网穿透工具。

shell：
    flask shell





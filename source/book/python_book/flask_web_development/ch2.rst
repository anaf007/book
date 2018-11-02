第二章：程序基本结构
============================

初始化::

	from flask import Flask
	app = Flask(__name__)

路由和视图函数::

	@app.route('/')
	def index():
	    return '<h1>Hello World!</h1>'

动态可变的部分name::

	@app.route('/user/<name>')
	def user(name):
	    return '<h1>Hello, %s!</h1>' % name


启动服务器::

	if __name__ == '__main__':
	    app.run(debug=True)

完整的程序::

	from flask import Flask app = Flask(__name__)

	@app.route('/')
	def index():
	    return '<h1>Hello World!</h1>'

	if __name__ == '__main__':
	    app.run(debug=True)	 

运行程序::

	(venv) $ python hello.py
	* Running on http://127.0.0.1:5000/
	* Restarting with reloader	 


**上下文的概念重之之重，现在刚开始学知道有这么一个东西就好**

*Flask上下文全局变量*::

	current_app:当前激活程序的程序实例
	g:处理请求时用作临时存储的对象。每次请求都会重设这个变量
	request:请求对象,封装了客户端发出的 HTTP 请求中的内容
	session:用户会话,用于存储请求之间需要“记住”的值的词典



请求钩子
------------

也是常用的模块，比如登录验证::
	
	before_first_request:注册一个函数,在处理第一个请求之前运行。
	before_request:注册一个函数,在每次请求之前运行。
	after_request:注册一个函数,如果没有未处理的异常抛出,在每次请求之后运行。
	teardown_request:注册一个函数,即使有未处理的异常抛出,也在每次请求之后运行。

响应
---------
:这个http协议内容，可以这样设置返回的状态::

	@app.route('/')
	def index():
	    return '<h1>Bad Request</h1>', 400


Response::

	from flask import make_response
	@app.route('/')
	def index():
	    response = make_response('<h1>This document carries a cookie!</h1>')
        response.set_cookie('answer', '42')
        return response

redirect跳转及404::

	from flask import redirect
	@app.route('/')
	def index():
	    return redirect('http://www.example.com')   

	from flask import abort
	@app.route('/user/<id>')
	def get_user(id):
	    user = load_user(id)
	    if not user:
	        abort(404)
	    return '<h1>Hello, %s</h1>' % user.name    


Flask扩展
---------------
	
Flask 被设计为可扩展形式,故而没有提供一些重要的功能,例如数据库和用户认证,所
以开发者可以自由选择最适合程序的包,或者按需求自行开发。

社区成员开发了大量不同用途的扩展,如果这还不能满足需求,你还可使用所有 Python 标 准包或代码库。

使用Flask-Script支持命令行选项
---------------------------------

Flask 的开发 Web 服务器支持很多启动设置选项,但只能在脚本中作为参数传给 app.run()函数。这种方式并不十分方便,传递设置选项的理想方式是使用命令行参数。


Flask-Script 是一个 Flask 扩展,为 Flask程序添加了一个命令行解析器。Flask-Script 自带了一组常用选项,而且还支持自定义命令。(版本更新这个插件已经弃用了。)

Flask-Script扩展使用pip安装::

	(venv) $ pip install flask-script

	from flask.ext.script import Manager 
	manager = Manager(app)
	# ...
	if __name__ == '__main__':
	    manager.run()

可以这样启动：python hello.py runserver --help

这样可以其他电脑访问：python hello.py runserver --host 0.0.0.0  
mac下可能有绑定限制 


.. include:: ../../../ad.rst


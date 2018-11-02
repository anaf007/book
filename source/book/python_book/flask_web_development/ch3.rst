============================
第三章：模板
============================


**默认情况下,Flask 在程序文件夹中的 templates子文件夹中寻找模板。**

-------------
渲染模板
-------------

.. literalinclude:: code/code3-1.py
    :language: python



变量
-----------

在模板中使用的{{ name }}结构表示一个变量,它是一种特殊的占位符,告诉模
板引擎这个位置的值从渲染模板时使用的数据中获取。


**Jinja2能识别所有类型的变量,甚至是一些复杂的类型,例如列表、字典和对象。在模板 中使用变量的一些示例如下** ::

     <p>A value from a dictionary: {{ mydict['key'] }}.</p>
     <p>A value from a list: {{ mylist[3] }}.</p>
     <p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
     <p>A value from an object's method: {{ myobj.somemethod() }}.</p>


可以使用过滤器修改变量,过滤器名添加在变量名之后,中间使用竖线分隔。例如,下述 模板以首字母大写形式显示变量 name 的值::
     
     Hello, {{ name|capitalize }}


Jinja2 提供的部分常用过滤器::

	safe:渲染值时不转义
	capitalize:把值的首字母转换成大写,其他字母转换成小写 lower 把值转换成小写形式
	upper:把值转换成大写形式
	title:把值中每个单词的首字母都转换成大写
	trim:把值的首尾空格去掉
	striptags:渲染之前把值中所有的 HTML 标签都删掉


safe 过滤器值得特别说明一下。默认情况下,出于安全考虑,Jinja2 会转义所有变量。例 如,如果一个变量的值为 '<h1>Hello</h1>',Jinja2 会将其渲染成 '&lt;h1&gt;Hello&lt;/ h1&gt;',浏览器能显示这个 h1 元素,但不会进行解释。很多情况下需要显示变量中存储 的 HTML 代码,这时就可使用 safe 过滤器。

控制结构
-------------

条件控制语句和循环语句::

	{% if user %}
	Hello, {{ user }}!
	{% else %}
	Hello, Stranger!
	{% endif %}

	<ul>
	{% for comment in comments %}
	<li>{{ comment }}</li> {% endfor %}
	</ul>

Jinja2还支持宏,宏类似于Python代码中的函数《本人觉得不常用，欢迎反驳他的好处，请加18977771077一起讨论》。例如::

	{% macro render_comment(comment) %} <li>{{ comment }}</li>
	{% endmacro %}
	<ul>
	{% for comment in comments %}
	{{ render_comment(comment) }} {% endfor %}
	</ul>


为了重复使用宏,我们可以将其保存在单独的文件中,然后在需要使用的模板中导入::

	{% import 'macros.html' as macros %} <ul>
	{% for comment in comments %}
	{{ macros.render_comment(comment) }}
	{% endfor %} </ul>

**需要在多处重复使用的模板代码片段可以写入单独的文件,再包含在所有模板中,以避免 重复《这个就很实用必须要用》**::	
	
	{% include 'common.html' %}

**还有另外一种很实用学会很有帮助的**，另一种重复使用代码的强大方式是模板继承,它类似于 Python 代码中的类继承。首先,创建一个名为 base.html 的基模板::
	
	<html>
	<head>
	{% block head %}
	<title>{% block title %}{% endblock %} - My Application</title> 
	{% endblock %}
	</head>
	<body>
	{% block body %}
	{% endblock %} </body>
	</html>

block 标签定义的元素可在衍生模板中修改。在本例中,我们定义了名为 head、title 和body 的块。注意,title 包含在 head 中。下面这个示例是基模板的衍生模板::

	{% extends "base.html" %}
	{% block title %}Index{% endblock %} {% block head %}
	{{ super() }}
	<style>
	</style>
	{% endblock %}
	{% block body %} 
	<h1>Hello, World!</h1> 
	{% endblock %}

extends 指令声明这个模板衍生自 base.html。在 extends 指令之后,基模板中的 3 个块被 重新定义,模板引擎会将其插入适当的位置。注意新定义的 head 块,在基模板中其内容不 是空的,**所以使用 super() 获取原来的内容**。

使用Flask-Bootstrap集成Twitter Bootstrap
-----------------------------------------------------

Bootstrap 是客户端框架,因此不会直接涉及服务器。服务器需要做的只是提供引用了 Bootstrap 层叠样式表(CSS)和 JavaScript 文件的 HTML 响应,并在 HTML、CSS 和 JavaScript 代码中实例化所需组件。这些操作最理想的执行场所就是模板。

::
	
	(venv) $ pip install flask-bootstrap


hello.py:初始化 Flask-Bootstrap::
	
	from flask.ext.bootstrap import Bootstrap
	#...
	bootstrap = Bootstrap(app)

templates/user.html:使用 Flask-Bootstrap 的模板

.. literalinclude:: code/code3-5.html
    :language: html


Jinja2 中的 extends 指令从 Flask-Bootstrap 中导入 bootstrap/base.html,从而实现模板继
承。Flask-Bootstrap 中的基模板提供了一个网页框架,引入了 Bootstrap 中的所有 CSS 和JavaScript 文件。

很多块都是 Flask-Bootstrap 自用的,如果直接重定义可能会导致一些问题。例 如,Bootstrap 所需的文件在 styles 和 scripts 块中声明。
**如果程序需要向已经有内容的块 中添加新内容,必须使用 Jinja2 提供的 super() 函数。**
例如,如果要在衍生模板中添加新 的 JavaScript 文件,需要这么定义 scripts 块::
	
	{% block scripts %}
	{{ super() }}
	<script type="text/javascript" src="my-script.js"></script> 
	{% endblock %}


自定义错误页面
-----------------

如果你在浏览器的地址栏中输入了不可用的路由,那么会显示一个状态码为 404 的错误页
面。现在这个错误页面太简陋、平庸,而且样式和使用了 Bootstrap 的页面不一致。
像常规路由一样,Flask 允许程序使用基于模板的自定义错误页面。最常见的错误代码有 两个:404,客户端请求未知页面或路由时显示;500,有未处理的异常时显示。

::

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

和视图函数一样,错误处理程序也会返回响应。它们还返回与该错误对应的数字状态码。

错误处理程序中引用的模板也需要编写。

示例 3-7 templates/base.html:包含导航条的程序基模板::

 .. literalinclude:: code/code3-7.html
    :language: html

这个模板的 content 块中只有一个 <div> 容器,其中包含了一个名为 page_content 的新的空块,块中的内容由衍生模板定义。 

现在,程序使用的模板继承自这个模板,而不直接继承自 Flask-Bootstrap 的基模板。通过继承 templates/base.html 模板编写自定义的 404 错误页面很简单.

 .. literalinclude:: code/code3-8.html
    :language: html


链接
---------

任何具有多个路由的程序都需要可以连接不同页面的链接,例如导航条。

在模板中直接编写简单路由的 URL 链接不难,但对于包含可变部分的动态路由,在模板 中构建正确的 URL 就很困难。而且,直接编写 URL 会对代码中定义的路由产生不必要的 依赖关系。如果重新定义路由,模板中的链接可能会失效。

为了避免这些问题,Flask 提供了 url_for() 辅助函数,它可以使用程序 URL 映射中保存 的信息生成 URL。

url_for() 函数最简单的用法是以视图函数名(或者 app.add_url_route() 定义路由时使用 的端点名)作为参数,返回对应的 URL。例如,在当前版本的 hello.py 程序中调用 url_for('index')得到的结果是/。调用
**url_for('index', _external=True)**
返回的则是绝对地 址,在这个示例中是 http://localhost:5000/。

使用 url_for() 生成动态地址时,将动态部分作为关键字参数传入。例如,
**url_for ('user', name='john', _external=True)**
的返回结果是http://localhost:5000/user/john。

传入 url_for()的关键字参数不仅限于动态路由中的参数。函数能将任何额外参数添加到 查询字符串中。例如,url_for('index', page=2)的返回结果是/?page=2。


静态文件
--------------

**调用 url_for('static', filename='css/styles.css', _external=True) 得 到 的 结 果 是 http:// localhost:5000/static/css/styles.css。**

默认设置下,Flask 在程序根目录中名为 static 的子目录中寻找静态文件。如果需要,可在 static 文件夹中使用子文件夹存放文件。服务器收到前面那个 URL 后,会生成一个响应, 包含文件系统中 static/css/styles.css 文件的内容。

 .. literalinclude:: code/code3-10.html
    :language: html



使用Flask-Moment本地化日期和时间
---------------------------------------

讲真  一般博主不用。

如果 Web 程序的用户来自世界各地,那么处理日期和时间可不是一个简单的任务。

服务器需要统一时间单位,这和用户所在的地理位置无关,所以一般使用协调世界时 (Coordinated Universal Time,UTC)。不过用户看到UTC格式的时间会感到困惑,他们更希望看到当地时间,而且采用当地惯用的格式。

有一个使用 JavaScript 开发的优秀客户端开源代码库,名为 moment.js(http://momentjs. com/),它可以在浏览器中渲染日期和时间。Flask-Moment 是一个 Flask 程序扩展,能把 moment.js 集成到 Jinja2 模板中。Flask-Moment 可以使用 pip 安装::

	(venv) $ pip install flask-moment
	from flask.ext.moment import Moment
	moment = Moment(app)

除了 moment.js,Flask-Moment 还依赖 jquery.js。要在 HTML 文档的某个地方引入这两个 库,可以直接引入,这样可以选择使用哪个版本,也可使用扩展提供的辅助函数,从内容 分发网络(Content Delivery Network,CDN)中引入通过测试的版本。Bootstrap已经引入 了 jquery.js,因此只需引入 moment.js 即可。示例 3-12 展示了如何在基模板的 scripts 块 中引入这个库。

::
	
	{% block scripts %}
	{{ super() }}
	{{ moment.include_moment() }} 
	{% endblock %}

::
	
	from datetime import datetime
	@app.route('/')
	def index():
		return render_template('index.html',current_time=datetime.utcnow())

templates/index.html::

	<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
	<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>

format('LLL') 根据客户端电脑中的时区和区域设置渲染日期和时间。参数决定了渲染的方 式,'L' 到 'LLLL' 分别对应不同的复杂度。format() 函数还可接受自定义的格式说明符。

第二行中的 fromNow() 渲染相对时间戳,而且会随着时间的推移自动刷新显示的时间。这 个时间戳最开始显示为“a few seconds ago”,但指定refresh参数后,其内容会随着时 间的推移而更新。如果一直待在这个页面,几分钟后,会看到显示的文本变成“a minute ago”“2 minutes ago”等。

Flask-Moment 实现了 moment.js 中的 format()、fromNow()、fromTime()、calendar()、valueOf() 和 unix() 方法。你可查阅文档(http://momentjs.com/docs/#/displaying/)学习 moment.js 提供的全部格式化选项。

Flask-Moment 渲染的时间戳可实现多种语言的本地化。语言可在模板中选择,把语言代码 传给 lang() 函数即可::

	{{ moment.lang('es') }}


使用本章介绍的技术,你应该能为程序编写出现代化且用户友好的网页。下一章将介绍本 章没有涉及的一个模板功能,即如何通过 Web 表单和用户交互。



.. include:: ../../../ad.rst




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

很多块都是 Flask-Bootstrap 自用的,如果直接重定义可能会导致一些问题。例 如,Bootstrap 所需的文件在 styles 和 scripts 块中声明。如果程序需要向已经有内容的块 中添加新内容,必须使用 Jinja2 提供的 super() 函数。例如,如果要在衍生模板中添加新 的 JavaScript 文件,需要这么定义 scripts 块::
	
	{% block scripts %}
	{{ super() }}
	<script type="text/javascript" src="my-script.js"></script> {% endblock %}





.. include:: ../../../ad.rst




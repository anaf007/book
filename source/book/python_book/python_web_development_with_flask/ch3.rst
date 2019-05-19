第三章、模板
=======================================================================

3.1 模板基本用法
---------------------------------------------------------------------

::

    #if for
    {% %}
    #变量
    {{}}
    #注释
    {##}

模板中允许使用大部分python对象，比如字符串、列表、字典、元祖、整形、浮点型、布尔型  运算符：+-\*/ 比较符号  == != 逻辑 and or not 以及in is None 

::

    {%if xx%}
    {%endif %}

    {%for xx%}
    {%endfor%}

for循环特殊变量：
 - loop.index
 - loop.index0
 - loop.revindex
 - loop.revindex0
 - loop.first
 - loop.last
 - loop.previtem 
 - loop.nextitem
 - loop.length


3.2 模板辅助工具
---------------------------------------------------------------------

除了渲染时传入的变量，也可以在模板中定义变量，使用set标签::

    {%set navigation = [('/','Home'),('/about','About')]%}

    {%set nacigation%}
        <li><a href="/">Home</a></li>
    {%endset%}

模板全局变量:
 - config :当前配置对象
 - request ： 当前请求对象，在已激活的请求环境下可用
 - session ： 当前会话对象 ，在已激活的请求环境下可用
 - g ： 与请求绑定的全局变量，在已激活的请求环境下可用。

flask提供了一个app.context_processor装饰器，可以用来注册模板上下文处理函数，他可以帮我们完成统一传入变量的工作，需要返回一个键值字典

lambda简化：app.context_processor(lambdaLdict(fo='fo'))

jinja2内置全局函数:
 - range ： 和python的range()相同
 - lipsum ：生成随机文本
 - dict ： 和python的dict()相同

flask内置模板全局函数:
 - url_for() ： 生成url的函数
 - get_flashed_messages() 获取flash消息的函数

自定义全局函数：app.template_global()


过滤器：
 - default ： 设置默认值
 - first    ： 返回序列第一个元素
 - escape   ：转移html文本
 - last ：返回最后一个元素
 - length ：返回变量长度
 - random ： 返回序列中的随机元素
 - safe ：将变量标记为安全 ，避免转义
 - trim ：清除变量前后的空格
 - max ： 返回序列中的最大值
 - min ：返回序列中的最小值 
 - unique ：返回序列中的不重复值
 - striptags ：清除变量内的html标签
 - urlize 将url文本转换为可单机的html链接
 - wordcount ： 计算单词数量
 - tojson ： 将变量转换为json格式
 - truncate 阶段字符串，常用语文章摘要。

自定义过滤器： @app.template_filter()


常用内置测试器：
 - callble ： 判断对象是否可被调用 
 - defined ： 判断变量是否已定义
 - undefined ： 判断变量是否未定义
 - none： 判断变量是否为None
 - number ： 判断变量是否为数字
 - string ： 判断变量是否为字符串
 - sequence ： 判断变量是否序列比如字符串、列表、元祖
 - iterable ：判断变量是否可迭代
 - mapping ： 判断变量是否匹配对象，比如字典
 - sameas ：判断变量与other是否指向相同的内存地址

自定义测试器： @app.template_test()



添加自定义全局对象： app.jinja_env.globals['bar'] = fo
添加自定义过滤器： app.jinja_env.filters['smiling'] = smiling
添加自定义测试器：app.jinja_env.tests['baz'] = baz






3.3 模板结构组织
-------------------------------------------------------------------

局部模板：{include '_banner.html'}

宏是jinja2体用一个费用有用的特性，它类似python中的函数。使用宏可以吧一部分模板大妈封装到宏里，使用传递的参数来构建内存


示例::

    {%macro qux(amount=1)%}
        {%if amount == 1%}
            qux
        {%else%}
            no qux
        {%endif%}
    {%endmacro%}

    {%from 'macros.html' import qux%}

    {{qux(amount=5)}}

    #注意这里可能会需要到上下文

    {%from 'macros.html' import qux with context %}


模板继承::

    {%block body%}
    XXXXX
    {%endblock%}

    {%extends 'bases.html'%}

    {%block body%}
    XXXXX
    {%endblock%}


3.4 模板进阶实践
---------------------------------------------------------------------

静态文件::

    url_for('static',filename='style.css')

消息闪现flash::

    {%for message in get_flashed_messages()%}
    xxxx {{message}}
    {%endfor%}

自定义错误页面：app.errorhandler(404)  自定义错误的传入对应的40x 50x

自定义错误页面::

    @app.errorhandler(404)
    def not_page(e):
        return  render_template"error.html",404;


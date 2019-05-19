第二章、Flask与HTTP
=======================================================================

HTTP：超文本传输协议

2.1 请求相应循环
---------------------------------------------------------------------
略

2.2 HTTP请求
---------------------------------------------------------------------

flask内置的url变量转换器：
 - string :不包含斜线的字符串默认
 - int ：整形
 - float ：浮点型
 - path ：包含斜线的字符串，static路由的URL规则中的filename变量就使用了这个转换器
 - any ：匹配一系列给定值中的一个元素
 - uuid ：UUID字符串


请求钩子：
 - before_first_request : 在处理第一个请求前运行
 - before_request ： 在处理每个请求前运行
 - after_before ： 如果没有未处理的异常抛出，会在每个请求结束后运行
 - teardown_request : 及时有未处理的异常抛出会在没请求结束后运行没如果有发生异常 会传入异常对象作为参数到注册的函数中
 - after_this_request ： 在视图函数内注册一个函数，会在这个请求结束后运行

before_first_request： 初始化操作可以使用这个 比如添加管理员创建数据库表等

before_request： 记录用户最后在线时间 

after_this_request： 更新 插入操作等


2.3 HTTP响应
---------------------------------------------------------------------
response类的常用属性和方法：
 - headers ： 相应头部
 - status ： 状态码 文本类型
 - status_code ： 状态码整形
 - mimetype ： MIME类型
 - set_cookie()： 设置一个cookie

set_cookie()方法的参数：
 - key : cookie键
 - value ： cookie值
 - max_age ： 被保存的时间 单位秒 默认关闭浏览器过期 
 - expires ：具体过期时间 一个datetime对象 
 - path ： 限制cookie只在给定的路径可用  默认整个域名
 - domain ： 设置cookie可用的域名 
 - secure ： 如果设置true 只有在https才可以使用
 - httponly ： 如果设置为true 禁止客户端JavaScript获取cookie

设置cookie::
    
    from flask import Flask,make_response

    @app.route('/<name>')
    def index(name):
        response = make_response(url_for('index'))
        response.set_cookie('name',name)
        return response

session: 安全的cookie::

    app.secret_key = 'secret_string'

    SECRET_KEY = 'string'



2.4 FLask上下文
---------------------------------------------------------------------

上下文的概念很重要，异步进行操作的时候不熟悉的话会  各种操作都会报错

flask中的上下文变量：
 - current_app :指初期请求的当前程序实例
 - g ： 替代python的全局变量用法，确保尽在当前请求中可用，用于存储全局数据，每次请求都会重设
 - request ： 封装客户端发出的请求报文数据
 - session  ：用户记住请求之间的数据

2.5 HTTP进阶实践
---------------------------------------------------------------------

获取上一个url：request.referrer 

ajax技术 略

http服务器推送技术：
 - 传统轮询
 - 长轮询
 - sse server-sent events

长轮询 webstock


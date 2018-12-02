第三章：flask web开发
=======================================================================


入门::

    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def index():
        return 'index'

    if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)

    #python index.py


动态url支持的规则:
 - string: 接受任何没有斜杠的文本，默认
 - int：整数
 - float：浮点数
 - path：和默认相似，但是接受斜杠
 - uuid：只接受uuid字符串
 - any：可以指定多种路径，但是需要传入参数

any示例：@app.route('/<any(a,b)>:page_name/'),类似枚举


**自定义url转换器** 
略  具体需要到在查询。

构造url::

    url_for

跳转和重定向：

redirect

静态文件::
    
    url_for('static',filename='style.css')

    app = Flask(__name__,static_folder='/tmp')


即插视图： 略

蓝图：略

子域名 ：略

命令行接口：略

模板：略

使用mysql：略

书中的内容对以上的知识都是简单说明所以内容全略。

理解Context：  重点  ，但是书中内容略 ，书中也是简单概括，可以去官网查询。

次此章节最后  又一个文件托管服务的例子 但是感觉不是很全，具体可以看这里的代码：https://github.com/dongweiming/web_develop/tree/master/chapter3/section5

这个案例涉及的知识点有：
 - python-magic：libmagic的python绑定，用于确定文件类型。
 - pillow：处理图片
 - cropresize2:用来剪切和调整图片大小
 - short_url:创建短连接。











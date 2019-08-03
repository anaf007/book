搜下没有很全的中文官方文档，都是其他个人的笔记很零散的功能。只好看着[官方教程](https://flask-admin.readthedocs.io/en/latest/)自己记录

#2017-08月 温习一遍 发现插件升级了有些地方都不对了  懒得更新代码了

**初始化：**
```python
from flask import Flask
from flask_admin import Admin

app = Flask(__name__)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here
app.run()
```

**添加模型动态视图：**

````python
from flask_admin.contrib.sqla import ModelView
# Flask and Flask-SQLAlchemy initialization here
admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
````
**添加admin/index.html**
```html
{% extends 'admin/master.html' %}

{% block body %}
  <p>Hello world</p>
{% endblock %}
```
**用户认证及其他一些功能列在下面代码注释里:** 
```python
#coding=utf-8
"""filename:app/admin/views.py
Created 2017-06-01
Author: by anaf
note:admin视图函数
"""


from flask import Flask,request,redirect,url_for
from flask.ext.admin import Admin, BaseView, expose
from app import admin_app,db
from app.models import Article,Category,User,User_msg,Category_attribute,Comment
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user,login_required
from wtforms.validators import Required

# class MyView(BaseView):
#   @expose('/')
#   def index(self):
#       return self.render('admin/index.html')


#增加一个导航
# admin_app.add_view(MyView(name=u'文章'))

# admin_app.add_view(ModelView(User,db.session,name=u'用户管理'))


class Admin_v(ModelView):
    #认证
    def is_accessible(self):
        return current_user.is_authenticated
    #不知道干什么用
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

    #是否允许创建、删除、编辑、只读
    can_create = True
    # can_delete = False
    # can_edit = False
    # can_view_details = True
    #每页记录显示行数
    page_size = 50

    #删除行
    # column_exclude_list = ['password', ]

    #搜索列表
    # column_searchable_list = ['username', 'name']
    #筛选列表
    # column_filters = ['location']
    #直接在视图中启用内联编辑，快速编辑行
    column_editable_list = ['name', 'username']
    #直接在当前页弹框 进行 编辑或者添加，  不是很大用
    # create_modal = True
    # edit_modal = True
    #移除创建的字段
    form_excluded_columns = ['comments','last_seen', 'avatar_hash','article_id','followed','followers']
    #form  WTForms 表单验证，详细验证规则 看WTForms 
    form_args={'name':{'label':u'名字','validators':[Required()]}}
    #制定form渲染参数
    form_widget_args = {
                    'about_me': {
                    'rows': 10,
                    'style': 'color: black'
                        }
                    }
    #当表单包含外键时，使用Ajax加载那些相关的模型（没会用）
    # form_ajax_refs = {
    #   'role_id': {
    #       'fields': ['first_name', 'last_name', 'email'],
    #       'page_size': 10
    #       }
    #   }
    #过滤ajax加载的结果 没会用
    # form_ajax_refs = {'active_user': QueryAjaxModelLoader('user', db.session, User,filters=["is_active=True", "id>1000"])}


    # select choices   没有select选择器  不知道效果
    # form_choices = {
    #   'title': [
 #          ('MR', 'Mr'),
 #          ('MRS', 'Mrs'),
 #          ('MS', 'Ms'),
 #          ('DR', 'Dr'),
 #          ('PROF', 'Prof.')
 #          ]
 #        }
    
    
    #列表行重写
    column_labels = {
        'id':u'序号',
        'username' : u'用户账号',
        # 'password_hash':u'密码加密值',
        'name':u'真实姓名',
        'location':u'地址',
        'about_me':u'自我简介',
        'avatar_hash':u'头像加密值',
    }
    column_list = ('id', 'username','name',
                'location','about_me','avatar_hash')

    def __init__(self, session, **kwargs):
        super(Admin_v, self).__init__(User, session, **kwargs)


admin_app.add_view(Admin_v(db.session,name=u'用户管理'))
admin_app.add_view(ModelView(Article,db.session,name=u'文章管理'))
admin_app.add_view(ModelView(Category,db.session,name=u'栏目管理'))
admin_app.add_view(ModelView(User_msg,db.session,name=u'留言管理'))
admin_app.add_view(ModelView(Category_attribute,db.session,name=u'栏目属性表(不要随意更改)'))
admin_app.add_view(ModelView(Comment,db.session,name=u'评论管理'))  


#文件管理
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
path = op.join(op.dirname(__file__), 'static/uploads')
admin_app.add_view(FileAdmin(path,'/static', name=u'静态文件'))

```

**添加 自定义视图**
```python
from flask_admin import BaseView, expose

class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('analytics_index.html')

admin.add_view(AnalyticsView(name='Analytics', endpoint='analytics'))
```
```html
{% extends 'admin/master.html' %}
{% block body %}
  <p>Here I'm going to display some data.</p>
{% endblock %}
```
**重写内置 视图**
```python
from flask_admin.contrib.sqla import ModelView

# Flask and Flask-SQLAlchemy initialization here

class UserView(ModelView):
    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
    """
        Custom create view.
    """

    return self.render('create_user.html')
```

**扩展内置模板**
可扩展的模板：对应继承 列表、创建、编辑页
admin/model/list.html
admin/model/create.html
admin/model/edit.html
例如：
{% extends 'admin/model/edit.html' %}

{% block body %}
    MicroBlog Edit View
    {{ super() }}
{% endblock %}

**使视图使用模板**
```python
class MicroBlogModelView(ModelView):
    edit_template = 'microblog_edit.html'
    # create_template = 'microblog_create.html'
    # list_template = 'microblog_list.html'
```
**如果使用基础模板，则在基础函数中添加**
```python
admin = Admin(app, base_template='microblog_master.html')
```
**重写内置模板**
可用的模板块，首先要定义一个基础模板快：admin/base.html.里面可以定义如下图内容：

![image.png](http://upload-images.jianshu.io/upload_images/2101610-03da4c0d17ef4fee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**admin/model/list.html包含了如下模块：**

![image.png](http://upload-images.jianshu.io/upload_images/2101610-82f542bc0a76bd28.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

可参照这里的[github例子](https://github.com/flask-admin/flask-admin/tree/master/examples/layout)

环境变量，在任何模板下可扩展admin/master.html模板。可用的环境变量有：

![image.png](http://upload-images.jianshu.io/upload_images/2101610-b6d33de1138e3077.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

为特定的视图生成url
```python
from flask import url_for

class MyView(BaseView):
    @expose('/')
    def index(self):
        # Get URL for the test view method
        user_list_url = url_for('user.index_view')
        return self.render('index.html', user_list_url=user_list_url)
url_for('user.edit_view', id=1, url=url_for('user.index_view'))
```
url_for('analytics.index')
admin.add_view(CustomView(name='Analytics', endpoint='analytics'))



---------------------------------------------------------------------
#高级 功能
**防止csrf攻击保护**

指定form_base_class 参数即可
```python
from flask_admin.form import SecureForm
from flask_admin.contrib.sqla import ModelView

class CarAdmin(ModelView):
    form_base_class = SecureForm
```
**格式化语言,显示中文字段**
pip install flask-babelex  #当时下载好多次才成功。6.8m太大了
初始化
from flask import app
from flask_babelex import Babel
app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'

**管理文件和文件夹。上面代码已经集成了**


**添加一个Redis控制器**(没有测试)
```python
from redis import Redis
from flask_admin.contrib import rediscli

# Flask setup here

admin = Admin(app, name='microblog', template_mode='bootstrap3')

admin.add_view(rediscli.RedisCli(Redis()))
```
**替换表单字段**
```python
from wtforms import TextAreaField
from wtforms.widgets import TextArea

class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

class MessageAdmin(ModelView):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    form_overrides = {
        'body': CKTextAreaField
    
```
**↑上面的代码 CKTextAreaField这个放最上面不然提示找不到这个类 **
效果如下图：

![image.png](http://upload-images.jianshu.io/upload_images/2101610-9705b8237c6d50ba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**亲测样子是实现了。但是没法上传图片**
检查了下，发现问题。第一在编辑器的config.js配置上传处理函数：
config.filebrowserImageUploadUrl= "/main/upload";
细节配置参考编辑器的文档
第二编写上传处理函数：
```python
#ckeditor图片上传
def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))

@main.route('/main/upload', methods=['GET','POST'])
@login_required
def UploadFileImage():
    """CKEditor file upload"""
    error = ''
    url = ''
    callback = request.args.get("CKEditorFuncNum")
    if request.method == 'POST' and 'upload' in request.files:
        fileobj = request.files['upload']
        fname, fext = os.path.splitext(fileobj.filename)
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)
        filepath = os.path.join(current_app.static_folder, 'uploads/main', rnd_name)
        
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dirname, os.W_OK):
            error = 'ERROR_DIR_NOT_WRITEABLE'
        if not error:
            fileobj.save(filepath)
            url = url_for('static', filename='%s/%s' % ('uploads/main', rnd_name))
    else:
        error = 'post error'
    res = """

        <script type="text/javascript">
          window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
        </script>

 """ % (callback, url, error)
    response = make_response(res)
    response.headers["Content-Type"] = "text/html"
    return response
```
这时候就可以上传图片了

**头像**
```python
from jinja2 import Markup
#...
    #头像
    def _list_thumbnail(view, context, model, name):
        if not model.avatar_hash:
            return ''
        return Markup('<img src="http://www.gravatar.com/avatar/%s?d=identicon&s=32"' % model.avatar_hash)

    column_formatters = {'avatar_hash': _list_thumbnail}
#...
```
效果图，看最后的小图像：

![image.png](http://upload-images.jianshu.io/upload_images/2101610-b0e48bfba73cd872.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
可以看到自我简介就上传了一张 图片。但是里面的内容非常的长。
想不到什么办法只好这样处理的，虽然不是很妥当：
```python
def _list_about_me_sub(view, context, model, name):
        return model.about_me[0:50]#截取50个字符

    column_formatters = {'avatar_hash': _list_thumbnail,'about_me':_list_about_me_sub}

```

看起来是这样：

![image.png](http://upload-images.jianshu.io/upload_images/2101610-e7a1581dc3b205c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

下面的的教程就是地理位置了 。这个不需要。有需要的自己看下文档吧[github上的flask-admin的地理位置文档](https://github.com/flask-admin/flask-admin/tree/master/examples/geo_alchemy)

**通过渲染规则自定义内置表单**
```python
from flask_admin.form import rules
form_create_rules = ('location', rules.HTML('<input type="text" />'), 'username', 'about_me')

```
效果图，看到左边多了一个文本框就是自定义添加的：

![image.png](http://upload-images.jianshu.io/upload_images/2101610-14dfece121b65e0e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
rules支持的类型如下图：

![image.png](http://upload-images.jianshu.io/upload_images/2101610-f2e26e6164d015d4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**重写表格**
```python
class MyView(ModelView):
    def scaffold_form(self):
        form_class = super(UserView, self).scaffold_form()
        form_class.extra = StringField('Extra')
        return form_class
```
反正我没有重写

**自定义批量操作**
```python
from flask_admin.actions import action

class UserView(ModelView):
    @action('approve', 'Approve', 'Are you sure you want to approve selected users?')
    def action_approve(self, ids):
        try:
            query = User.query.filter(User.id.in_(ids))

            count = 0
            for user in query.all():
                if user.approve():
                    count += 1

            flash(ngettext('User was successfully approved.',
                           '%(count)s users were successfully approved.',
                           count,
                           count=count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash(gettext('Failed to approve users. %(error)s', error=str(ex)), 'error')
```
还没有去尝试添加自定义操作，就是除了系统自带的增删改查基础上增加自己的功能操作
基本以上的操作都可以满足大部分功能了。教程也就到这里吧，应该是目前最全的了


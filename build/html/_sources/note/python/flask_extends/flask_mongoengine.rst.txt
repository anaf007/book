flask-mongoengine扩展
====================================================================

time:2018-09-25

flask的扩展，提供了与MongoEngine的集成，详细查看MongoEngine的文档 http://docs.mongoengine.org/

安装flask-mongoengine::

    pip install flask-mongoengine


config配置::

    MONGODB_DB = ''
    MONGODB_HOST = ''
    MONGODB_PORT = '27017'
    MONGODB_USERNAME = ''
    MONGODB_PASSWORD = ''


默认情况下，flask-mongoengine会在实例化扩展时打开连接，但您可以将其配置为仅在第一次访问数据库时打开连接::

    MONGODB_CONNECT=False


自定义查询
 - get_or_404 ：与get类似，如果查询到没有对象返回abort(404)    
 - first_or_404: 同上。
 - paginate：数据集分页传递两个参数，page和per_page。
 - paginate_field ：在 查询中一个文档进行分页，参数：field_name，doc_id，page，per_page。



例子::

    # 404 if object doesn't exist
    def view_todo(todo_id):
        todo = Todo.objects.get_or_404(_id=todo_id)
    ..

    # Paginate through todo
    def view_todos(page=1):
        paginated_todos = Todo.objects.paginate(page=page, per_page=10)

    # Paginate through tags of todo
    def view_todo_tags(todo_id, page=1):
        todo = Todo.objects.get_or_404(_id=todo_id)
        paginated_tags = todo.paginate_field('tags', page, per_page=10)


分页对象的属性包括：iter_pages，next，prev，has_next，has_prev，next_num，prev_num。

template::

    {# Display a page of todos #}
    <ul>
    {% for todo in paginated_todos.items %}
        <li>{{ todo.title }}</li>
    {% endfor %}
    </ul>

    {# Macro for creating navigation links #}
    {% macro render_navigation(pagination, endpoint) %}
    <div class=pagination>
    {% for page in pagination.iter_pages() %}
        {% if page %}
            {% if page != pagination.page %}
                <a href="{{ url_for(endpoint, page=page) }}">{{ page }}</a>
            {% else %}
            <strong>{{ page }}</strong>
        {% endif %}
        {% else %}
            <span class=ellipsis>…</span>
        {% endif %}
    {% endfor %}
    </div>
    {% endmacro %}

    {{ render_navigation(paginated_todos, 'view_todos') }}



与WTForms的集成
------------------------------------------------------------------

flask-mongoengine自动从MongoEngine模型生成WTForms::

    from flask_mongoengine.wtf import model_form

    class User(db.Document):
        email = db.StringField(required=True)
        first_name = db.StringField(max_length=50)
        last_name = db.StringField(max_length=50)

    class Content(db.EmbeddedDocument):
        text = db.StringField()
        lang = db.StringField(max_length=3)

    class Post(db.Document):
        title = db.StringField(max_length=120, required=True, validators=[validators.InputRequired(message=u'Missing title.'),])
        author = db.ReferenceField(User)
        tags = db.ListField(db.StringField(max_length=30))
        content = db.EmbeddedDocumentField(Content)

    PostForm = model_form(Post)

    def add_post(request):
        form = PostForm(request.POST)
        if request.method == 'POST' and form.validate():
            # do something
            redirect('done')
        return render_template('add_post.html', form=form)

如果不是隐式转换，则允许提示用户参数::        

    PostForm = model_form(Post, field_args={'title': {'textarea': True}})

支持的参数:

choices:
 - multiple to use a SelectMultipleField
 - radio to use a RadioField

StringField:
 - password to use a PasswordField
 - textarea to use a TextAreaField


默认情况下，没有设置max_length时，StringField才会转换为TextAreaField。

支持的字段:
  - StringField
  - BinaryField
  - URLField
  - EmailField
  - IntField
  - FloatField
  - DecimalField
  - BooleanField
  - DateTimeField
  - ListField(使用wtforms.fields.FieldList)
  - SortedListField(重复ListField)
  - EmbeddedDocumentField(使用wtforms.fields.FormField并生成内联表单)
  - ReferenceField(使用带有从QuerySet或Document加载的选项的wtforms.fields.SelectFieldBase)
  - DictField

目前不支持的类型:
 - ObjectIdField
 - GeoLocationField
 - GenericReferenceField


Session 会话
------------------------------------------------------------------

要使用MongoEngine作为会话存储，只需配置会话接口::

    from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

    app = Flask(__name__)
    db = MongoEngine(app)
    app.session_interface = MongoEngineSessionInterface(db)

Flask-DebugToolbar::

    from flask import Flask
    from flask_debugtoolbar import DebugToolbarExtension

    app = Flask(__name__)
    db = MongoEngine(app)
    toolbar = DebugToolbarExtension(app)

    #config.py：
    DEBUG_TB_PANELS = 'flask_mongoengine.panels.MongoDebugPanel'



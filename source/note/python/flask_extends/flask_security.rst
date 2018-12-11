Flask-Security官方中文翻译
=======================================================================

添加安全机制，包括：
 - 会话认证
 - 角色管理
 - 哈希密码
 - 基于http身份认证
 - 基于令牌身份认证
 - 基于令牌账号激活[可选]
 - 基于令牌的密码重置[可选]
 - 用户注册[可选]
 - 登陆跟踪[可选]
 - JSON/Ajax支持

通过集成flask的插件可以实现这些功能：
 - Flask-Login
 - Flask-Mail
 - Flask-Principal
 - Flask-WTF
 - itsdangerous
 - passlib

Flask-Security支持以下用于数据持久性的Flask扩展：
 - Flask-SQLAlchemy
 - Flask-MongoEngine
 - Flask-Peewee
 - PonyORM

配置
---------------------------------------------------------------------


.. list-table:: 核心配置
   :header-rows: 1

   * - SECURITY_BLUEPRINT_NAME
     - 指定flask-security蓝图名称
   * - SECURITY_CLI_USERS_NAME
     - 指定管理用户的命令名称。通过设置禁用false，默认为users
   * - SECURITY_CLI_ROLES_NAME
     - 指定命令管理角色名称。通过设置禁用false，默认为roles
   * - SECURITY_URL_PREFIX
     - 指定Flask-Security蓝图的URL前缀。默认为 None。
   * - SECURITY_SUBDOMAIN
     - 指定Flask-Security蓝图的子域。默认为 None。
   * - SECURITY_FLASH_MESSAGES
     - 指定在安全过程中是否刷新消息。默认为True。
   * - SECURITY_I18N_DOMAIN
     - 指定用于翻译的域的名称。默认为flask_security。
   * - SECURITY_PASSWORD_HASH
     - 指定散列密码时要使用的密码哈希算法。生产系统推荐值bcrypt、sha512_crypt或pbkdf2_sha512。默认为 bcrypt。
   * - SECURITY_PASSWORD_SALT
     - 指定HMAC盐。仅当密码哈希类型设置为纯文本以外的其他内容时才使用此选项。默认为None。
   * - SECURITY_PASSWORD_SINGLE_HASH
     - 指定仅对密码进行一次哈希处理。默认密码经过两次哈希处理
   * - SECURITY_HASHING_SCHEMES
     - 用于创建和验证令牌的算法列表。默认为sha256_crypt。
   * - SECURITY_DEPRECATED_HASHING_SCHEMES
     - 用于创建和验证令牌的已弃用算法列表。默认为hex_md5。
   * - SECURITY_PASSWORD_HASH_OPTIONS
     - 指定要传递给散列方法的其他选项。
   * - SECURITY_EMAIL_SENDER
     - 指定发送电子邮件的电子邮件地址。MAIL_DEFAULT_SENDER如果另外使用Flask-Mail，
   * - SECURITY_TOKEN_AUTHENTICATION_KEY
     - 指定使用令牌身份验证时要读取的查询字符串参数。默认为auth_token。
   * - SECURITY_TOKEN_AUTHENTICATION_HEADER
     - 指定使用令牌身份验证时要读取的HTTP标头。默认为 Authentication-Token
   * - SECURITY_TOKEN_MAX_AGE
     - 指定身份验证令牌到期之前的秒数。默认为None，表示令牌永不过期。
   * - SECURITY_DEFAULT_HTTP_AUTH_REALM
     - 使用基本HTTP身份验证时指定默认身份验证领域。默认为Login Required


.. list-table:: URL和视图
   :header-rows: 1

   * - SECURITY_LOGIN_URL
     - 指定登录URL。默认为/login。
   * - SECURITY_LOGOUT_URL
     - 指定注销URL。默认为 /logout。
   * - SECURITY_REGISTER_URL
     - 指定注册URL。默认为 /register。
   * - SECURITY_RESET_URL
     - 指定密码重置URL。默认为 /reset。
   * - SECURITY_CHANGE_URL
     - 指定密码更改URL。默认为 /change。
   * - SECURITY_CONFIRM_URL
     - 指定电子邮件确认URL。默认为/confirm。
   * - SECURITY_POST_LOGIN_VIEW
     - 指定用户登录后重定向到的默认视图。此值可以设置为URL或端点名称。默认为/。
   * - SECURITY_POST_LOGOUT_VIEW
     - 指定用户注销后重定向到的默认视图。此值可以设置为URL或端点名称。默认为/。
   * - SECURITY_CONFIRM_ERROR_VIEW
     - 如果发生确认错误，则指定要重定向到的视图。此值可以设置为URL或端点名称。如果此值为 None，
   * - SECURITY_POST_REGISTER_VIEW
     - 指定在用户成功注册后重定向到的视图。此值可以设置为URL或端点名称。
   * - SECURITY_POST_CONFIRM_VIEW
     - 指定用户成功确认其电子邮件后要重定向到的视图。此值可以设置为URL或端点名称。
   * - SECURITY_POST_RESET_VIEW
     - 指定用户成功重置密码后要重定向到的视图。此值可以设置为URL或端点名称。
   * - SECURITY_POST_CHANGE_VIEW
     - 指定用户成功更改密码后要重定向到的视图。此值可以设置为URL或端点名称。
   * - SECURITY_UNAUTHORIZED_VIEW
     - 如果用户尝试访问他们无权访问的URL /端点，则指定要重定向到的视图。

.. list-table:: 模板路径
   :header-rows: 1

   * - SECURITY_FORGOT_PASSWORD_TEMPLATE
     - 指定忘记密码页面的模板路径。默认为 security/forgot_password.html。
   * - SECURITY_LOGIN_USER_TEMPLATE
     - 指定用户登录页面的模板路径。默认为 security/login_user.html。
   * - SECURITY_REGISTER_USER_TEMPLATE
     - 指定用户注册页面的模板路径。默认为 security/register_user.html。
   * - SECURITY_RESET_PASSWORD_TEMPLATE
     - 指定重置密码页面的模板路径。默认为 security/reset_password.html。
   * - SECURITY_CHANGE_PASSWORD_TEMPLATE
     - 指定更改密码页面的模板路径。默认为 security/change_password.html。
   * - SECURITY_SEND_CONFIRMATION_TEMPLATE
     - 指定重新发送确认说明页面的模板路径。默认为 security/send_confirmation.html。
   * - SECURITY_SEND_LOGIN_TEMPLATE
     - 指定无密码登录的发送登录说明页面模板的路径。默认为 security/send_login.html。

.. list-table:: 功能标志
   :header-rows: 1

   * - SECURITY_CONFIRMABLE
     - 指定在注册新帐户时是否要求用户确认其电子邮件地址。如果此值为True，Flask-Security会创建一个端点来处理确认和请求以重新发送确认指令。此端点的URL由SECURITY_CONFIRM_URL配置选项指定。默认为False。
   * - SECURITY_REGISTERABLE
     - 指定Flask-Security是否应创建用户注册端点。此端点的URL由SECURITY_REGISTER_URL 配置选项指定。默认为False。
   * - SECURITY_RECOVERABLE
     - 指定Flask-Security是否应创建密码重置/恢复端点。此端点的URL由SECURITY_RESET_URL配置选项指定。默认为False。
   * - SECURITY_TRACKABLE
     - 指定Flask-Security是否应跟踪基本用户登录统计信息。如果设置为True，请确保您的模型具有必需的字段/属性。如果您使用代理，请务必使用ProxyFix。默认为 False
   * - SECURITY_PASSWORDLESS
     - 指定Flask-Security是否应启用无密码登录功能。如果设置为True，则用户无需输入密码进行登录，但会收到带有登录链接的电子邮件。此功能是实验性的，应谨慎使用。默认为False。
   * - SECURITY_CHANGEABLE
     - 指定Flask-Security是否应启用更改密码端点。此端点的URL由SECURITY_CHANGE_URL配置选项指定。默认为False。

.. list-table:: Email
   :header-rows: 1

   * - SECURITY_EMAIL_SUBJECT_REGISTER
     - 设置确认电子邮件的主题。默认为Welcome
   * - SECURITY_EMAIL_SUBJECT_PASSWORDLESS
     - 设置无密码功能的主题。
   * - SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE
     - 设置密码通知的主题。
   * - SECURITY_EMAIL_SUBJECT_PASSWORD_RESET
     - 设置密码重置电子邮件的主题。
   * - SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE
     - 设置密码更改通知的主题。
   * - SECURITY_EMAIL_SUBJECT_CONFIRM
     - 设置电子邮件确认消息的主题。
   * - SECURITY_EMAIL_PLAINTEXT
     - 使用*.txt模板以纯文本形式发送电子邮件 。默认为True。
   * - SECURITY_EMAIL_HTML
     - 使用*.html模板将电子邮件发送为HTML 。默认为True。

.. list-table:: 其他选项
   :header-rows: 1

   * - SECURITY_USER_IDENTITY_ATTRIBUTES
     - 指定用户对象的哪些属性可用于登录。默认为['email']。
   * - SECURITY_SEND_REGISTER_EMAIL
     - 指定是否发送注册电子邮件。默认为 True。
   * - SECURITY_SEND_PASSWORD_CHANGE_EMAIL
     - 指定是否发送密码更改电子邮件。默认为 True。
   * - SECURITY_SEND_PASSWORD_RESET_EMAIL
     - 指定是否发送密码重置电子邮件。默认为 True。
   * - SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL
     - 指定是否发送密码重置通知电子邮件。默认为 True。
   * - SECURITY_CONFIRM_EMAIL_WITHIN
     - 指定用户在确认链接到期之前的时间量。始终将此值的时间单位复数。默认为5天。
   * - SECURITY_RESET_PASSWORD_WITHIN
     - 指定用户在密码重置链接到期之前的时间量。始终将此值的时间单位复数。默认为5天
   * - SECURITY_LOGIN_WITHIN
     - 指定用户在登录链接到期之前的时间量。仅在启用无密码登录功能时使用。始终将此值的时间单位复数。默认为1天
   * - SECURITY_LOGIN_WITHOUT_CONFIRMATION
     - 指定用户是否可以在将值SECURITY_CONFIRMABLE设置为 确认其电子邮件之前登录 True。默认为False。
   * - SECURITY_CONFIRM_SALT
     - 生成确认链接/令牌时指定salt值。默认为 confirm-salt。
   * - SECURITY_RESET_SALT
     - 生成密码重置链接/令牌时指定salt值。默认为 reset-salt。
   * - SECURITY_LOGIN_SALT
     - 生成登录链接/令牌时指定salt值。默认为login-salt。
   * - SECURITY_REMEMBER_SALT
     - 生成记忆标记时指定salt值。请记住使用令牌代替用户ID，因为它更安全。默认为 remember-salt。
   * - SECURITY_DEFAULT_REMEMBER_ME
     - 指定登录用户时使用的默认“记住我”值。默认为False。
   * - SECURITY_DATETIME_FACTORY
     - 指定默认的datetime工厂。默认为 datetime.datetime.utcnow。


消息

可以在中找到默认消息和错误级别core.py：
 - SECURITY_MSG_ALREADY_CONFIRMED
 - SECURITY_MSG_CONFIRMATION_EXPIRED
 - SECURITY_MSG_CONFIRMATION_REQUEST
 - SECURITY_MSG_CONFIRMATION_REQUIRED
 - SECURITY_MSG_CONFIRM_REGISTRATION
 - SECURITY_MSG_DISABLED_ACCOUNT
 - SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED
 - SECURITY_MSG_EMAIL_CONFIRMED
 - SECURITY_MSG_EMAIL_NOT_PROVIDED
 - SECURITY_MSG_FORGOT_PASSWORD
 - SECURITY_MSG_INVALID_CONFIRMATION_TOKEN
 - SECURITY_MSG_INVALID_EMAIL_ADDRESS
 - SECURITY_MSG_INVALID_LOGIN_TOKEN
 - SECURITY_MSG_INVALID_PASSWORD
 - SECURITY_MSG_INVALID_REDIRECT
 - SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN
 - SECURITY_MSG_LOGIN
 - SECURITY_MSG_LOGIN_EMAIL_SENT
 - SECURITY_MSG_LOGIN_EXPIRED
 - SECURITY_MSG_PASSWORDLESS_LOGIN_SUCCESSFUL
 - SECURITY_MSG_PASSWORD_CHANGE
 - SECURITY_MSG_PASSWORD_INVALID_LENGTH
 - SECURITY_MSG_PASSWORD_IS_THE_SAME
 - SECURITY_MSG_PASSWORD_MISMATCH
 - SECURITY_MSG_PASSWORD_NOT_PROVIDED
 - SECURITY_MSG_PASSWORD_NOT_SET
 - SECURITY_MSG_PASSWORD_RESET
 - SECURITY_MSG_PASSWORD_RESET_EXPIRED
 - SECURITY_MSG_PASSWORD_RESET_REQUEST
 - SECURITY_MSG_REFRESH
 - SECURITY_MSG_RETYPE_PASSWORD_MISMATCH
 - SECURITY_MSG_UNAUTHORIZED
 - SECURITY_MSG_USER_DOES_NOT_EXIST


快速入门
---------------------------------------------------------------------



安装依赖::
	
	#sqlalchemy
	pip install flask-security flask-sqlalchemy
	#flask-mongoengine
	pip install flask-security flask-mongoengine
	#flask-peewee
	pip install flask-security flask-peewee

基于sqlalchemy程序
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sqlalchemy程序::

	from flask import Flask, render_template
	from flask_sqlalchemy import SQLAlchemy
	from flask_security import Security, SQLAlchemyUserDatastore, \
	    UserMixin, RoleMixin, login_required

	# Create app
	app = Flask(__name__)
	app.config['DEBUG'] = True
	app.config['SECRET_KEY'] = 'super-secret'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

	# Create database connection object
	db = SQLAlchemy(app)

	# Define models
	roles_users = db.Table('roles_users',
	        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

	class Role(db.Model, RoleMixin):
	    id = db.Column(db.Integer(), primary_key=True)
	    name = db.Column(db.String(80), unique=True)
	    description = db.Column(db.String(255))

	class User(db.Model, UserMixin):
	    id = db.Column(db.Integer, primary_key=True)
	    email = db.Column(db.String(255), unique=True)
	    password = db.Column(db.String(255))
	    active = db.Column(db.Boolean())
	    confirmed_at = db.Column(db.DateTime())
	    roles = db.relationship('Role', secondary=roles_users,
	                            backref=db.backref('users', lazy='dynamic'))

	# Setup Flask-Security
	user_datastore = SQLAlchemyUserDatastore(db, User, Role)
	security = Security(app, user_datastore)

	# Create a user to test with
	@app.before_first_request
	def create_user():
	    db.create_all()
	    user_datastore.create_user(email='matt@nobien.net', password='password')
	    db.session.commit()

	# Views
	@app.route('/')
	@login_required
	def home():
	    return render_template('index.html')

	if __name__ == '__main__':
	    app.run()


SESSION的SQLAlchemy程序
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

app.py::

	from flask import Flask
	from flask_security import Security, login_required, \
	     SQLAlchemySessionUserDatastore
	from database import db_session, init_db
	from models import User, Role

	# Create app
	app = Flask(__name__)
	app.config['DEBUG'] = True
	app.config['SECRET_KEY'] = 'super-secret'

	# Setup Flask-Security
	user_datastore = SQLAlchemySessionUserDatastore(db_session,
	                                                User, Role)
	security = Security(app, user_datastore)

	# Create a user to test with
	@app.before_first_request
	def create_user():
	    init_db()
	    user_datastore.create_user(email='matt@nobien.net', password='password')
	    db_session.commit()

	# Views
	@app.route('/')
	@login_required
	def home():
	    return render('Here you go!')

	if __name__ == '__main__':
	    app.run()

databases.py::

	from sqlalchemy import create_engine
	from sqlalchemy.orm import scoped_session, sessionmaker
	from sqlalchemy.ext.declarative import declarative_base

	engine = create_engine('sqlite:////tmp/test.db', \
	                       convert_unicode=True)
	db_session = scoped_session(sessionmaker(autocommit=False,
	                                         autoflush=False,
	                                         bind=engine))
	Base = declarative_base()
	Base.query = db_session.query_property()

	def init_db():
	    # import all modules here that might define models so that
	    # they will be registered properly on the metadata.  Otherwise
	    # you will have to import them first before calling init_db()
	    import models
	    Base.metadata.create_all(bind=engine)

models.py::

	from database import Base
	from flask_security import UserMixin, RoleMixin
	from sqlalchemy import create_engine
	from sqlalchemy.orm import relationship, backref
	from sqlalchemy import Boolean, DateTime, Column, Integer, \
	                       String, ForeignKey

	class RolesUsers(Base):
	    __tablename__ = 'roles_users'
	    id = Column(Integer(), primary_key=True)
	    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
	    role_id = Column('role_id', Integer(), ForeignKey('role.id'))

	class Role(Base, RoleMixin):
	    __tablename__ = 'role'
	    id = Column(Integer(), primary_key=True)
	    name = Column(String(80), unique=True)
	    description = Column(String(255))

	class User(Base, UserMixin):
	    __tablename__ = 'user'
	    id = Column(Integer, primary_key=True)
	    email = Column(String(255), unique=True)
	    username = Column(String(255))
	    password = Column(String(255))
	    last_login_at = Column(DateTime())
	    current_login_at = Column(DateTime())
	    last_login_ip = Column(String(100))
	    current_login_ip = Column(String(100))
	    login_count = Column(Integer)
	    active = Column(Boolean())
	    confirmed_at = Column(DateTime())
	    roles = relationship('Role', secondary='roles_users',
	                         backref=backref('users', lazy='dynamic'))


基本的MongoEngine程序
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

core.py::

	from flask import Flask, render_template
	from flask_mongoengine import MongoEngine
	from flask_security import Security, MongoEngineUserDatastore, \
	    UserMixin, RoleMixin, login_required

	# Create app
	app = Flask(__name__)
	app.config['DEBUG'] = True
	app.config['SECRET_KEY'] = 'super-secret'

	# MongoDB Config
	app.config['MONGODB_DB'] = 'mydatabase'
	app.config['MONGODB_HOST'] = 'localhost'
	app.config['MONGODB_PORT'] = 27017

	# Create database connection object
	db = MongoEngine(app)

	class Role(db.Document, RoleMixin):
	    name = db.StringField(max_length=80, unique=True)
	    description = db.StringField(max_length=255)

	class User(db.Document, UserMixin):
	    email = db.StringField(max_length=255)
	    password = db.StringField(max_length=255)
	    active = db.BooleanField(default=True)
	    confirmed_at = db.DateTimeField()
	    roles = db.ListField(db.ReferenceField(Role), default=[])

	# Setup Flask-Security
	user_datastore = MongoEngineUserDatastore(db, User, Role)
	security = Security(app, user_datastore)

	# Create a user to test with
	@app.before_first_request
	def create_user():
	    user_datastore.create_user(email='matt@nobien.net', password='password')

	# Views
	@app.route('/')
	@login_required
	def home():
	    return render_template('index.html')

	if __name__ == '__main__':
	    app.run()


基本的Peewee程序
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Peewee 程序::

	from flask import Flask, render_template
	from flask_peewee.db import Database
	from peewee import *
	from flask_security import Security, PeeweeUserDatastore, \
	    UserMixin, RoleMixin, login_required

	# Create app
	app = Flask(__name__)
	app.config['DEBUG'] = True
	app.config['SECRET_KEY'] = 'super-secret'
	app.config['DATABASE'] = {
	    'name': 'example.db',
	    'engine': 'peewee.SqliteDatabase',
	}

	# Create database connection object
	db = Database(app)

	class Role(db.Model, RoleMixin):
	    name = CharField(unique=True)
	    description = TextField(null=True)

	class User(db.Model, UserMixin):
	    email = TextField()
	    password = TextField()
	    active = BooleanField(default=True)
	    confirmed_at = DateTimeField(null=True)

	class UserRoles(db.Model):
	    # Because peewee does not come with built-in many-to-many
	    # relationships, we need this intermediary class to link
	    # user to roles.
	    user = ForeignKeyField(User, related_name='roles')
	    role = ForeignKeyField(Role, related_name='users')
	    name = property(lambda self: self.role.name)
	    description = property(lambda self: self.role.description)

	# Setup Flask-Security
	user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
	security = Security(app, user_datastore)

	# Create a user to test with
	@app.before_first_request
	def create_user():
	    for Model in (Role, User, UserRoles):
	        Model.drop_table(fail_silently=True)
	        Model.create_table(fail_silently=True)
	    user_datastore.create_user(email='matt@nobien.net', password='password')

	# Views
	@app.route('/')
	@login_required
	def home():
	    return render_template('index.html')

	if __name__ == '__main__':
	    app.run()


邮件配置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

	# At top of file
	from flask_mail import Mail

	# After 'Create app'
	app.config['MAIL_SERVER'] = 'smtp.example.com'
	app.config['MAIL_PORT'] = 465
	app.config['MAIL_USE_SSL'] = True
	app.config['MAIL_USERNAME'] = 'username'
	app.config['MAIL_PASSWORD'] = 'password'
	mail = Mail(app)

Proxy代理配置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

	# At top of file
	from werkzeug.config.fixers import ProxyFix

	# After 'Create app'
	app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)


数据库模型
---------------------------------------------------------------------

插件需要最少字段：

用户表：
 - id
 - email
 - password
 - active

角色表：
 - id
 - name
 - description

附加功能：
	根据应用程序的配置，可能需要其他字段添加到用户模型中。

Confirmable：
	如果启用用户确认，SECURITY_CONFIRMABLE的值设置为true，则需要在user模型中添加如下字段:
	 - confirmed_at

Trackable:
	如果通过将应用程序的SECURITY_TRACKABLE 配置值设置为True来启用用户跟踪，则用户模型将需要以下附加字段：
	 - last_login_at
	 - current_login_at
	 - last_login_ip
	 - current_login_ip
	 - login_count 

自定义用户内容
---------------------------------------------------------------------

::

	class User(db.Model, UserMixin):
		id = db.Column(db.Integer, primary_key=True)
		email = TextField()
		password = TextField()
		active = BooleanField(default=True)
		confirmed_at = DateTimeField(null=True)
		name = db.Column(db.String(80))

		# Custom User Payload
		def get_security_payload(self):
			return {
				'id': self.id,
				'name': self.name,
				'email': self.email
			}


自定义视图页面
---------------------------------------------------------------------

视图views:
 - security/forgot_password.html
 - security/login_user.html
 - security/register_user.html
 - security/reset_password.html
 - security/change_password.html
 - security/send_confirmation.html
 - security/send_login.html

操作：
 1. 创建security文件夹
 2. 覆盖一样文件名的html文件

上下文处理器::

	security = Security(app, user_datastore)

	# This processor is added to all templates
	@security.context_processor
	def security_context_processor():
	    return dict(hello="world")

	# This processor is added to only the register view
	@security.register_context_processor
	def security_register_processor():
	    return dict(something="else")

以下是所有可用的上下文处理器装饰器的列表：
 - context_processor：所有观点
 - forgot_password_context_processor：忘记密码查看
 - login_context_processor：登录视图
 - register_context_processor：注册视图
 - reset_password_context_processor：重置密码视图
 - change_password_context_processor：更改密码视图
 - send_confirmation_context_processor：发送确认视图
 - send_login_context_processor：发送登录视图

表单
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

	from flask_security.forms import RegisterForm

	class ExtendedRegisterForm(RegisterForm):
	    first_name = StringField('First Name', [Required()])
	    last_name = StringField('Last Name', [Required()])

	security = Security(app, user_datastore,
	         register_form=ExtendedRegisterForm)

::

	class User(db.Model, UserMixin):
	    id = db.Column(db.Integer, primary_key=True)
	    email = db.Column(db.String(255), unique=True)
	    password = db.Column(db.String(255))
	    first_name = db.Column(db.String(255))
	    last_name = db.Column(db.String(255))

表单重写：
 - login_form: Login form
 - confirm_register_form: Confirmable register form
 - register_form: Register form
 - forgot_password_form: Forgot password form
 - reset_password_form: Reset password form
 - change_password_form: Change password form
 - send_confirmation_form: Send confirmation form
 - passwordless_login_form: Passwordless login form

电子邮件模板重写：
 - security/email/confirmation_instructions.html
 - security/email/confirmation_instructions.txt
 - security/email/login_instructions.html
 - security/email/login_instructions.txt
 - security/email/reset_instructions.html
 - security/email/reset_instructions.txt
 - security/email/reset_notice.html
 - security/email/change_notice.txt
 - security/email/change_notice.html
 - security/email/reset_notice.txt
 - security/email/welcome.html
 - security/email/welcome.txt

重写步骤：
	1. 创建security文件夹
	2. 创建email文件夹
	3. 覆盖相同的模板名称

上下文::

	security = Security(app, user_datastore)

	# This processor is added to all emails
	@security.mail_context_processor
	def security_mail_processor():
	    return dict(hello="world")

异步发送::

	# Setup the task
	@celery.task
	def send_security_email(msg):
	    # Use the Flask-Mail extension instance to send the incoming ``msg`` parameter
	    # which is an instance of `flask_mail.Message`
	    mail.send(msg)

	@security.send_mail_task
	def delay_security_email(msg):
	    send_security_email.delay(msg)


init_app 方式发送::

	from flask import Flask
	from flask_mail import Mail
	from flask_security import Security, SQLAlchemyUserDatastore
	from celery import Celery

	mail = Mail()
	security = Security()
	celery = Celery()

	def create_app(config):
	    """Initialize Flask instance."""

	    app = Flask(__name__)
	    app.config.from_object(config)

	    @celery.task
	    def send_flask_mail(msg):
	        mail.send(msg)

	    mail.init_app(app)
	    datastore = SQLAlchemyUserDatastore(db, User, Role)
	    security_ctx = security.init_app(app, datastore)

	    # Flexible way for defining custom mail sending task.
	    @security_ctx.send_mail_task
	    def delay_flask_security_mail(msg):
	        send_flask_mail.delay(msg)

	    # A shortcurt.
	    security_ctx.send_mail_task(send_flask_mail.delay)

	    return app

Celery::

	@celery.task
	def send_flask_mail(**kwargs):
	        mail.send(Message(**kwargs))

	@security_ctx.send_mail_task
	def delay_flask_security_mail(msg):
	    send_flask_mail.delay(subject=msg.subject, sender=msg.sender,
	                          recipients=msg.recipients, body=msg.body,
	                          html=msg.html)







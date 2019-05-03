第五章：数据库
========================================

**数据库这块是很重要的，多敲遇到问题就搜错误信息一般都能查到解决方案**

** 2019-04-23 映射已存在的表**

参考：
 - https://blog.csdn.net/weixin_40238625/article/details/88177492
 - https://blog.lazybee.me/sqlalchemy-demo/
 - https://blog.csdn.net/weixin_38570967/article/details/83211799

数据库按照一定规则保存程序数据,程序再发起查询取回所需的数据。Web 程序最常用基 于关系模型的数据库,这种数据库也称为 SQL 数据库,因为它们使用结构化查询语言。不 过最近几年文档数据库和键值对数据库成了流行的替代选择,这两种数据库合称 NoSQL 数据库。

SQL数据库
---------------

关系型数据库把数据存储在表中,表模拟程序中不同的实体。例如,订单管理程序的数据
库中可能有表 customers、products 和 orders。

表的列数是固定的,行数是可变的。列定义表所表示的实体的数据属性。例如,customers
表中可能有 name、address、phone 等列。表中的行定义各列对应的真实数据。

表中有个特殊的列,称为主键,其值为表中各行的唯一标识符。表中还可以有称为外键的 列,引用同一个表或不同表中某行的主键。行之间的这种联系称为关系,这是关系型数据 库模型的基础。


NoSQL数据库
---------------

所有不遵循上节所述的关系模型的数据库统称为 NoSQL 数据库。NoSQL 数据库一般使用 集合代替表,使用文档代替记录。NoSQL 数据库采用的设计方式使联结变得困难,所以大 多数数据库根本不支持这种操作。对于结构如图 5-1 所示的 NoSQL 数据库,若要列出各 用户及其角色,就需要在程序中执行联结操作,即先读取每个用户的 role_id,再在 roles 表中搜索对应的记录。

使用SQL还是NoSQL
---------------------

SQL 数据库擅于用高效且紧凑的形式存储结构化数据。这种数据库需要花费大量精力保证
数据的一致性。NoSQL 数据库放宽了对这种一致性的要求,从而获得性能上的优势。 对不同类型数据库的全面分析、对比超出了本书范畴。对中小型程序来说,SQL 和 NoSQL
数据库都是很好的选择,而且性能相当。

Python数据库框架
-------------------------

大多数的数据库引擎都有对应的 Python 包,包括开源包和商业包。Flask 并不限制你使 用何种类型的数据库包,因此可以根据自己的喜好选择使用 MySQL、Postgres、SQLite、 Redis、MongoDB 或者 CouchDB。

如果这些都无法满足需求,还有一些数据库抽象层代码包供选择,例如 SQLAlchemy 和 MongoEngine。你可以使用这些抽象包直接处理高等级的 Python 对象,而不用处理如表、 文档或查询语言此类的数据库实体。

FLask集成度选择框架时,你不一定非得选择已经集成了 Flask 的框架,但选择这些框架可以节省 你编写集成代码的时间。使用集成了 Flask 的框架可以简化配置和操作,所以专门为 Flask 开发的扩展是你的首选。

基于以上因素,本书选择使用的数据库框架是 Flask-SQLAlchemy(http://pythonhosted.org/ Flask-SQLAlchemy/),这个 Flask 扩展包装了 SQLAlchemy(http://www.sqlalchemy.org/)框架。

使用Flask-SQLAlchemy管理数据库
-------------------------------------

安装::

    (venv) $ pip install flask-sqlalchemy

在 Flask-SQLAlchemy 中,数据库使用 URL 指定。最流行的数据库引擎采用的数据库 URL 格式如表 5-1 所示。

 - MySQL | mysql://username:password@hostname/database
 - Postgres | postgresql://username:password@hostname/database
 - SQLite(Unix) | sqlite:////absolute/path/to/database
 - SQLite(Windows) | sqlite:///c:/absolute/path/to/database
   
在这些 URL 中,hostname 表示 MySQL 服务所在的主机,可以是本地主机(localhost), 也可以是远程服务器。数据库服务器上可以托管多个数据库,因此 database 表示要使用的 数据库名。

程序使用的数据库 URL 必须保存到 Flask 配置对象的 SQLALCHEMY_DATABASE_URI 键中。配 置对象中还有一个很有用的选项,即 SQLALCHEMY_COMMIT_ON_TEARDOWN 键,将其设为 True 时,每次请求结束后都会自动提交数据库中的变动。其他配置选项的作用请参阅 Flask- SQLAlchemy 的文档。

 .. literalinclude:: code/code5-1.py
    :language: python

db 对象是 SQLAlchemy 类的实例,表示程序使用的数据库,同时还获得了 Flask-SQLAlchemy提供的所有功能。


定义模型
------------------

模型这个术语表示程序使用的持久化实体。在 ORM 中,模型一般是一个 Python 类,类中
的属性对应数据库表中的列。

Flask-SQLAlchemy 创建的数据库实例为模型提供了一个基类以及一系列辅助类和辅助函 数,可用于定义模型的结构。

 .. literalinclude:: code/code5-2.py
    :language: python

类变量 __tablename__ 定义在数据库中使用的表名。如果没有定义 __tablename__,Flask-SQLAlchemy会使用一个默认名字,但默认的表名没有遵守使用复数形式进行命名的约定, 所以最好由我们自己来指定表名。其余的类变量都是该模型的属性,被定义为 db.Column 类的实例。

db.Column 类构造函数的第一个参数是数据库列和模型属性的类型。

最常用的SQLAlchemy列类型:

 - 类型名   Python类型   说明
 - Integer int 普通整数,一般是 32 位
 - SmallInteger int 取值范围小的整数,一般是 16 位
 - BigInteger int 或 long
 - Float float 浮点数
 - Numeric decimal.Decimal 定点数
 - String str 变长字符串
 - Text str 变长字符串,对较长或不限长度的字符串做了优化
 - Unicode unicode  变长 Unicode 字符串
 - UnicodeText unicode 变长 Unicode 字符串,对较长或不限长度的字符串做了优化
 - Boolean bool 布尔值
 - Date datetime.date 日期
 - Time datetime.time 时间
 - DateTime datetime.datetime 日期和时间
 - Interval datetime.timedelta  时间间隔
 - Enum str 一组字符串
 - PickleType 任何Python对象 自动使用Pickle序列化
 - LargeBinary str 二进制文件

db.Column 中其余的参数指定属性的配置选项。

 - primary_key 如果设为 True,这列就是表的主键
 - unique 如果设为 True,这列不允许出现重复的值
 - index 如果设为 True,为这列创建索引,提升查询效率
 - nullable 如果设为 True,这列允许使用空值;如果设为 False,这列不允许使用空值
 - default 为这列定义默认值


虽然没有强制要求,但这两个模型都定义了 __repr()__ 方法,返回一个具有可读性的字符 串表示模型,可在调试和测试时使用。

关系
---------

关系型数据库使用关系把不同表中的行联系起来。图 5-1 所示的关系图表示用户和角色之 间的一种简单关系。这是角色到用户的一对多关系,因为一个角色可属于多个用户,而每 个用户都只能有一个角色。

 .. literalinclude:: code/code5-3.py
    :language: python

关系使用 users 表中的外键连接了两行。添加到 User 模型中的 role_id 列 被定义为外键,就是这个外键建立起了关系。传给 db.ForeignKey() 的参数 'roles.id' 表 明,这列的值是 roles 表中行的 id 值。

添加到 Role 模型中的 users 属性代表这个关系的面向对象视角。对于一个 Role 类的实例, 其 users 属性将返回与角色相关联的用户组成的列表。db.relationship() 的第一个参数表 明这个关系的另一端是哪个模型。如果模型类尚未定义,可使用字符串形式指定。

db.relationship() 中的 backref 参数向 User 模型中添加一个 role 属性,从而定义反向关 系。这一属性可替代 role_id 访问 Role 模型,此时获取的是模型对象,而不是外键的值。

大多数情况下,db.relationship() 都能自行找到关系中的外键,但有时却无法决定把 哪一列作为外键。例如,如果 User 模型中有两个或以上的列定义为 Role 模型的外键, SQLAlchemy 就不知道该使用哪列。如果无法决定外键,你就要为 db.relationship() 提供 额外参数,从而确定所用外键.

常用的SQLAlchemy关系选项

 - backref 在关系的另一个模型中添加反向引用
 - primaryjoin 明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
 - lazy 指定如何加载相关记录。可选值有 select(首次访问时按需加载)、immediate(源对象加载后就加载)、joined(加载记录,但使用联结)、subquery(立即加载,但使用子查询),noload(永不加载)和 dynamic(不加载记录,但提供加载记录的查询)
 - uselist 如果设为 Fales,不使用列表,而使用标量值
 - order_by 指定关系中记录的排序方式
 - secondary 指定多对多关系中关系表的名字
 - secondaryjoin SQLAlchemy 无法自行决定时,指定多对多关系中的二级联结条件

**其实要很熟这个关系选项，不然多对多的时候非常报错**

一对一关系可以用前面介绍的一对多关系 表示,但调用 db.relationship() 时要把 **uselist 设为 False**
,把“多”变成“一”。多对 一关系也可使用一对多表示,对调两个表即可,或者把外键和 db.relationship() 都放在“多”这一侧。最复杂的关系类型是多对多,需要用到第三张表,这个表称为关系表

数据库操作
-----------------

创建表
^^^^^^^^^^^^^^^
首先,我们要让 Flask-SQLAlchemy 根据模型类创建数据库。方法是使用 db.create_all() 函数::

    (venv) $ python hello.py shell
    >>> from hello import db
    >>> db.create_all()

如果你查看程序目录,会发现新建了一个名为 data.sqlite 的文件。这个 SQLite 数据库文件 的名字就是在配置中指定的。如果数据库表已经存在于数据库中,那么 db.create_all() 不会重新创建或者更新这个表。如果修改模型后要把改动应用到现有的数据库中,这一特 性会带来不便。更新现有数据库表的粗暴方式是先删除旧表再重新创建:

::
    
    >>> db.drop_all()
    >>> db.create_all()

遗憾的是,这个方法有个我们不想看到的副作用,它把数据库中原有的数据都销毁了。本 章末尾将会介绍一种更好的方式用于更新数据库。

**博主使用mysql，就算本地测试也一样。因为使用sqlite时多对多报错 换成mysql就没事了**

插入行
-----------

::

    >>> admin_role = Role(name='Admin')
    >>> mod_role = Role(name='Moderator')
    >>> user_role = Role(name='User')
    >>> user_john = User(username='john', role=admin_role)
    >>> user_susan = User(username='susan', role=user_role)
    >>> user_david = User(username='david', role=user_role)
    >>> print(admin_role.id)
    None
    >>> print(mod_role.id)
    None
    >>> print(user_role.id)
    None
    >>> db.session.add(admin_role)
    >>> db.session.add(mod_role)
    >>> db.session.add(user_role)
    >>> db.session.add(user_john)
    >>> db.session.add(user_susan)
    >>> db.session.add(user_david)

or或者简写成::

    db.session.add_all([admin_role, mod_role, user_role,user_john, user_susan, user_david])

为了把对象写入数据库,我们要调用 commit() 方法提交会话::

    >>> db.session.commit()

修改行::

    >>> admin_role.name = 'Administrator'
    >>> db.session.add(admin_role)
    >>> db.session.commit()

删除行::

    >>> db.session.delete(mod_role)
    >>> db.session.commit()

查询行::

    Role.query.all()
    User.query.all()
    >>> User.query.filter_by(role=user_role).all()


**若要查看 SQLAlchemy 为查询生成的原生 SQL 查询语句,只需把 query 对象转换成字符串**::

    str(User.query.filter_by(role=user_role))

条件查询::

    user_role = Role.query.filter_by(name='User').first()


完整的列表参见 SQLAlchemy 文档(http://docs.sqlalchemy.org)。

常用的SQLAlchemy查询过滤器

 - filter()   把过滤器添加到原查询上,返回一个新查询
 - filter_by()   把等值过滤器添加到原查询上,返回一个新查询
 - limit()  使用指定的值限制原查询返回的结果数量,返回一个新查询
 - offset()  偏移原查询返回的结果,返回一个新查询
 - order_by() 根据指定条件对原查询结果进行排序,返回一个新查询
 - group_by() 根据指定条件对原查询结果进行分组,返回一个新查询

 在查询上应用指定的过滤器后,通过调用 all() 执行查询,以列表的形式返回结果。除了 all() 之外,还有其他方法能触发查询执行。

最常使用的SQLAlchemy查询执行函数

 - all() 以列表形式返回查询的所有结果
 - first() 返回查询的第一个结果,如果没有结果,则返回 None
 - first_or_404() 返回查询的第一个结果,如果没有结果,则终止请求,返回 404 错误响应
 - get() 返回指定主键对应的行,如果没有对应的行,则返回 None
 - get_or_404() 返回指定主键对应的行,如果没找到指定的主键,则终止请求,返回 404 错误响应 count() 返回查询结果的数量
 - paginate() 返回一个 Paginate 对象,它包含指定范围内的结果

**数据库这块是很重要的，多敲遇到问题就搜错误信息一般都能查到解决方案**

在视图函数中操作数据库
----------------------------

 .. literalinclude:: code/code5-5.py
    :language: python

在这个修改后的版本中,提交表单后,程序会使用 filter_by() 查询过滤器在数据库中查 找提交的名字。变量 known 被写入用户会话中,因此重定向之后,可以把数据传给模板, 用来显示自定义的欢迎消息。注意,要想让程序正常运行,你必须按照前面介绍的方法, 在 Python shell 中创建数据库表。


集成Python shell
------------------------

每次启动 shell 会话都要导入数据库实例和模型,这真是份枯燥的工作。为了避免一直重复
导入,我们可以做些配置,让 Flask-Script 的 shell 命令自动导入特定的对象。

::
    
    from flask.ext.script import Shell
    def make_shell_context():
        return dict(app=app, db=db, User=User, Role=Role)
    manager.add_command("shell", Shell(make_context=make_shell_context))

    $ python hello.py shell
    >>> app
    <Flask 'app'>
    >>> db
    <SQLAlchemy engine='sqlite:////home/flask/flasky/data.sqlite'> 
    >>> User
    <class 'app.User'>

使用Flask-Migrate实现数据库迁移
-------------------------------------------

在开发程序的过程中,你会发现有时需要修改数据库模型,而且修改之后还需要更新数据库。

仅当数据库表不存在时,Flask-SQLAlchemy 才会根据模型进行创建。因此,更新表的唯一 方式就是先删除旧表,不过这样做会丢失数据库中的所有数据。

SQLAlchemy 的主力开发人员编写了一个迁移框架,称为 Alembic(https://alembic.readthedocs.org/en/latest/index.html)。除了直接使用 Alembic 之外,Flask 程序还可使用 Flask-Migrate (http://flask-migrate.readthedocs.org/en/latest/)扩展。这个扩展对 Alembic 做了轻量级包装,并集成到 Flask-Script 中,所有操作都通过 Flask-Script 命令完成。


创建迁移仓库
----------------

::

    (venv) $ pip install flask-migrate


::

    from flask.ext.migrate import Migrate, MigrateCommand 
    # ...
    migrate = Migrate(app, db)
    manager.add_command('db', MigrateCommand)

::

    (venv) $ python hello.py db init

创建迁移脚本::

    python hello.py db migrate -m "initial migration"

or::

    python hello.py db migrate 


更新数据库::

    (venv) $ python hello.py db upgrade


**数据库的设计和使用是很重要的话题,甚至有整本的书对其进行介绍。你应该把本章视作 一个概览,更高级的话题会在后续各章中讨论。**


.. include:: ../../../ad.rst
第五章、数据库
=======================================================================

5.1 数据库的分类
---------------------------------------------------------------------

SQL
NoSQL

5.2 ORM魔法
---------------------------------------------------------------------

略

5.3 使用Flask-SQLalchemy管理数据库
---------------------------------------------------------------------

常用的字段类型：
 - Integer ： 整型
 - String ： 字符串
 - Text ：较长的Unicode文本
 - Date ： 日期  datetime.date对象
 - Time ： 时间 datetime.time对象
 - Date Time ：时间日期 datetime对象
 - Interval ：时间坚哥 datetime.timedelta对象
 - Float ：浮点型
 - Boolean ：布尔值
 - PickleType ：pickle列化
 - LargeBinary ：任意二进制数据

常用的字段参数：
 - primary_key ： 主键
 - unique ： 唯一
 - index  ：索引
 - nullable ：默认true 是否为空
 - default ：默认值 


5.4 数据库操作
---------------------------------------------------------------------

查询方法：
 - all() : 返回包含所有查询记录的列表
 - first() ： 返回查询的第一条记录，如果未找到返回none
 - one() ： 返回第一条记录 如果大于或者小于1则报错
 - get(ident) ： 传入主键id作为参数返回记录 如果未找到返回none
 - count() ： 返回查询结果的数量
 - one_or_none() ： 类似one() 瑞国结果不为1 返回none
 - first_or_404() ： 返回查询的第一条记录如果为找到返回404 错误相应
 - get_or_404() ： 返回主键记录  如果为找到返回404错误响应
 - pagginate() ：返回pagination对象 可以对记录进行分页处理
 - with_parent(instance) ： 传入模型类示例作为参数 返回和这个示例相关联的对象。

过滤方法:
 - filter() : 使用指定的规则过滤记录 返回新产生的查询对象
 - filter_by() ：使用指定规则过滤记录，以关键字表达式的形式，返回新产生的查询对象
 - order_by() ： 根据指定条件对记录进行排序，返回新产生的查询对象
 - limit() ： 使用指定的值限制原查询返回的记录数量返回新产生的查询对象
 - group_by() ： 根据指定条件对记录进行分组，返回新产生的查询对象
 - offset() ： 使用指定的值便宜原查询的结果，返回新产生的查询对象。

 这里具体以后会逐个添加示例  

5.5 定义关系
---------------------------------------------------------------------

关系函数参数：
 - back_populates :定义反向索引  用于简历双向关系，在关系的另一侧也必须显示定义关系属性
 - backref ： 添加反向引用，自动在另一侧简历关系属性，是back_populates的简化版
 - lazy ： 指定如何加载相关记录
 - uselist ： 指定是否使用列表的实行加载记录，设为false则使用标量
 - cascade ： 设置级联操作
 - order_by ： 指定加载相关记录时的排序方式
 - secondary ： 在多对多关系中指定关联表
 - primaryjoin ： 指定多对多关系中的以及连接条件
 - secondaryjoin ： 指定多对多关系中的二级连接条件

关系记录加载方式(lazy参数可选值)：
 - select ： 在必要时一次性加载记录 返回默认几率的列表   同等于 lazy=True
 - joined ： 和父查询一样加载几率，但使用联结 同等于 lazy=False
 - immediate ： 一旦父查询加载就加载
 - subquery ： 类似于joined 不过将使用子查询
 - dynamic ： 不直接加载记录，而是返回一个包含相关记录的query对象，一遍再继续附加查询函数对结果进行过滤。

5.6 更新数据库表
---------------------------------------------------------------------

::

    db.drop_all()
    db.create_all()

5.7 数据进阶实践
---------------------------------------------------------------------
cascade 级联操作

sqlalchemy 提供了一个listen_for()装饰器用来注册事件回调。

事件监听     
 - SQLAlchemy core事件
 - SQLAlchemy ORM事件



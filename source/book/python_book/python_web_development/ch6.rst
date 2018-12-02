第六章：网站架构
=======================================================================

常见的WSGI容器

gunicorn：豆瓣广泛使用。

uWSGI：这个也有很多人用。

nginx做转发端口。

缓存：

memcached：介绍略

书中这里介绍了简单的Redis的操作

也举例了几个例子：
    1. 取最新N个数据的操作
    2. 取Top操作(排行榜应用)
    3. 实时统计

具体代码请看：https://github.com/dongweiming/web_develop/tree/master/chapter6

分片和集群管理：
    1. Twemproxy
    2. Redis Cluster
    3. Coids


Nosql：略

书中后面都是简单文字性介绍了一下内容：
    1. 高可用方案
    2. 分片方案
    3. 缓存
    4. 均衡负载
    5. 群集

以上内容都是简单文件描述，没有实际意义。




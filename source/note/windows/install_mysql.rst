安装mysql5.7遇到的坑 
====================================================================



2018-10-27 
安装mysql8.0遇到了挺多的坑，比如安装完毕navcat无法连接，原因是连接加密了。在安装过程中选中了其中一项需要校验密码，总是错误，另外一项又是无法连接，只要安装回5.7。发现没有弹框配置，只好手动配置。


原链接是这里:

https://blog.csdn.net/bingoxubin/article/details/78490483?utm_source=blogxgwz0


::

    ##以下二选一
    # mysqld --initialize-insecure #这个方法初始化完后，root用户无密码
    # mysqld --initialize --console #这个方法初始化完后，root用户有密码。密码是console中输出的一段字符串（记住该字符串）

    ##安装服务
    mysqld --install

    删除mysql服务 sc delete mysql
    开启mysql服务 net start mysql
    停止mysql服务 net stop mysql



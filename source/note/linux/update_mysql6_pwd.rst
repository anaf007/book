修改mysql密码
====================================================================


filename:update_mysql6_pwd.rst

::

    vim /etc/my.cnf

    在[mysqld]字段中加上这句话

    skip-grant-tables

    :wq!保存

    重启服务：

    service mysqld restart

    进入mysql：

    mysqld -u root

    选择数据库

    use mysql

    更新密码
    UPDATE user SET Password = password ('your_pwd') WHERE User = 'root'; 

    flush privileges ; 

    quit

    删除skip-grant-tables

    service mysqld restart

    ok
    


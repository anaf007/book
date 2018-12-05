centos6下安装mysql5.6(转)
====================================================================

filename:centos6_install_mysql5_6.rst

原文连接：https://blog.csdn.net/dwyane__wade/article/details/81082153

::

    # 检查系统是否安装其他版本的MYSQL数据，有则卸载

    yum list installed | grep mysql
    yum -y remove mysql-libs.x86_64

    # 安装及配置

    wget http://repo.mysql.com/mysql-community-release-el6-5.noarch.rpm

    rpm -ivh mysql-community-release-el6-5.noarch.rpm
    yum repolist all | grep mysql

    # 安装MYSQL数据库

    yum install mysql-community-server -y

    # 设置为开机启动
    chkconfig --list | grep mysqld
    chkconfig mysqld on

    # 启动

    service mysqld start

    # 设置密码
    /usr/bin/mysqladmin -u root password '123456'

    # 如果上一步执行失败
    mysql -uroot -proot尝试


    允许远程登录：

    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'your_pwd' WITH GRANT OPTION;















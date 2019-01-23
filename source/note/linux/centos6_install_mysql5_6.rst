centos6下安装mysql56/57(转)
====================================================================

filename:centos6_install_mysql5_6.rst

原文连接：https://blog.csdn.net/dwyane__wade/article/details/81082153

::
    
    #查看系统版本：
    cat /etc/issue 

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

    flush privileges;

    #备注 这里设置了也访问不了  可能是防火墙打开  
    service iptables stop


参考文章：https://blog.csdn.net/shuaigexiaobo/article/details/78190168



安装mysql5.7
---------------------------------------------------------------------

原文：https://www.cnblogs.com/lzj0218/p/5724446.html

1.检测系统是否已经安装过mysql或其依赖，若已装过要先将其删除，否则第4步使用yum安装时会报错：


::

    yum list installed | grep mysql
    #删除
    yum -y remove mysql-libs.x86_64

    wget dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm --no-check-certificate

    yum install mysql-community-release-el6-5.noarch.rpm

    ls /etc/yum.repos.d

    yum repolist enabled | grep mysql
    #这里下载了300M+的文件
    yum install mysql-community-server

    service mysqld start












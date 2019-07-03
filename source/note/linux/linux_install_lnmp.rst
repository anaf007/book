centos下LNMP的安装
=======================================================================

1.关闭防火墙: chkconfig iptables off

2.关闭selinux ::

    vi /etc/sysconfig/selinux 
    //将SELINUX=enforcing修改为disabled然后重启生效

3、配置CentOS 6.0 第三方yum源（CentOS默认的标准源里没有nginx软件包）::

    yum install wget
    wget http://www.atomicorp.com/installers/atomic
    sh ./atomic
    yum check-update

    #  163源  centos7
    参考：https://blog.csdn.net/qq_18831583/article/details/79146759
    #  cd /etc/yum.repos.d
    #  mv ./CentOS-Base.repo ./CentOS-Base-repo.bak
    #  wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
    #  yum clean all
    #  mv CentOS7-Base-163.repo CentOS-Base.repo
    #  yum makecache
    #  


4.安装开发包和库文件::

     yum -y install ntp make openssl openssl-devel pcre pcre-devel libpng libpng-devel libjpeg-6b libjpeg-devel-6b freetype freetype-devel gd gd-devel zlib zlib-devel  gcc gcc-c++ libXpm libXpm-devel ncurses ncurses-devel libmcrypt libmcrypt-devel libxml2  libxml2-devel imake autoconf automake screen sysstat compat-libstdc++-33 curl curl-devel


5.卸载已安装的apache、mysql、php::

    yum remove httpd
    yum remove mysql
    yum remove php

6.安装nginx::

    yum install nginx
    service nginx start
    //设2、3、5级别开机启动
    chkconfig --levels 235 nginx on    

7.安装mysql::

    yum install mysql mysql-server mysql-devel
    service mysqld start
    chkconfig --levels 235 mysqld on
    //为root用户设置密码
    mysqladmin -u root password "pwd"
    service mysqld restart
    //创建数据库
    create database example DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    use example;


8.安装php::


    ####
    安装php 更新了 下面的是安装php5.4的   
    需要安装5.6以上的 参照连接： 
    https://www.cnblogs.com/shione/p/7492735.html
    
    //安装php和所需组件使PHP支持MySQL、FastCGI模式
    yum install php lighttpd-fastcgi php-cli php-mysql php-gd php-imap php-ldap php-odbc php-pear php-xml php-xmlrpc php-mbstring php-mcrypt php-mssql php-snmp php-soap php-tidy php-common php-devel php-fpm
    service php-fpm start
    chkconfig --levels 235 php-fpm on

9.配置nginx支持php::
    
    //由于原配置文件要自己去写因此可以使用默认的配置文件作为配置文件
    //将配置文件改为备份文件
    mv /etc/nginx/nginx.conf /etc/nginx/nginx.confbak
    cp /etc/nginx/nginx.conf.default /etc/nginx/nginx.conf
    //自己的配置文件在conf.d/default.conf文件
    vi /etc/nginx/nginx.conf
    index index.php index.html index.htm;
    //将以上代码注释去掉，并修改成nginx默认路径
    location ~ \.php$ {
        root           /usr/share/nginx/html;
        root           /home/www/html;
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  /usr/share/nginx/html$fastcgi_script_name;
        fastcgi_param  SCRIPT_FILENAME   /home/www/html$fastcgi_script_name;
        include        fastcgi_params;
    }

10.配置php ::

    //编辑文件php.ini，在文件末尾添加cgi.fix_pathinfo = 1
    vi /etc/php.ini

11.重启nginx php-fpm::

    service nginx restart
    service php-fpm restart


12.建立info.php文件::

    vi /usr/share/nginx/html/info.php
    <?php
       phpinfo();
    ?>

13.测试nginx是否解析php ::
    
    输入：192.168.1.105/info.php
    显示php界面说明解析成功


14绑定域名::

    /etc/nginx/conf.d/default.conf 是配置文件
    /etc/nginx/conf.d/virtual.conf 配置虚拟主机

    按照格式 添加：

    server {
    listen 80;
    server_name z1013.anaf.cn;
        location ~ \.php$ {
            root /usr/www/z1013;
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_index index.php;
            fastcgi_param SCRIPT_FILENAME /usr/www/z1013$fastcgi_script_name;
            include fastcgi_params;
        }
        location / {
            root /usr/www/z1013;
            index index.html index.htm index.php;
        }
    }

    #静态文件
    server {
        listen 80;
        server_name work.anaf.cn;
        index index.html; 
        location / {
            root   /home/www/my_work/build/html; 
            index  index.html index.htm;
        }

    }



额外  部署SSL  启用HTTPS：  

去申请免费证书 得到  pem  key两个证书文件  

nginx配置::

    server{
        listen 443 ssl;
        server_name anhy.net;
        root /home/www/anhy_net;

        ssl_session_cache shared:SSL:1m;
        ssl_certificate "/home/www/anhy_net/2170589_anhy.net.pem";
        ssl_certificate_key "/home/www/anhy_net/2170589_anhy.net.key";
        ssl_session_timeout  10m;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;
        location / {
            proxy_pass http://192.168.6.11;
        } 
    }


刷新配置 ``nginx -t`` ``nginx -s reload``

证书自签： https://www.howtoing.com/how-to-create-a-self-signed-ssl-certificate-for-nginx-on-centos-7

步骤：

1. 安装Nginx及调整防火墙

::

    yum install epel-release
    yum install nginx
    systemctl start nginx

    systemctl status nginx

    sudo firewall-cmd --add-service=http
    sudo firewall-cmd --add-service=https
    sudo firewall-cmd --runtime-to-permanent

    sudo iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT
    sudo iptables -I INPUT -p tcp -m tcp --dport 443 -j ACCEPT


2. 创建ssl证书

创建对应的目录

::

    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt

    需要先 yum  install  OpenSSL

    OpenSSL的 ：这是用于创建和管理OpenSSL的证书，密钥和其他文件的基本命令行工具。
    REQ：此子命令指定我们要使用X.509证书签名请求（CSR）的管理。 “X.509”是SSL和TLS遵循的用于其密钥和证书管理的公钥基础结构标准。我们要创建一个新的X.509证书，所以我们使用这个子命令。
    -x509：这进一步告诉我们要进行的，而不是生成一个证书签名请求的自签名证书的工具修改以前的子命令，因为通常会发生。
    -nodes：这告诉OpenSSL的跳到使用密码保护我们的证书的选项。我们需要Nginx能够在服务器启动时读取文件，无需用户干预。口令将防止这种情况发生，因为我们必须在每次重新启动后输入。
    -days 365：此选项设置的证书将被视为有效的时间长度。我们在这里设置了一年。
    -newkey RSA：2048：指定我们要生成新的证书，并在同一时间一个新的密钥。 我们没有创建在上一步中签署证书所需的密钥，因此我们需要与证书一起创建。 在rsa:2048部分告诉它做的RSA密钥是2048位。
    -keyout：这行告诉OpenSSL的在什么地方，我们正在创建的生成私钥文件。
    -out ：这告诉OpenSSL的在什么地方，我们正在创建的证书。
    


    openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048

3. 配置SSL证书   就是使用 宝塔的脚本   复制 car  pem的内容就可以了

4. 重载 nginx   




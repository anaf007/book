linux查找软件(nginx)安装位置及配置信息等
====================================================================

::

    ps -ef | grep nginx 


    find / -name httpd.conf

    httpd -V

    #拼接就是路径了



安装nginx::

    rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm

    yum info nginx

    yum install nginx

    service nginx start


永久关闭防火墙::

     chkconfig iptables off


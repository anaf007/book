centos下LAMP的安装
=======================================================================


参考文章：https://segmentfault.com/a/1190000013129679

域名绑定：https://blog.csdn.net/qq_21956483/article/details/52602708


::

	<VirtualHost *:80>
	    DocumentRoot "/var/www/html/oa/backend/MeeshineOA/MeeshineOA"  
	    ServerName hoa.com   
	    <Directory "/var/www/html/oa/backend/MeeshineOA/MeeshineOA">  
	        Allow from All  
	        AllowOverride None
	    </Directory>  
	</VirtualHost>



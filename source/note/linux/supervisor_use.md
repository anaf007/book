supervisor的使用
==============================================

参考：
* https://blog.csdn.net/cnctcom/article/details/70688815
* https://blog.csdn.net/DongGeGe214/article/details/80264811
* https://blog.csdn.net/fwhezfwhez/article/details/80841578
* https://blog.csdn.net/qq_40771567/article/details/80064657
* https://blog.csdn.net/xin_101/article/details/82798726
* https://juejin.im/post/5a30f7f0f265da43346fe8b5

安装
```
不能使用yum 安装  直接使用原来的pip安装  python2下的pip安装参照升级python部分

安装pip后  直接 pip install supervisor 


```
echo_supervisord_conf > supervisor.conf # 生成 supervisor 默认配置文件

运行：  supervisord -c supervisor.conf

/home/www/fabric/venv/bin/python3 /home/www/fabric/venv/bin/gunicorn


ProtocolError: <ProtocolError for 127.0.0.1/RPC2: 401 Unauthor.


ps -ef | grep supervisord

kill id


新建flask项目的一些步骤
==============================================

项目环境：mac10.13   python365  

::

    pip install cookiecutter
    cookiecutter https://github.com/sloria/cookiecutter-flask.git
    pip install -r requirements/dev.txt
    #注意webpack，不用就删掉对应的扩展删除略

    #还要注意一下database.py的封装，外键不能为空的选项可能会报错。

    #创建虚拟环境 
    pip install virtualenv 
    python3 -m virtualenv venv
    source venv/bin/activate


    #2018-11-15和之前一样的bug
    #报错ModuleNotFoundError: No module named 'MySQLdb'
    pip install mysqlclient
    #Python: MySQLdb and “Library not loaded: libmysqlclient.16.dylib”
    #Library not loaded: libssl.1.0.0.dylib
    #_mysql.cpython-36m-darwin.so  Reason: image not found

    export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
    #设置环境变量DYLD_LIBRARY_PATH，直接在.env下添加

     


环境： centos64 

报错 ： OSError: mysql_config not found

::

    yum install mysql-devel gcc gcc-devel python-devel

    python3 -m pip install mysqlclient

    #ok




部署：

Windows+nginx  替换了 iis 环境::

    server {
        listen 81;
        server_name localhost; 

        location / {
            proxy_pass http://127.0.0.1:5678; 
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

    }

    flask run -p 5678 -h 0.0.0.0

    #之前还记得有替代gunicorn的工具  叫 pylons 而且已经部署 这次在去看 是一个web框架  可能保存错了 后面再尝试    这里展示用flask自带的 

    更改成 iis 部署 因为启动了nginx 还要启动flask  一个命令行黑乎乎的 不是很好










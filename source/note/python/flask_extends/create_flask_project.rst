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







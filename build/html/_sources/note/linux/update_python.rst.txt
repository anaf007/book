centos下升级pyhton3
====================================================================

time:2018-09-12

**缺少组件会报错需要先安装下组件**

::

    yum install -y zlib* 
    yum install -y gcc


::
    
    #切换目录
    cd /opt/
    #下载python36
    wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
    #解压
    tar -zxvf Python-3.6.0.tgz
    #进入目录
    cd Python-3.6.0

    ./configure --prefix=/usr/local/python3
    #./configure --prefix=/usr/local/python3 --enable-optimizations
    make
    make install
    /usr/local/python3/bin/python3 -V
    >>Python 3.6.0 
    #创建软连接
    ln -s /usr/local/python3/bin/python3 /usr/bin/python3
    python3 -V
    >>Python 3.6.0 
    ok




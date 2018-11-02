centos6下升级pyhton3
====================================================================

time:2018-09-12


更新时间：2018-09-24  
------------------------------------------------------------------


yum install openssl-devel


在新的服务器重新安装python3的时候   运行flask出现ModuleNotFoundError: No module named '_ssl'错误。经查  ，  需要重新安装编译python 才行。



**缺少组件会报错需要先安装下组件**

::

    yum install -y zlib* 
    yum install -y gcc


::
    
    #切换目录
    cd /opt/
    #下载python36
    #wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz

    wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz

    #解压
    tar -zxvf Python-3.6.5.tgz
    #进入目录
    cd Python-3.6.5

    #./configure --prefix=/usr/local/python3
    ./configure --prefix=/usr/local/python3 --enable-optimizations

    这里  test400+的东西 用了10+分钟

    make
    make install
    /usr/local/python3/bin/python3 -V
    >>Python 3.6.0 
    #创建软连接
    ln -s /usr/local/python3/bin/python3 /usr/bin/python3
    python3 -V
    >>Python 3.6.5
    ok




centos6下安装和使用git
====================================================================


filename:centos6_install_git.rst

::

    yum install git

    #生成ssh秘钥
    ssh-keygen -t rsa -C "anaf@163.com"

    回车3次

    打开github
    settings->SSH And GPG Keys->New SSH key

    vi /root/.ssh/id_rsa.pub

    复制到github

    然后就可以使用 git clone   xxxx了



2018-09-25操作发现github  在git clone 无法clone  

搜索git clone太慢得到的结果说这样::

    git config --global http.proxy 'socks5://127.0.0.1:1080'    

这样就可以了

还说，在hosts文件中添加,不过我没加::

    151.101.76.249 github.global.ssl.fastly.net 
    192.30.253.112 github.com


原文：https://blog.csdn.net/twang0x80/article/details/79777135

https://blog.csdn.net/github_34965845/article/details/80610060


解决pip install  xx慢 的问题

pip慢

地址 ：https://blog.csdn.net/lambert310/article/details/52412059









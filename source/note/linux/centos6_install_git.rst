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
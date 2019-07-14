git的使用
=======================================================================

git升级
---------------------------------------------------------------------

参考：https://www.cnblogs.com/zendwang/p/7089512.html

教程中少了一步::

    yum install xmlto

git在centos下的安装
---------------------------------------------------------------------

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

::

    pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple


加入.gitignore无效的解决方法
---------------------------------------------------------------------

::
    
    git rm -r --cached xxx
    git rm --cached demo-project.iml

再重新加入.gitignore文件

::
    
    git rm -r --cached .    
    git add .

    #提交版本
    git commit -m "first commit"
    #推送服务器
    git push -u origin master


window下一键push的脚本
---------------------------------------------------------------------

::

	git add .
	git commit -m "..."
	git push origin master


新建pus.bat文件::

	
	git add -A .

	set /p declation=msg:
	git commit -m "%declation%"

	echo;

	git push origin master

	echo;
	finish！
	echo;

	pause


丢到c盘Windows文件夹下  OK 每次只用 push一下就OK了


Git强制拉取远程覆盖本地仓库
---------------------------------------------------------------------

::

    git fetch --all
    git reset --hard origin/master
    git pull

    #放弃本地修改
    git reset --hard 
    git pull


拉取提示冲突错误
---------------------------------------------------------------------

::

    error: Your local changes to 'c/environ.c' would be overwritten by merge.  Aborting.
    Please, commit your changes or stash them before you can merge.


    1、先将本地修改存储起来
    git stash
    其中stash@{0}就是刚才保存的标记。

    2、pull内容
    git pull

    3、还原暂存的内容
    git stash pop stash@{0}

    4、解决文件中冲突的的部分
    其中Updated upstream 和=====之间的内容就是pull下来的内容，====和stashed changes之间的内容就是本地修改的内容。碰到这种情况，git也不知道哪行内容是需要的，所以要自行确定需要的内容。







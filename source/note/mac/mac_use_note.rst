mac使用小技巧
====================================================================

在mac上使用brew 安装软件的时候， 会更新很慢。解决办法如下：

解决方法，关闭自动更新::

    export HOMEBREW_NO_AUTO_UPDATE=true


brew慢,参考地址: https://xu3352.github.io/mac/2018/09/06/mac-homebrew-update-slowly

方法::

    # 进入brew主目录
    $ cd `brew --repo`

    # 更换镜像
    $ git remote set-url origin https://git.coding.net/homebrew/homebrew.git

    # 测试效果
    $ brew update


几个镜像地址：
 - https://git.coding.net/homebrew/homebrew.git - Coding
 - https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git - 清华
 -  https://mirrors.ustc.edu.cn/brew.git - 中科大

mac:

    /usr/local/opt/mysql@5.7/bin/mysql.server start



::

    501 11217     1   0 10:59下午 ttys001    0:00.04 /bin/sh /usr/local/Cellar/mysql@5.7/5.7.25/bin/mysqld_safe --datadir=/usr/local/var/mysql --pid-file=/usr/local/var/mysql/anafdeMacBook.local.pid
    501 11317 11217   0 10:59下午 ttys001    0:00.43 /usr/local/Cellar/mysql@5.7/5.7.25/bin/mysqld --basedir=/usr/local/Cellar/mysql@5.7/5.7.25 --datadir=/usr/local/var/mysql --plugin-dir=/usr/local/Cellar/mysql@5.7/5.7.25/lib/plugin --log-error=anafdeMacBook.local.err --pid-file=/usr/local/var/mysql/anafdeMacBook.local.pid

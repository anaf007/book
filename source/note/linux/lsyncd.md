lsyncd Linux下文件同步备份工具及Mysql主从备份
=======================================================================

原文： https://shockerli.net/post/linux-tool-lsyncd/

安装：
---------------------------------------------------------------------

```
yum -y install lsyncd

```
配置：

lsyncd 主配置文件，假设放置在/etc/lsyncd.conf:

```
settings {
    nodaemon = false,
    logfile = "/var/log/lsyncd.log",
    statusFile = "/var/log/lsyncd.status",
    inotifyMode = "CloseWrite",
    maxProcesses = 8
}
-- 可以有多个sync，各自的source，各自的target，各自的模式，互不影响。
sync {
    default.rsyncssh,
    source    = "/home/wwwroot/web1/",
    host      = "111.222.333.444",
    targetdir = "/home/wwwroot/web1/",
    -- 忽略文件路径规则，可用table也可用外部配置文件
    -- excludeFrom = "/etc/lsyncd_exclude.lst",
    exclude = {
        ".svn",
        "Runtime/**",
        "Uploads/**",
    },
    -- maxDelays = 5,
    delay = 0,
    -- init = false,
    rsync = {
        binary = "/usr/bin/rsync",
        archive = true,
        compress = true,
        verbose = true,
        _extra = {"--bwlimit=2000"},
    },
}
```


忽略规则
---------------------------------------------------------------------

需要忽略同步的文件或文件夹，excludeFrom 选项才配置该文件，exclude 类型的配置不用该配置文件。假设配置文件放在/etc/lsyncd_exclude.lst。、

```
.svn
Runtime/**
Uploads/**

```

免密登录
---------------------------------------------------------------------

1. 生成秘钥 ssh-keygen -t rsa
2. ssh-copy-id -i 远程机器  yes 然后输入密码 ok
3. ssh root@远程IP   不用再次输入密码

启动
---------------------------------------------------------------------


lsyncd -log Exec /etc/lsyncd.conf




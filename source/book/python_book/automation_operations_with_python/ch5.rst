第五章：系统批量运维管理器pexpeet详解
==============================================

pexpect可以理解成Linux下的expect的python封装。可以实现对ssh、ftp、passwd、telnet等命令进行自动化交互。

5.1、安装
------------------------------------------------------------------

::

    pip install pexpect

一个简单的ssh登录::

    import pexpect
    child = pexpect.spawn('scp foo user@example.com')
    child.expect('Password:')
    child.sendline(passwd) 

5.2、pexpect的核心组件
------------------------------------------------------------------

5.2.1、spawn类





.. include:: ../../../ad.rst

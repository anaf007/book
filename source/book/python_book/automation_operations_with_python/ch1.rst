第一章：系统基础信息模块详解
================================

1.1、系统性能信息模块psutil
------------------------------------------------------------------

psutil是一个跨平台库，能够获取系统的运行进程和系统利用率（包括CPU、内存、磁盘、网络等）

1.1.1、获取系统性能信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.CPU信息：
 - User Time 执行用户进程的时间百分比
 - System Time 执行内核进程和中断的时间百分比
 - Wait IO 由于IO等待而使CPU处于idle（空闲）状态的时间百分比
 - Idle,CPU处于idle状态的时间百分比

::

    import pustil
    pustil.cpu_times()
    pustil.cpu_times().user
    pustil.cpu_count()
    pustil.cpu_count(logical=False)#获得物理CPU个数

1.内存信息：
 - total（内存总数）
 - used (已使用的内存数)
 - free （空闲内存）
 - buffers（缓冲使用数）
 - cache（缓存使用）
 - swap （交换分区使用数）

分别使用psutil。virtaul_memory()和psutil.swap_memory()方法获取这些信息。

3.磁盘信息：
 - read_count:读IO数
 - write_count：写IO数
 - read_bytes：IO读字节数
 - write_bytes:IO写字节数
 - read_time:磁盘读数据
 - write_time:磁盘写时间
 - 利用率可使用：psutil.disk_usage()获取
 - IO信息科使用：psutil.disk_io_counters()获取

4.网络信息：
 - bytes_sent:发送字节数
 - bytes_recv:接收字节数
 - packets_sent：发送数据包数
 - packets_recv:接收数据包数

这些信息可以使用psutil.net_io_counters()获取

5.获取其他信息(开机时间、用户登录等)：
 - psutil.users()
 - psutil.boot_time()

1.1.2、系统进程管理方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

获取当前系统的进程信息，包括进程的启动时间、查看或设置CPU亲和度、内存使用率、IO信息、socket连接、线程数等。

1.进程信息

psutil.pids()获取所有PID,使用psutil.Process()接收单个进程的PID，获取进程名、路径、状态、系统资源等。

2.popen类的使用

psutil提供了popen类的作用是获取用户启动的应用程序进程信息，以便跟踪进程的运行状态。

1.2、实用的IP地址处理模块IPy
------------------------------------------------------------------

IPy模块可以很好的辅助我们完成高效的规划工作。


1.3、DNS处理模块dnspython
------------------------------------------------------------------

dnspython支出几乎所有的记录类型，可以用于查询、传输并动态更新ZONE信息。

dnspython模块提供了大量的DNS处理方法，最常用的方法是域名查询、dnspython提供了一个DNS解析类-reslover，使用它的query方法来实现域名的查询功能。

DNS域名轮询业务监控::

    #!/usr/bin/python

    import dns.resolver
    import os
    import httplib

    iplist=[]    #定义域名IP列表变量
    appdomain="www.google.com.hk"    #定义业务域名

    def get_iplist(domain=""):    #域名解析函数，解析成功IP将追加到iplist
        try:
            A = dns.resolver.query(domain, 'A')    #解析A记录类型
        except Exception,e:
            print "dns resolver error:"+str(e)
            return
        for i in A.response.answer:
            for j in i.items:
                iplist.append(j.address)    #追加到iplist
        return True

    def checkip(ip):
        checkurl=ip+":80"
        getcontent=""
        httplib.socket.setdefaulttimeout(5)    #定义http连接超时时间(5秒)
        conn=httplib.HTTPConnection(checkurl)    #创建http连接对象

        try:
            conn.request("GET", "/",headers = {"Host": appdomain})  #发起URL请求，添加host主机头
            r=conn.getresponse()
            getcontent =r.read(15)   #获取URL页面前15个字符，以便做可用性校验
        finally:
            if getcontent=="<!doctype html>":  #监控URL页的内容一般是事先定义好，比如“HTTP200”等
                print ip+" [OK]"
            else:
                print ip+" [Error]"    #此处可放告警程序，可以是邮件、短信通知

    if __name__=="__main__":
        if get_iplist(appdomain) and len(iplist)>0:    #条件：域名解析正确且至少要返回一个IP
            for ip in iplist:
                checkip(ip)
        else:
            print "dns resolver error."



.. include:: ../../../ad.rst




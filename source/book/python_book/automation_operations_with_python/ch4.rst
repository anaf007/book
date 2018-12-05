第四章：python与系统安全
==============================================

4.1、构建集中式的病毒扫描机制
------------------------------------------------------------------

clam antivirus 是一款免费而且开放源代码的防毒软件。pyClamd是python第三方库，可以让python直接使用clamAV病毒扫描守护进程clamd来实现一个高效的病毒检测功能。

描述略

4.1.2、实践：实现集中式病毒扫描
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::


    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import time
    import pyclamd
    from threading import Thread

    class Scan(Thread):

        def __init__ (self,IP,scan_type,file):
            """构造方法"""
            Thread.__init__(self)
            self.IP = IP
            self.scan_type=scan_type
            self.file = file
            self.connstr=""
            self.scanresult=""


        def run(self):
            """多进程run方法"""

            try:
                cd = pyclamd.ClamdNetworkSocket(self.IP,3310)
                if cd.ping():
                    self.connstr=self.IP+" connection [OK]"
                    cd.reload()
                    if self.scan_type=="contscan_file":
                        self.scanresult="{0}\n".format(cd.contscan_file(self.file))
                    elif self.scan_type=="multiscan_file":
                        self.scanresult="{0}\n".format(cd.multiscan_file(self.file))
                    elif self.scan_type=="scan_file":
                        self.scanresult="{0}\n".format(cd.scan_file(self.file))
                    time.sleep(1)
                else:
                    self.connstr=self.IP+" ping error,exit"
                    return
            except Exception,e:
                self.connstr=self.IP+" "+str(e)


    IPs=['192.168.1.21','192.168.1.22']
    scantype="multiscan_file"
    scanfile="/data/www"
    i=1
    threadnum=2
    scanlist = []

    for ip in IPs:

        currp = Scan(ip,scantype,scanfile)
        scanlist.append(currp)

        if i%threadnum==0 or i==len(IPs):
            for task in scanlist:
                task.start()

            for task in scanlist:
                task.join()
                print task.connstr
                print task.scanresult
            scanlist = []   
        i+=1

4.2、实现高效的端口扫描器python-nmap模块
------------------------------------------------------------------

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import sys
    import nmap

    scan_row=[]
    input_data = raw_input('Please input hosts and port: ')
    scan_row = input_data.split(" ")
    if len(scan_row)!=2:
        print "Input errors,example \"192.168.1.0/24 80,443,22\""
        sys.exit(0)
    hosts=scan_row[0]    #接收用户输入的主机
    port=scan_row[1]    #接收用户输入的端口

    try:
        nm = nmap.PortScanner()    #创建端口扫描对象
    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(0)

    try:
        nm.scan(hosts=hosts, arguments=' -v -sS -p '+port)    #调用扫描方法，参数指定扫描主机hosts，nmap扫描命令行参数arguments
    except Exception,e:
        print "Scan erro:"+str(e)
        
    for host in nm.all_hosts():    #遍历扫描主机
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))    #输出主机及主机名
        print('State : %s' % nm[host].state())    #输出主机状态，如up、down

        for proto in nm[host].all_protocols():    #遍历扫描协议，如tcp、udp
            print('----------')
            print('Protocol : %s' % proto)    #输入协议名

            lport = nm[host][proto].keys()    #获取协议的所有扫描端口
            lport.sort()    #端口列表排序
            for port in lport:    #遍历端口及输出端口与状态
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

.. include:: ../../../ad.rst



第二章：业务服务监控详解
============================

2.1、文件内存差异对比方法
------------------------------------------------------------------

本章通过difflib模块实现内存差异对比。difflib作为python标准库模块无须安装，作用是对比文件之间的差异，且支持输出可读性的html文件。

与Linuxdiff命令类似::

    #!/usr/bin/python
    import difflib

    text1 = """text1:
    This module provides classes and functions for comparing sequences.
    including HTML and context and unified diffs.
    difflib document v7.4
    add string
    """

    text1_lines = text1.splitlines()

    text2 = """text2:
    This module provides classes and functions for Comparing sequences.
    including HTML and context and unified diffs.
    difflib document v7.5"""

    text2_lines = text2.splitlines()

    d = difflib.Differ()
    diff = d.compare(text1_lines, text2_lines)
    print '\n'.join(list(diff))

生成HTML::
    
    d = difflib.HtmlDiff()
    print d.make_file(text1_lines,text2_lines)
    运行simple2.py > diff.html即可

示例：对比nginx配置文件的差异::

    #!/usr/bin/python
    import difflib
    import sys

    try:
        textfile1=sys.argv[1]
        textfile2=sys.argv[2]
    except Exception,e:
        print "Error:"+str(e)
        print "Usage: simple3.py filename1 filename2"
        sys.exit()

    def readfile(filename):
        try:
            fileHandle = open (filename, 'rb' ) 
            text=fileHandle.read().splitlines()
            fileHandle.close()
            return text
        except IOError as error:
           print('Read file Error:'+str(error))
           sys.exit()

    if textfile1=="" or textfile2=="":
        print "Usage: simple3.py filename1 filename2"
        sys.exit()


    text1_lines = readfile(textfile1) 
    text2_lines = readfile(textfile2) 

    d = difflib.HtmlDiff()
    print d.make_file(text1_lines, text2_lines)    

2.2、文件与目录差异对比方法
------------------------------------------------------------------

自带的filecmp模块就可以实现文件、目录、遍历子目录的差异对比功能。

filecmp提供了三个操作方法。分别是：cmp单文件对比、cmpfile多文件对比、dircmp目录对比。

::

    import filecmp

    a="/home/test/filecmp/dir1"
    b="/home/test/filecmp/dir2"

    dirobj=filecmp.dircmp(a,b,['test.py'])

    print "-------------------report---------------------"
    dirobj.report()
    print "-------------report_partial_closure-----------"
    dirobj.report_partial_closure()
    print "-------------report_full_closure--------------"
    dirobj.report_full_closure()

    print "left_list:"+ str(dirobj.left_list)
    print "right_list:"+ str(dirobj.right_list)
    print "common:"+ str(dirobj.common)
    print "left_only:"+ str(dirobj.left_only)
    print "right_only:"+ str(dirobj.right_only)
    print "common_dirs:"+ str(dirobj.common_dirs)
    print "common_files:"+ str(dirobj.common_files)
    print "common_funny:"+ str(dirobj.common_funny)
    print "same_file:"+ str(dirobj.same_files)
    print "diff_files:"+ str(dirobj.diff_files)
    print "funny_files:"+ str(dirobj.funny_files)


示例2、校验源于备份目录差异::

    #!/usr/bin/env python
 
    import os, sys
    import filecmp
    import re
    import shutil
    holderlist=[]
     
    def compareme(dir1, dir2):
        dircomp=filecmp.dircmp(dir1,dir2)
        only_in_one=dircomp.left_only
        diff_in_one=dircomp.diff_files
        dirpath=os.path.abspath(dir1)
        [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in only_in_one]
        [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in diff_in_one]
        if len(dircomp.common_dirs) > 0:
            for item in dircomp.common_dirs:
                compareme(os.path.abspath(os.path.join(dir1,item)), \
                os.path.abspath(os.path.join(dir2,item)))
            return holderlist

    def main():
        if len(sys.argv) > 2:
            dir1=sys.argv[1]
            dir2=sys.argv[2]
        else:
            print "Usage: ", sys.argv[0], "datadir backupdir"
            sys.exit()
     
        source_files=compareme(dir1,dir2)
        dir1=os.path.abspath(dir1)

        if not dir2.endswith('/'): dir2=dir2+'/'
        dir2=os.path.abspath(dir2)
        destination_files=[]
        createdir_bool=False

        for item in source_files:
            destination_dir=re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)
            if os.path.isdir(item):
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                    createdir_bool=True

        if createdir_bool:
            destination_files=[]
            source_files=[]
            source_files=compareme(dir1,dir2)
            for item in source_files:
                destination_dir=re.sub(dir1, dir2, item)
                destination_files.append(destination_dir)

        print "update item:"
        print source_files 

        copy_pair=zip(source_files,destination_files)
        for item in copy_pair:
            if os.path.isfile(item[0]):
                shutil.copyfile(item[0], item[1])
     
    if __name__ == '__main__':
        main()


2.3、发送电子邮件
------------------------------------------------------------------

::

    import smtplib
    import string
     
    HOST = "smtp.gmail.com"
    SUBJECT = "Test email from Python"
    TO = "test@qq.com"
    FROM = "test@gmail.com"
    text = "Python rules them all!"
    BODY = string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT ,
            "",
            text
            ), "\r\n")
    server = smtplib.SMTP()
    server.connect(HOST,"25")
    server.starttls()
    server.login("test@gmail.com","123456")
    server.sendmail(FROM, [TO], BODY)
    server.quit()

::

    #coding: utf-8
    import smtplib
    from email.mime.text import MIMEText

    HOST = "smtp.gmail.com"
    SUBJECT = u"官网流量数据报表"
    TO = "test@qq.com"
    FROM = "test@gmail.com"

    msg = MIMEText("""
        <table width="800" border="0" cellspacing="0" cellpadding="4">
          <tr>
            <td bgcolor="#CECFAD" height="20" style="font-size:14px">*官网数据  <a href="monitor.domain.com">更多>></a></td>
          </tr>
          <tr>
            <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
            1）日访问量:<font color=red>152433</font>  访问次数:23651 页面浏览量:45123 点击数:545122  数据流量:504Mb<br>
            2）状态码信息<br>
            &nbsp;&nbsp;500:105  404:3264  503:214<br>
            3）访客浏览器信息<br>
            &nbsp;&nbsp;IE:50%  firefox:10% chrome:30% other:10%<br>
            4）页面信息<br>
            &nbsp;&nbsp;/index.php 42153<br>
            &nbsp;&nbsp;/view.php 21451<br>
            &nbsp;&nbsp;/login.php 5112<br>
        </td>
          </tr>
        </table>""","html","utf-8")
    msg['Subject'] = SUBJECT
    msg['From']=FROM
    msg['To']=TO
    try:
        server = smtplib.SMTP()
        server.connect(HOST,"25")
        server.starttls()
        server.login("test@gmail.com","123456")
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        print "邮件发送成功！"
    except Exception, e:  
        print "失败："+str(e) 

::

    #coding: utf-8
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage

    HOST = "smtp.gmail.com"
    SUBJECT = u"业务性能数据报表"
    TO = "test@qq.com"
    FROM = "test@gmail.com"

    def addimg(src,imgid):
        fp = open(src, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', imgid)
        return msgImage

    msg = MIMEMultipart('related')
    msgtext = MIMEText("""
    <table width="600" border="0" cellspacing="0" cellpadding="4">
          <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
            <td colspan=2>*官网性能数据  <a href="monitor.domain.com">更多>></a></td>
          </tr>
          <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
             <img src="cid:io"></td><td>
             <img src="cid:key_hit"></td>
          </tr>
          <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
             <td>
             <img src="cid:men"></td><td>
             <img src="cid:swap"></td>
          </tr>
        </table>""","html","utf-8")
    msg.attach(msgtext)
    msg.attach(addimg("img/bytes_io.png","io"))
    msg.attach(addimg("img/myisam_key_hit.png","key_hit"))
    msg.attach(addimg("img/os_mem.png","men"))
    msg.attach(addimg("img/os_swap.png","swap"))

    msg['Subject'] = SUBJECT
    msg['From']=FROM
    msg['To']=TO
    try:
        server = smtplib.SMTP()
        server.connect(HOST,"25")
        server.starttls()
        server.login("test@gmail.com","123456")
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        print "邮件发送成功！"
    except Exception, e:  
        print "失败："+str(e) 


::

    #coding: utf-8
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage

    HOST = "smtp.gmail.com"
    SUBJECT = u"官网业务服务质量周报"
    TO = "test@qq.com"
    FROM = "test@gmail.com"

    def addimg(src,imgid):
        fp = open(src, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', imgid)
        return msgImage

    msg = MIMEMultipart('related')
    msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>","html","utf-8")
    msg.attach(msgtext)
    msg.attach(addimg("img/weekly.png","weekly"))

    attach = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")
    attach["Content-Type"] = "application/octet-stream"
    #attach["Content-Disposition"] = "attachment; filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("gb18030")
    msg.attach(attach)

    msg['Subject'] = SUBJECT
    msg['From']=FROM
    msg['To']=TO
    try:
        server = smtplib.SMTP()
        server.connect(HOST,"25")
        server.starttls()
        server.login("test@gmail.com","123456")
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        print "邮件发送成功！"
    except Exception, e:  
        print "失败："+str(e) 


2.4、探测web服务质量方法
------------------------------------------------------------------

pycurl是一个用C语言编写的python实现、支持的操作协议有：ftp、http、https、telnet等，可以理解成Linux下curl命令功能的python封装。

::

    # -*- coding: utf-8 -*-
    import os,sys
    import time
    import sys
    import pycurl

    URL="http://www.google.com.hk"
    c = pycurl.Curl()
    c.setopt(pycurl.URL, URL)
                    
    #连接超时时间,5秒
    c.setopt(pycurl.CONNECTTIMEOUT, 5)

    #下载超时时间,5秒
    c.setopt(pycurl.TIMEOUT, 5)
    c.setopt(pycurl.FORBID_REUSE, 1)
    c.setopt(pycurl.MAXREDIRS, 1)
    c.setopt(pycurl.NOPROGRESS, 1)
    c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
    indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
    c.setopt(pycurl.WRITEHEADER, indexfile)
    c.setopt(pycurl.WRITEDATA, indexfile)
    try:
        c.perform()
    except Exception,e:
        print "connecion error:"+str(e)
        indexfile.close()
        c.close()
        sys.exit()

    NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME)
    CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)
    PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME)
    STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
    TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
    HTTP_CODE =  c.getinfo(c.HTTP_CODE)
    SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)
    HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
    SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)

    print "HTTP状态码：%s" %(HTTP_CODE)
    print "DNS解析时间：%.2f ms"%(NAMELOOKUP_TIME*1000)
    print "建立连接时间：%.2f ms" %(CONNECT_TIME*1000)
    print "准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000)
    print "传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000)
    print "传输结束总时间：%.2f ms" %(TOTAL_TIME*1000)

    print "下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD)
    print "HTTP头部大小：%d byte" %(HEADER_SIZE)
    print "平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD)

    indexfile.close()
    c.close()





.. include:: ../../../ad.rst

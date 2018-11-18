第三章：定制业务质量报表详解
============================

3.1、数据报表excel操作模块wlsxWriter
------------------------------------------------------------------

::

    #coding: utf-8
    import xlsxwriter


    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('demo1.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    #bold = workbook.add_format({'bold': True})
    bold = workbook.add_format()
    bold.set_bold()

    # Write some simple text.
    worksheet.write('A1', 'Hello')

    # Text with formatting.
    worksheet.write('A2', 'World', bold)

    worksheet.write('B2', u'中文测试', bold)

    # Write some numbers, with row/column notation.
    worksheet.write(2, 0, 32)
    worksheet.write(3, 0, 35.5)
    worksheet.write(4, 0, '=SUM(A3:A4)')

    # Insert an image.
    worksheet.insert_image('B5', 'img/python-logo.png')

    workbook.close()


3.1.1、模块常用方法说明
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. workbook类

    add_workshee方法，添加一个新的工作表。

    add_format():在工作表中创建一个新的格式对象来格式化单元格。

2. worksheet类

    worksheet类代表了一个excel工作表。是最核心的一个类

3. char类

    char类实现在xlsxWriter模块中图表组件的基类，支持的图表类型包括面积、条形图、柱状图、折线图、饼图、散点图、股票和雷达等。

    ：
     - area：创建一个面积样式的图表
     - bar：创建一个条形图
     - column：创建一个柱形图
     - line：创建一个线条图
     - pie：创建一个饼图
     - scatter：创建一个散点图
     - stock：创建一个股票图
     - radar：创建一个雷达图

3.1.2、实践：定制自动化业务流量报表图
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    #coding: utf-8
    import xlsxwriter

    workbook = xlsxwriter.Workbook('chart.xlsx')
    worksheet = workbook.add_worksheet()

    chart = workbook.add_chart({'type': 'column'})

    title = [u'业务名称',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日',u'平均流量']
    buname= [u'业务官网',u'新闻中心',u'购物频道',u'体育频道',u'亲子频道']

    data = [
        [150,152,158,149,155,145,148],
        [89,88,95,93,98,100,99],
        [201,200,198,175,170,198,195],
        [75,77,78,78,74,70,79],
        [88,85,87,90,93,88,84],
    ]
    format=workbook.add_format()
    format.set_border(1)

    format_title=workbook.add_format()
    format_title.set_border(1)
    format_title.set_bg_color('#cccccc')
    format_title.set_align('center')
    format_title.set_bold()

    format_ave=workbook.add_format()
    format_ave.set_border(1)
    format_ave.set_num_format('0.00')

    worksheet.write_row('A1',title,format_title)
    worksheet.write_column('A2', buname,format)
    worksheet.write_row('B2', data[0],format)
    worksheet.write_row('B3', data[1],format)
    worksheet.write_row('B4', data[2],format)
    worksheet.write_row('B5', data[3],format)
    worksheet.write_row('B6', data[4],format)

    def chart_series(cur_row):
        worksheet.write_formula('I'+cur_row, \
         '=AVERAGE(B'+cur_row+':H'+cur_row+')',format_ave)
        chart.add_series({
            'categories': '=Sheet1!$B$1:$H$1',
            'values':     '=Sheet1!$B$'+cur_row+':$H$'+cur_row,
            'line':       {'color': 'black'},
            'name': '=Sheet1!$A$'+cur_row,
        })

    for row in range(2, 7):
        chart_series(str(row))

    #chart.set_table()
    #chart.set_style(30)
    chart.set_size({'width': 577, 'height': 287})
    chart.set_title ({'name': u'业务流量周报图表'})
    chart.set_y_axis({'name': 'Mb/s'})

    worksheet.insert_chart('A8', chart)
    workbook.close()


3.2、Python与rrdtool的结合模块
------------------------------------------------------------------

rrdtool工具最为环状数据库的存储格式， rrdtool robin是一种处理定量数据以及当前元素指针的技术。rrdtool主要用来跟踪对象的变化情况，生成这些变化的走势图。比如业务的访问流量、系统性能、磁盘利用率等趋势图，很多流行监控平台都是用到例如rrdtool。

3.2.1、rrdtool模块常用方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. create方法：创建一个后缀为rrd的rrdtool数据库。
2. update方法：存储一个新值到rrdtool数据库。
3. graph方法：根据指定的rrdtool数据库进行绘图
4. fetch方法：根据指定的rrdtool数据库进行查询

3.3.2、实践：实现网卡流量图表绘制
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

create.py::

    # -*- coding: utf-8 -*-
    #!/usr/bin/python
    import rrdtool
    import time

    cur_time=str(int(time.time()))
    rrd=rrdtool.create('Flow.rrd','--step','300','--start',cur_time,
            'DS:eth0_in:COUNTER:600:0:U',
            'DS:eth0_out:COUNTER:600:0:U',
            'RRA:AVERAGE:0.5:1:600',
        'RRA:AVERAGE:0.5:6:700',
        'RRA:AVERAGE:0.5:24:775',
        'RRA:AVERAGE:0.5:288:797',
        'RRA:MAX:0.5:1:600',
        'RRA:MAX:0.5:6:700',
        'RRA:MAX:0.5:24:775',
        'RRA:MAX:0.5:444:797',
        'RRA:MIN:0.5:1:600',
        'RRA:MIN:0.5:6:700',
        'RRA:MIN:0.5:24:775',
        'RRA:MIN:0.5:444:797')
    if rrd:
        print rrdtool.error()

update.py::

    # -*- coding: utf-8 -*-
    #!/usr/bin/python
    import rrdtool
    import time,psutil
     
    total_input_traffic = psutil.net_io_counters()[1]
    total_output_traffic = psutil.net_io_counters()[0]
    starttime=int(time.time())

    update=rrdtool.updatev('/home/test/rrdtool/Flow.rrd','%s:%s:%s' % (str(starttime),str(total_input_traffic),str(total_output_traffic)))
    print update 

graph.py::

    # -*- coding: utf-8 -*-
    #!/usr/bin/python
    import rrdtool
    import time

    title="Server network  traffic flow ("+time.strftime('%Y-%m-%d',time.localtime(time.time()))+")"
    rrdtool.graph( "Flow.png", "--start", "-1d","--vertical-label=Bytes/s","--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H",\
     "--width","650","--height","230","--title",title,
     "DEF:inoctets=Flow.rrd:eth0_in:AVERAGE",
     "DEF:outoctets=Flow.rrd:eth0_out:AVERAGE",
     "CDEF:total=inoctets,outoctets,+",
     "LINE1:total#FF8833:Total traffic",
     "AREA:inoctets#00FF00:In traffic",
     "LINE1:outoctets#0000FF:Out traffic",
     "HRULE:6144#FF0000:Alarm value\\r",
     "CDEF:inbits=inoctets,8,*",
     "CDEF:outbits=outoctets,8,*",
     "COMMENT:\\r",
     "COMMENT:\\r",
     "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
     "COMMENT:   ",
     "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps",
     "COMMENT:  ",
     "GPRINT:inbits:MIN:MIN In traffic\: %6.2lf %Sbps\\r",
     "COMMENT: ",
     "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
     "COMMENT: ",
     "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps",
     "COMMENT: ",
     "GPRINT:outbits:MIN:MIN Out traffic\: %6.2lf %Sbps\\r")

3.3、生成动态路由轨迹图scapy模块
------------------------------------------------------------------

scapy可能怼数据包进行伪造或解包，包括发送数据包、包嗅探、应答和反馈匹配等功能。可以用在处理网络扫描、路由跟踪、服务探测、单元测试等方面。


3.3.1、模块常用方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

scapy模块提供了众多网络数据包操作方法。包括发包send()、SYN/ACK扫描、嗅探、sniff()、抓包wrpcap()、TCP路由跟踪traceroute()等

3.3.2、实践：实现TCP探测目标服务路由轨迹
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    # -*- coding: utf-8 -*-
    import os,sys,time,subprocess
    import warnings,logging
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from scapy.all import traceroute
    domains = raw_input('Please input one or more IP/domain: ')
    target =  domains.split(' ')
    dport = [80]
    if len(target) >= 1 and target[0]!='':
        res,unans = traceroute(target,dport=dport,retry=-2)
        res.graph(target="> test.svg")
        time.sleep(1)
        subprocess.Popen("/usr/bin/convert test.svg test.png", shell=True)
    else:
        print "IP/domain number of errors,exit"





.. include:: ../../../ad.rst
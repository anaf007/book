定时任务框架APScheduler学习详解
====================================================================

APScheduler简介
------------------------------------------------------------------

APScheduler基于Quartz的一个Python定时任务框架，实现了Quartz的所有功能，使用起来十分方便。提供了基于日期、固定时间间隔以及crontab类型的任务，并且可以持久化任务。基于这些功能，我们可以很方便的实现一个python定时任务系统。

安装
------------------------------------------------------------------

::

    pip install apscheduler

APScheduler有四种组成部分：
------------------------------------------------------------------

触发器(trigger)包含调度逻辑，每一个作业有它自己的触发器，用于决定接下来哪一个作业会运行。除了他们自己初始配置意外，触发器完全是无状态的。

作业存储(job store)存储被调度的作业，默认的作业存储是简单地把作业保存在内存中，其他的作业存储是将作业保存在数据库中。一个作业的数据讲在保存在持久化作业存储时被序列化，并在加载时被反序列化。调度器不能分享同一个作业存储。

执行器(executor)处理作业的运行，他们通常通过在作业中提交制定的可调用对象到一个线程或者进城池来进行。当作业完成时，执行器将会通知调度器。

调度器(scheduler)是其他的组成部分。你通常在应用只有一个调度器，应用的开发者通常不会直接处理作业存储、调度器和触发器，相反，调度器提供了处理这些的合适的接口。配置作业存储和执行器可以在调度器中完成，例如添加、修改和移除作业。　

简单应用::

    import time
    from apscheduler.schedulers.blocking import BlockingScheduler

    def my_job():
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
 
    sched = BlockingScheduler()
    sched.add_job(my_job, 'interval', seconds=5)
    sched.start()
    #上面的例子表示每隔5s执行一次my_job函数，输出当前时间信息

添加作业
------------------------------------------------------------------

上面是通过add_job()来添加作业，另外还有一种方式是通过scheduled_job()修饰器来修饰函数

::

    import time
    from apscheduler.schedulers.blocking import BlockingScheduler
 
    sched = BlockingScheduler()
 
    @sched.scheduled_job('interval', seconds=5)
    def my_job():
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
 
    sched.start()

第六章：电子邮件
=========================================

这章节其实跟flask不是很大关系，主要是与flask的集成，跳过这章学习对之后也没影响

安装::

    (venv) $ pip install flask-mail

    #配置

    import os
    # ...
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com' 
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME'
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

    #初始化
    from flask.ext.mail import Mail 
    mail = Mail(app)

保存电子邮件服务器用户名和密码的两个环境变量要在环境中定义。如果你在 Linux 或 Mac OS X 中使用 bash,那么可以按照下面的方式设定这两个变量::

    (venv) $ export MAIL_USERNAME=<Gmail username>
    (venv) $ export MAIL_PASSWORD=<Gmail password>


微软 Windows 用户可按照下面的方式设定环境变量::

    (venv) $ set MAIL_USERNAME=<Gmail username>
    (venv) $ set MAIL_PASSWORD=<Gmail password>



 .. literalinclude:: code/code6-1.py
    :language: python


 .. literalinclude:: code/code6-2.py
    :language: python


异步发送电子邮件
-------------------------

 .. literalinclude:: code/code6-3.py
    :language: python


程序要发送大量电子邮件时,使 用专门发送电子邮件的作业要比给每封邮件都新建一个线程更合适。例如,我们可以把执 行 send_async_email() 函数的操作发给 Celery(http://www.celeryproject.org/)任务队列。




.. include:: ../../../ad.rst    
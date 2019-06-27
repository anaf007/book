windows下无CMD窗口静默运行
=======================================================================

无窗口化运行nginx示例：

```
REM REM是bat文件的注释类似于php的//
REM 设置不输出命令
@ECHO off
REM 设置Nginx和php-cgi的目录
SET py_home=C:/nginx-1.15.10/html/flask_thief/env/Scripts/
SET nginx_home=C:/nginx-1.15.10/
SET www_home=C:/nginx-1.15.10/html/flask_thief/

REM 输出状态
ECHO Starting Python ...
RunHiddenConsole %py_home%python.exe %www_home%run_waitress.py
REM 输出状态
ECHO Starting nginx...
REM 启动Nginx -p Nginx的根目录
RunHiddenConsole %nginx_home%nginx.exe -p %nginx_home%
```
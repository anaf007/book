第一章：安装
===================================


**flask非常小，但是,小并不意味着它比其他框架的功能少。Flask 自开发伊始就被设计为可扩展的框架, 它具有一个包含基本服务的强健核心,其他功能则可通过扩展实现。**

**Flask有两个主要依赖:路由、调试和Web服务器网关接口(Web Server Gateway Interface, WSGI)子系统由 Werkzeug(http://werkzeug.pocoo.org/)提供;模板系统由 Jinja2(http:// jinja.pocoo.org/)提供。Werkzeug 和 Jinjia2 都是由 Flask 的核心开发者开发而成。**


使用虚拟环境
---------------

- 首先需要安装python，linux和mac都自带python，Windows需要下载一个安装包安装，注意选择32/64版本。
- 安装pip。https://bootstrap.pypa.io/get-pip.py，然后运行 python get-pip.py。如果报错根据报错原因搜索一般都会有答案。

- 安装虚拟环境。pip install virtualenv 这里pip 报错一般是window没有把python的环境变量加上。然后使用 virtualenv --version 即可看到虚拟环境的版本信息。注意Linux权限 .可以使用 pip install virtualenv --user

::

	$ git clone https://github.com/miguelgrinberg/flasky.git 
	$ cd flasky
	$ git checkout 1a
	这里说 需要clone下来  如果没有安装git是报错的，可自行查阅安装git。




创建虚拟环境：
::

   	$ virtualenv venv
	New python executable in venv/bin/python2.7
	Also creating executable in venv/bin/python
	Installing setuptools............done.
	Installing pip...............done.


激活::

	source venv/bin/activate
	Windows：
	venv\Scripts\activate
	退出：
	deactivate

**之前virtualenv venv有报错过，网络原因尝试多次后就可以了**


使用pip安装Python包
---------------------------

::

	pip install flask



.. include:: ../../../ad.rst




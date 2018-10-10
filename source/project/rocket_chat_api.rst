聊天框架rockat.chat的api集成使用
====================================================================

.. Note::

    编写flask api接口，去调用rockat.chat，使项目对接rockat.chat更方便

开始项目::

    pip install cookiecutter
    cookiecutter https://github.com/sloria/cookiecutter-flask.git


虚拟环境::

    python3 -m virtualenv venv  
    source venv/bin/activate



安装rocketchat_API::

    pip install rocketchat_API

安装flask_restful::

    pip install flask-restful    

安装sphinx::

    pip install sphinx
    #创建项目
    sphinx-quickstart
    #第一 Y  第二 回车 第三 项目名  第四作者名  以下N

    #
    pip install sphinxcontrib-httpdomain

conf.py::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinxcontrib.httpdomain',
        'sphinxcontrib.autohttp.flask',
        'sphinxcontrib.autohttp.flaskqref',
    ]    

index.rst::

    Welcome to rocket_chat_api's documentation!
    ===========================================


    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       introduction

创建introduction.rst文件::

    ===================
    `myapp`
    ===================

    Oasis Flask app that handles keys requests.

    myapp.app
    ---------------------

    .. automodule:: main.api.v1.views
       :members:
       :undoc-members:   


ok



rocket_chat聊天室框架的学习使用
====================================================================

filename:rocket_chat.rst

官网https://rocket.chat

github: https://github.com/RocketChat/Rocket.Chat

::

    
    #按照官网第一步，Quick start：
    git clone https://github.com/RocketChat/Rocket.Chat.git
    #昨晚这个过程很久下载了很久，找了很多加速方案都不行
    cd Rocket.Chat

    meteor npm start

    #提示没有meteor

    #安装 meteor  macos and linux：
    #相关访问https://www.meteor.com/install
    curl https://install.meteor.com/ | sh

    #然后去node.js官网安装node.js，安装步骤略。

    #运行 meteor npm start  报错：

    fs.js:904:18: ENOENT: no such file or directory, scandir
    'packages/rocketchat-katex/node_modules/katex/dist/fonts/'
    at Object.fs.readdirSync (fs.js:904:18)
    at package.js:24:29
   
   
    => Your application has errors. Waiting for file change.

    #搜索说：更新版本，发现还是不行，仔细一看 是缺少目录
    update --release 1.3.1


    #在Rocket.Chat/packages/rocketchat-katex目录下创建对应的目录，注意权限。
    packages/rocketchat-katex/node_modules/katex/dist/fonts/

    继续报错：
    npm ERR! Failed at the Rocket.Chat@0.70.0-develop start script.
    npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
    npm WARN Local package.json exists, but node_modules missing, did you mean to install?

    #根据错误提示：
    npm install package




mac上删除卸载node::

    sudo npm uninstall npm -g 
    sudo rm -rf /usr/local/lib/node /usr/local/lib/node_modules /var/db/receipts/org.nodejs.* 
    sudo rm -rf /usr/local/include/node /Users/$USER/.npm 
    sudo rm /usr/local/bin/node 
    sudo rm /usr/local/share/man/man1/node.1 
    sudo rm /usr/local/lib/dtrace/node.d




2018-09-29重新clone一遍，未发现错误，但是卡在了node-pre-gyp install --fallback-to-build --library=static_library很久

google::

    npm install -g node-gyp

出现错误；

meteor npm install  

也提示了一堆错误；但是都是依赖包版本问题
使用npm install  xxx@^x.x.x 之后 在运行 meteor npm start 等了一段时间编译提示：

Note:you are using a pure-JavaScript implementation of bcrypt.
While this implementation will work correctly, it is known to be
approximately three times slower than the native implementation.
In order to use the native implementation instead, run
meteor npm install \--save bcrypt
in the root directory of your application.
Updating process.env.MAIL_URL
I20180929-11:26:29.269(8)? Starting Email Intercepter...
I20180929-11:26:37.295(8)? Exception in callback of async function: Error: Cannot find module '../build/Release/sharp.node'

重新来一次meteor npm start
还是不行 ，根据错误：

sudo npm install -g node-gyp


Failed at the sharp@0.20.8 install script.

meteor npm install --save bcrypt

Exception in callback of async function: Error: Cannot find module '/Volumes/mydata/www/flask_code/cookiecutter-flask/Rocket.Chat/node_modules/grpc/src/node/extension_binary/node-v57-darwin-x64-unknown/grpc_node.node'


Please make sure you are using a supported platform and node version. If you
would like to compile fibers on this machine please make sure you have setup your
build environment--
Windows + OS X instructions here: https://github.com/nodejs/node-gyp
Ubuntu users please run: `sudo apt-get install g++ build-essential`
Alpine users please run: `sudo apk add python make g++`
sh: nodejs: command not found


要安装xcode。。。

还是等假期更新系统到10.13再来吧。

2018-10-08使用mac10.10在走一次
------------------------------------------------------------------
::
    
    #这里下载很久，速度慢又重新下  好几才ok
    git clone https://github.com/RocketChat/Rocket.Chat.git
    cd Rocket.Chat
    #这里没有直接meteor npm start，
    meteor npm install --save babel-runtime
    #居然没有报错，继续  这里提示 需要python2.7  使用命令：meteor npm config set python python2.7，我默认的就是python2.7  所以略过
    meteor npm install --save bcrypt
    #也没有报错。  只是3个警告依赖不正确，
    meteor npm start
    #报错：Your application has errors. Waiting for file change.
    #如图



.. image:: /_static/errorImages/1538980616451.jpg


仔细看是目录问题 手动创建对应的目录::

    #再次运行   
    meteor npm start
    #报错，如图

.. image:: /_static/errorImages/1538981173842.jpg

日志文件

.. image:: /_static/errorImages/1538981302558.jpg
   
搜索到使用命令::

    npm install --no-cach
    再次运行    
    meteor npm start
    #登录N久之后   OK

.. image:: /_static/errorImages/1538982540948.jpg
 
提示正常运行，但打开http://localhost:3000/却无法访问

仔细想了想  原来是docker之前设置的了端口映射  ，在docker的虚拟机中关闭端口映射就好了

.. image:: /_static/images/1537937903837.jpg
           
.. image:: /_static/images/1537938271293.jpg







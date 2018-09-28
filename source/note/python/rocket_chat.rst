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











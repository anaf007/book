翻墙新工具
------------------------------------------------------------------


参考：
 - https://gitlab.com/Alvin9999/free/wikis/%E8%87%AA%E5%BB%BAv2ray%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B
 - https://www.echoteen.com/v2ray-new-webui.html
 - http://zshttp.com/1310.html
 - https://www.codercto.com/a/22204.html
 - https://mrhee.com/v2ray.html
 - https://www.4spaces.org/digitalocean-build-v2ray-0-1/  
 - https://atrandys.com/2019/1579.html  [参照了这个]
 - https://atrandys.com/2018/216.html


一键脚本： wget -N --no-check-certificate https://raw.githubusercontent.com/YLWS-4617/V2ray.Fun/master/install.sh && bash install.sh

VPS商家：
 - https://billing.virmach.com/cart.php?a=checkout An090987.  anaf@163.com 
 - k0TJw46Ct9mzUOO83w 107.172.82.146
 - x0Wos91ZJM4Ncb85Qg 107.172.207.26 

::

    yum -y install wget
    yum install zip unzip  
    wget https://install.direct/go.sh
    bash go.sh 

    #启动
    systemctl start v2ray

    ## 停止
    sudo systemctl stop v2ray

    ## 重启
    sudo systemctl restart v2ray

    #继续  
    https://www.4spaces.org/v2ray-nginx-tls-websocket/
    #加速
    https://www.4spaces.org/speed-up-your-vps-with-bbr-plus/

    ===========配置参数============ 
     地址：virmach.anaf.cn 
     端口：443 
     uuid：757b8bbc-6ced-4b6f-86e0-392abc431a0e 
     额外id：64 
     加密方式：aes-128-gcm 
     传输协议：ws 
     别名：myws 
     路径：c67b 
     底层传输：tls


    ===========配置参数============ 
     地址：virmach1.anaf.cn 
     端口：443 
     uuid：65c59714-68da-4314-8c44-128d3a86b466 
     额外id：64 
     加密方式：aes-128-gcm 
     传输协议：ws 
     别名：myws 
     路径：cccf 
     底层传输：tls 
      

 v2ray+ws+tls一键脚本（CentOS7版）:


注意：务必保证域名解析已经成功了，再使用下面的脚本安装。

打开电脑命令行，ping 你的域名，如果显示VPS的IP地址，则解析生效了。

1. 一键脚本::

    curl -O https://raw.githubusercontent.com/atrandys/v2ray-ws-tls/master/v2ray_ws_tls.sh && chmod +x v2ray_ws_tls.sh && ./v2ray_ws_tls.sh

2. 等待脚本执行，过程中会提示需要输入域名，输入解析到本VPS的域名，然后回车

3. 等待安装完成，你可以看到配置参数，客户端配置时用到。

4、安装BBR加速，指向下面命令::

    cd /usr/src && wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh" && chmod +x tcp.sh && ./tcp.sh

5、注意在弹出的安装界面首先选择1，安装BBR内核,安装过程可能时间较长,耐心等待。

6、安装完成后会提示重启VPS,输入Y，然后回车，确认重启。然后等待几分钟，再使用xshell连接vps（连接方法是点软件上打开，找到之前保存的连接，然后点连接）登陆后执行下列命令::

    cd /usr/src && ./tcp.sh

7、在弹出安装界面,输入5,然后回车，使用BBR魔改版加速，等待安装完成提示bbr启动成功即可。

1、下载v2ray客户端

v2ray各平台客户端：https://www.v2ray.com/awesome/tools.html

2、将参数对应填写到客户端

这里大概说明一下参数怎么填写：

地址：你的域名，例如google.com

端口：443

用户ID：就是一长串uuid

加密方式：aes-128-gcm

传输协议：ws

path：就填路径这个参数

底层传输：tls

3、开启上网即可

telegram交流群：https://t.me/atrandys

4、关于移动端说明

目前有小伙伴反映，这个方案下，有的客户端可用有的不可用，那么需要你在保证配置正确的情况下，多试几个客户端。

个人现在主要用justmysocks，开头推荐的那个瓦工机场，主要是省心，所以关于这个方案的移动客户端使用情况，我给不了什么参考意见。


复活被墙IP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

免费域名：https://my.freenom.com/cart.php?a=confdomains&language=english  花了6块钱在阿里云买了个xyz的域名  

使用了国外的DNS解析就行了  cloudflare.com   



主机综合地址：www.zhujiceping.com
主机综合评测等：www.freehao123.com

新加坡域名商：sg.godaddy.com

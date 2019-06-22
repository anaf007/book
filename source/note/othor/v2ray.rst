翻墙新工具
------------------------------------------------------------------


参考：
 - https://gitlab.com/Alvin9999/free/wikis/%E8%87%AA%E5%BB%BAv2ray%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B
 - https://www.echoteen.com/v2ray-new-webui.html
 - http://zshttp.com/1310.html
 - https://www.codercto.com/a/22204.html
 - https://mrhee.com/v2ray.html
 - https://www.4spaces.org/digitalocean-build-v2ray-0-1/  [参照了这个]


一键脚本： wget -N --no-check-certificate https://raw.githubusercontent.com/YLWS-4617/V2ray.Fun/master/install.sh && bash install.sh

VPS商家：
 - https://billing.virmach.com/cart.php?a=checkout An090987.  anaf@163.com fRCO63A1njwvC72Ri5 107.172.82.146

 -  lMKZIOydQn8c18489z 107.172.207.26 

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



16076 ssh prot

Your Server IP        :  107.172.82.146 
Your Server Port      :  16076 
Your Password         :  fRCO63A1njwvC72Ri5 
Your Encryption Method:  rc4-md5 
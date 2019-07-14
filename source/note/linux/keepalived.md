keepalived 高可用方案
=======================================================================

参考：

* https://www.jianshu.com/p/da26df4f7d60
* https://qizhanming.com/blog/2018/05/17/how-to-config-keepalived-on-centos-7
* https://klionsec.github.io/2017/12/23/keepalived-nginx/
* https://www.centos.bz/2012/02/nginx-keepalived-high-availability/
* http://seanlook.com/2015/05/18/nginx-keepalived-ha/


check_nginx.sh
```sh
count=0
for (( k=0; k<2; k++ ))
do
    check_code=$( curl --connect-timeout 3 -sL -w "%{http_code}\\n" http://192.168.6.40 -o /dev/null )
    if [ "$check_code" != "200" ]; then
        count=$(expr $count + 1)
        sleep 3
        continue
    else
        count=0
        break
    fi
done
if [ "$count" != "0" ]; then
#   /etc/init.d/keepalived stop
    exit 1
else
    exit 0
fi

```

主zhu_keepalived.conf：
```
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
   script_user root
   enable_script_security 
}

vrrp_script chk_nginx {
    script "/etc/keepalived/check_nginx.sh"
    interval 2
    weight -5
    fall 3  
    rise 2
}

vrrp_instance VI_1 {
    state MASTER
    interface ens192
    virtual_router_id 51
    mcast_src_ip 192.168.6.40
    priority 150
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.6.65
    }
    track_script {
       chk_nginx
    }
}



```

从keepalived.conf：
```
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
   script_user root
   enable_script_security 
}

vrrp_script chk_nginx {
    script "/etc/keepalived/check_nginx.sh"
    interval 2
    weight -5
    fall 3  
    rise 2
}

vrrp_instance VI_1 {
    state BACKUP
    interface ens192
    virtual_router_id 51
    mcast_src_ip 192.168.6.41
    priority 101
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.6.65
    }
    track_script {
       chk_nginx
    }
}


```

上面 virtual_ipaddress 会虚拟 IP地址出来 这样站点就需要多绑定这个地址才行 

同时使用 lsyncd 同步文件
docker学习[菜鸟教程]
====================================================================

基本使用
------------------------------------------------------------------


使用::
    
    #运行ubuntu:15.10 会先下载  打印一句话  
    docker run ubuntu:15.10 /bin/echo "Hello world"

    #运行centos 会先下载 打印一句话
    docker run centos /bin/echo "Hello world"


运行交互式的容器
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们通过docker的两个参数 -i -t，让docker运行的容器实现"对话"的能力    

::

    docker run -i -t centos:6.8 /bin/bash

各个参数解析：
 - -t:在新容器内指定一个伪终端或终端。
 - -i:允许你对容器内的标准输入 (STDIN) 进行交互。

这样就想一个新系统一样了

**可以通过运行exit命令或者使用CTRL+D来退出容器。**


启动容器（后台模式）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用以下命令创建一个以进程方式运行的容器::

    docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
    2b1b7a428627c51ab8810d541d759f072b4fc75487eed05812646b8534a2fe63


在输出中，我们没有看到期望的"hello world"，而是一串长字符

这个长字符串叫做容器ID，对每个容器来说都是唯一的，我们可以通过容器ID来查看对应的容器发生了什么。

首先，我们需要确认容器有在运行，可以通过 
**docker ps** 
来查看::

    docker ps

CONTAINER ID:容器ID

NAMES:自动分配的容器名称

在容器内使用docker logs命令，查看容器内的标准输出::

    docker logs 2b1b7a428627

    docker logs amazing_cori


停止容器
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们使用 docker stop 命令来停止容器::
    
    docker stop  CONTAINER ID

    docker stop NAME

    docker ps



Docker 客户端
------------------------------------------------------------------

docker 客户端非常简单 ,我们可以直接输入 docker 命令来查看到 Docker 客户端的所有命令选项::

    docker

可以通过命令 docker command --help 更深入的了解指定的 Docker 命令使用方法。

例如我们要查看 docker stats 指令的具体使用方法::

    docker stats --help



运行一个web应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

前面我们运行的容器并没有一些什么特别的用处。

接下来让我们尝试使用 docker 构建一个 web 应用程序。

我们将在docker容器中运行一个 Python Flask 应用来运行一个web应用::

    docker run -d -P training/webapp python app.py               


参数说明:
 - -d:让容器在后台运行。
 - -P:将容器内部使用的网络端口映射到我们使用的主机上。

查看 WEB 应用容器
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 docker ps 来查看我们正在运行的容器::

    docker ps

Docker 开放了 5000 端口（默认 Python Flask 端口）映射到主机端口 32769 上。

这里mac 有个小插曲  ，需要在virtualbox上设置端口转发

.. image:: /_static/images/1537937903837.jpg
           
.. image:: /_static/images/1537938271293.jpg
                    

我们也可以指定 -p 标识来绑定指定端口::

    docker run -d -p 5000:5000 training/webapp python app.py

网络端口的快捷方式
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

通过docker ps 命令可以查看到容器的端口映射，docker还提供了另一个快捷方式：docker port,使用 docker port 可以查看指定 （ID或者名字）容器的某个确定端口映射到宿主机的端口号。

上面我们创建的web应用容器ID为:7a38a1ad55c6 名字为：determined_swanson

我可以使用docker port 7a38a1ad55c6 或docker port determined_swanson来查看容器端口的映射情况::

    docker port 7a38a1ad55c6
    docker port determined_swanson

查看WEB应用程序日志
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

docker logs [ID或者名字] 可以查看容器内部的标准输出::

    docker logs 7a38a1ad55c6
    docker logs determined_swanson


-f:让 dokcer logs 像使用 tail -f 一样来输出容器内部的标准输出。

从上面，我们可以看到应用程序使用的是 5000 端口并且能够查看到应用程序的访问日志。

查看WEB应用程序容器的进程
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们还可以使用 docker top 来查看容器内部运行的进程::

    docker top determined_swanson


检查WEB应用程序
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 docker inspect 来查看Docker的底层信息。它会返回一个 JSON 文件记录着 Docker 容器的配置和状态信息::

    docker inspect determined_swanson

停止WEB应用容器
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::
    
    docker stop determined_swanson   

重启WEB应用容器
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    docker start determined_swanson                


docker ps -l 来查看正在运行的容器

移除WEB应用容器
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    docker rm determined_swanson  

删除容器时，容器必须是停止状态，否则会报如下错误


Docker 镜像使用
------------------------------------------------------------------

Docker 镜像使用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当运行容器时，使用的镜像如果在本地中不存在，docker 就会自动从 docker 镜像仓库中下载，默认是从 Docker Hub 公共镜像源下载。

 - 1、管理和使用本地 Docker 主机镜像
 - 2、创建镜像

列出镜像列表
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们可以使用 docker images 来列出本地主机上的镜像::

    docker images 

各个选项说明:
 - REPOSTITORY：表示镜像的仓库源
 - TAG：镜像的标签
 - IMAGE ID：镜像ID
 - CREATED：镜像创建时间
 - SIZE：镜像大小


同一仓库源可以有多个 TAG，代表这个仓库源的不同个版本，如ubuntu仓库源里，有15.10、14.04等多个不同的版本，我们使用 REPOSTITORY:TAG 来定义不同的镜像。

所以，我们如果要使用版本为15.10的ubuntu系统镜像来运行容器时，命令如下::

    docker run -t -i ubuntu:15.10 /bin/bash 

如果要使用版本为14.04的ubuntu系统镜像来运行容器时，命令如下::

    docker run -t -i ubuntu:14.04 /bin/bash 

获取一个新的镜像
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当我们在本地主机上使用一个不存在的镜像时 Docker 就会自动下载这个镜像。如果我们想预先下载这个镜像，我们可以使用 docker pull 命令来下载它::

    docker pull ubuntu:13.10

查找镜像
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们可以从 Docker Hub 网站来搜索镜像，Docker Hub 网址为：https://hub.docker.com/

我们也可以使用 docker search 命令来搜索镜像。比如我们需要一个httpd的镜像来作为我们的web服务。我们可以通过 docker search 命令搜索 httpd 来寻找适合我们的镜像。

::

    docker search httpd


 - NAME:镜像仓库源的名称
 - DESCRIPTION:镜像的描述
 - OFFICIAL:是否docker官方发布    

拖取镜像
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们决定使用上图中的httpd 官方版本的镜像，使用命令 docker pull 来下载镜像::

    docker pull httpd

下载完成后，我们就可以使用这个镜像了::

    docker run httpd    


创建镜像
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当我们从docker镜像仓库中下载的镜像不能满足我们的需求时，我们可以通过以下两种方式对镜像进行更改。
 - 1.从已经创建的容器中更新镜像，并且提交这个镜像
 - 2.使用 Dockerfile 指令来创建一个新的镜像

更新镜像
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

更新镜像之前，我们需要使用镜像来创建一个容器::

    docker run -t -i ubuntu:15.10 /bin/bash

在运行的容器内使用 apt-get update 命令进行更新。

在完成操作之后，输入 exit命令来退出这个容器。

此时ID为e218edb10161的容器，是按我们的需求更改的容器。我们可以通过命令 docker commit来提交容器副本。

::

    docker commit -m="has update" -a="youj" e218edb10161 
    w3cschool/ubuntu:v2
    sha256:70bf1840fd7c0d2d8ef0a42a817eb29f854c1af8f7c59fc03ac7bdee9545aff8

各个参数说明：
 - -m:提交的描述信息
 - -a:指定镜像作者
 - e218edb10161：容器ID
 - w3cschool/ubuntu:v2:指定要创建的目标镜像名


我们可以使用 docker images 命令来查看我们的新镜像 w3cschool/ubuntu:v2：

构建镜像
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们使用命令 docker build ， 从零开始来创建一个新的镜像。为此，我们需要创建一个 Dockerfile 文件，其中包含一组指令来告诉 Docker 如何构建我们的镜像。
::

    cat Dockerfile 
    FROM    centos:6.7
    MAINTAINER      Fisher "fisher@sudops.com"

    RUN     /bin/echo 'root:123456' |chpasswd
    RUN     useradd youj
    RUN     /bin/echo 'youj:123456' |chpasswd
    RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" &gt; /etc/default/local
    EXPOSE  22
    EXPOSE  80
    CMD     /usr/sbin/sshd -D

每一个指令都会在镜像上创建一个新的层，每一个指令的前缀都必须是大写的。

第一条FROM，指定使用哪个镜像源

RUN 指令告诉docker 在镜像内执行命令，安装了什么。。。

然后，我们使用 Dockerfile 文件，通过 docker build 命令来构建一个镜像。

::

    w3cschool@w3cschool:~$ docker build -t youj/centos:6.7 .
    Sending build context to Docker daemon 17.92 kB
    Step 1 : FROM centos:6.7
     ---&gt; d95b5ca17cc3
    Step 2 : MAINTAINER Fisher "fisher@sudops.com"
     ---&gt; Using cache
     ---&gt; 0c92299c6f03
    Step 3 : RUN /bin/echo 'root:123456' |chpasswd
     ---&gt; Using cache
     ---&gt; 0397ce2fbd0a
    Step 4 : RUN useradd youj
    ......

参数说明：
 - -t ：指定要创建的目标镜像名
 - . ：Dockerfile 文件所在目录，可以指定Dockerfile 的绝对路径

使用docker images 查看创建的镜像已经在列表中存在,镜像ID为860c279d2fec

我们可以使用新的镜像来创建容器

::

    docker run -t -i youj/centos:6.7  /bin/bash

设置镜像标签
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们可以使用 docker tag 命令，为镜像添加一个新的标签::
    
    docker tag 860c279d2fec youj/centos:dev

docker tag 镜像ID，这里是 860c279d2fec ,用户名称、镜像源名(repository name)和新的标签名(tag)。

使用 docker images 命令可以看到，ID为860c279d2fec的镜像多一个标签。



Docker 容器连接
------------------------------------------------------------------

Docker 容器连接
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

前面我们实现了通过网络端口来访问运行在docker容器内的服务。下面我们来实现通过端口连接到一个docker容器

网络端口映射

我们创建了一个 python 应用的容器。

::

    docker run -d -P training/webapp python app.py

另外，我们可以指定容器绑定的网络地址，比如绑定 127.0.0.1。

我们使用 -P 参数创建一个容器，使用 docker ps 来看到端口5000绑定主机端口32768。

我们也可以使用 -p 标识来指定容器端口绑定到主机端口。

两种方式的区别是:
 - -P :是容器内部端口随机映射到主机的高端口。
 - -p :是容器内部端口绑定到指定的主机端口。    

::

    docker run -d -p 5000:5000 training/webapp python app.py 

上面的例子中，默认都是绑定 tcp 端口，如果要绑定 UPD 端口，可以在端口后面加上 /udp。

::

    docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py

docker port 命令可以让我们快捷地查看端口的绑定情况::

    docker port adoring_stonebraker 5002

Docker容器连接
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

端口映射并不是唯一把 docker 连接到另一个容器的方法。

docker有一个连接系统允许将多个容器连接在一起，共享连接信息。

docker连接会创建一个父子关系，其中父容器可以看到子容器的信息。

容器命名

当我们创建一个容器的时候，docker会自动对它进行命名。另外，我们也可以使用--name标识来命名容器，例如

::

    docker run -d -P --name youj training/webapp python app.py







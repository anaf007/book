docker学习[官网]
==============================================

连接：https://docs.docker.com/get-started/

第一章、概述和开始
------------------------------------------------------------------

下载安装docker 略

查看版本::

    docker --version

    docker info

测试docker安装::

    #运行镜像测试安装是否有效
    docker run hello-world    

    #列出安装的镜像
    docker image ls

    docker container ls --all

第二章、容器
------------------------------------------------------------------

连接：https://docs.docker.com/get-started/part2/

使用定义容器Dockerfile

创建项目，进入项目创建 Dockerfile 文件::

    # Use an official Python runtime as a parent image
    FROM python:2.7-slim

    # Set the working directory to /app
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install --trusted-host pypi.python.org -r requirements.txt

    # Make port 80 available to the world outside this container
    EXPOSE 80

    # Define environment variable
    ENV NAME World

    # Run app.py when the container launches
    CMD ["python", "app.py"]

注意如上注释

同时创建如下两个文件 ：

requirements.txt::

    Flask

app.py::

    from flask import Flask
    import os
    import socket

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return html.format(name=os.getenv("NAME", "world"))

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80)

构建应用程序::

    #注意后面的点
    docker build --tag=friendlyhello .

    docker image ls



运行应用程序::

    docker run -p 4000:80 friendlyhello

    http://localhost:4000

    curl http://localhost:4000

后台运行::

    docker run -d -p 4000:80 friendlyhello

    docker container ls

停止::

    docker container stop 1fa4ab2cf395

分享镜像::

    去注册一个账号：https://hub.docker.com/

    使用ID登录

    docker login

    标记镜像

    docker tag image username/repository:tag

    #查看已经标记的镜像
    docker image ls

发布图像::

    docker push username/repository:tag

从远程存储库中拉出并运行映像::

    docker run -p 4000:80 username/repository:tag

    #如果映像在本地不可用，则Docker会从存储库中提取映像。    


第三章、服务
------------------------------------------------------------------

连接：https://docs.docker.com/get-started/part3/

运行和扩展文件 docker-compose.yml 

``docker-compose.yml`` 文件是一个YAML文件，它定义了如何Docker容器在生产中应表现。

将文件保存在任意位置。确保已将 第2部分中创建的图像推送到注册表，并通过替换 图像详细信息进行更新。.ymlusername/repo:tag

::

    version: "3"
    services:
      web:
        # replace username/repo:tag with your name and image details
        image: username/repo:tag
        deploy:
          replicas: 5
          resources:
            limits:
              cpus: "0.1"
              memory: 50M
          restart_policy:
            condition: on-failure
        ports:
          - "4000:80"
        networks:
          - webnet
    networks:
      webnet:

该docker-compose.yml文件告诉Docker执行以下操作：
 - 拉我们在步骤2中上传的图像从注册表。
 - 将该映像的5个实例作为一个被调用的服务运行web 限制每个实例使用，最多只占单个CPU核心时间的10％（这也可以是例如“1.5”表示每个核心的1和半核心），以及50MB RAM。
 - 如果一个失败，立即重启容器。
 - 将主机上的端口4000映射到web端口80。
 - 指示web容器通过称为负载平衡的网络共享端口80 webnet。（在内部，容器本身web在短暂的端口发布到 80端口。）
 - webnet使用默认设置（负载平衡的覆盖网络）定义网络。

``运行新的负载均衡应用``

::
    
    docker swarm init
    docker stack deploy

设置应用程序名称，假设：getstartedlab::

    docker stack deploy -c docker-compose.yml getstartedlab

我们的单个服务堆栈在一台主机上运行已部署映像的5个容器实例::

    docker service ls

您可以运行 ``docker stack services`` 然后运行堆栈的名称::

    docker stack services getstartedlab

值列出系统上的所有容器::

    docker container ls -q

要查看堆栈的所有任务，您可以运行 ``docker stack ps`` 您的应用程序名称::

    docker stack ps getstartedlab

扩展应用程序:

您可以通过更改 ``replicas`` 值 ``docker-compose.yml`` ，保存更改并重新运行 ``docker stack deploy`` 命令来扩展应用程序::

    docker stack deploy -c docker-compose.yml getstartedlab

重新运行 ``docker container ls -q`` 以查看已重新配置的已部署实例

将应用程序关闭docker stack rm::

    docker stack rm getstartedlab

关闭群集::

    docker swarm leave --force

第四章、群集[待添加]
------------------------------------------------------------------

第五章、堆栈[待添加]
------------------------------------------------------------------

第六章、部署应用程序[待添加]
------------------------------------------------------------------


第七章、在docker上开发
------------------------------------------------------------------






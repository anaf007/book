黄永成thinkphp3.1视频讲解笔记内容
==============================================

安装
------------------------------------------------------------------

下载3.1核心版本

复制到项目目录，同级新建index.php输入::

    <?php

        define('APP_NAME','Index');
        define('APP_PATH','./Index/');
        //define('APP_DEBUG',TRUE);

        include './ThinkPHP/ThinkPHP.php';//下载的核心版本的php文件

    ?>

配置
------------------------------------------------------------------
运行后会在目录下创建Index目录，进入目录Conf会有配置文件

实例化函数::

    function __constuct(){}

公共配置文件config.php::

    <?php
    return array(
        'DB_HOST' => '127.0.0.1',
        'DB_USER' => 'root',
        'DB_PWD' => '',
        'DB_NAME' => 'think',
        'DB_PREFIX' => 't_',
    );
    ?>
    //获取配置项
    C('DB_HOST')








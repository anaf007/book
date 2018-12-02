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

公共配置文件Conf/config.php::

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


扩展函数
---------------------------------------------------------------------

Common/common.php下定义的函数就能自动加载

如果在Common下定义其他名称的函数就要在config.php中配置::

    LOAD_EXT_FILE => 'function'; //函数名称

另外一种方法只能在前期方法里面生效::
    
    function public index(){
        load('@.function');
        //xxxx
    }
    
引入静态文件
---------------------------------------------------------------------

::

    __PUBLIC__
    //更改位置
    在配置config.php文件中修改：
    'TMPL_PAESR_STRING' => array('__PUBLIC__'=>__ROOT__.'/'.APP_NAME.'/tpl');


U函数的使用  和I函数的使用。

修改后缀：config.php::
    
    'URL_HTML_SUFFIX' => '';


post判断：IS_POST  _404()

M函数


应用分组部署及公共项独立
---------------------------------------------------------------------

修改配置文件config.php::
    
    return array(
        'APP_GROUP_LIST' => 'Index,Admin',
        'DEFAULT_GROUP' => 'Index',
    );

    //然后在Action中删掉原来的Action.php  新建Index目录在下面新建Action文件，然后在新建Admin文件里面在创建Action文件

    //然后在Conf下创建对应模块的目录就可以实现独立的模块配置访问了

    //同理Common也一样。模板也一样。

指定错误页面：修改配置文件config.php::

    'TMPL_EXCEPTION_FILE' => 'XXX/error.html'

error.html::

    <?php ecch $e['message'];?>

设置默认的I的过滤函数::

    'DEFAULT_FILTER' => 'htmlspecialchar',

F 函数用来做数据的存储，看着挺实用的，初始化存储不变的常量

验证码的使用
---------------------------------------------------------------------


框架已经帮写好了直接使用::

    public function verify(){
        import('ORG.Util.Image');
        Image::buildImageVerify(4,5,'png')
    }


后台登录验证与自动运行
---------------------------------------------------------------------

新建CommonAction.class.php::

    public function _initialize(){
        if(!isset(xxxx)){
            跳转
        }
    }

    Class IndexAction extends CommonAction{

        里面的所有function都会自动校验
    }


分页
---------------------------------------------------------------------

可以这样引用css/js::

    <css file='__PUBLIC__/style.css'>
    <js file='__PUBLIC__/style.css'>


略

独立分组
---------------------------------------------------------------------

功能和普通分组差不多，只是文件夹目录提高一层。

内容为第14章

'APP_GROUP_MODE' => 1.
'APP_GROUP_PATH' => 'app'


RBAC权限
---------------------------------------------------------------------

内容挺多的  需要看帮助手册







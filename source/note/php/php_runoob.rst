菜鸟教程的PHP教程
==============================================

macOS 使用了MxSrvs软件，相当于 Windows的wamp

语法
------------------------------------------------------------------

PHP 脚本以 <?php 开始，以 ?> 结束::

    <?php
    // PHP 代码
    ?>

PHP 文件的默认文件扩展名是 ".php"。

PHP 文件通常包含 HTML 标签和一些 PHP 脚本代码。

::

    <!DOCTYPE html> 
    <html> 
    <body> 

    <h1>My first PHP page</h1> 

    <?php 
    echo "Hello World!"; 
    ?> 

    </body> 
    </html>


浏览器输出文本的基础指令：echo 和 print。

注释::

    // 这是 PHP 单行注释

    /*
    这是 
    PHP 多行
    注释
    */

变量
------------------------------------------------------------------

::

    <?php
    $x=5;
    $y=6;
    $z=$x+$y;
    echo $z;
    ?>

PHP 变量规则：
 - 变量以 $ 符号开始，后面跟着变量的名称
 - 变量名必须以字母或者下划线字符开始
 - 变量名只能包含字母数字字符以及下划线（A-z、0-9 和 _ ）
 - 变量名不能包含空格
 - 变量名是区分大小写的（$y 和 $Y 是两个不同的变量）

PHP 是一门弱类型语言
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
在上面的实例中，我们注意到，不必向 PHP 声明该变量的数据类型。

PHP 会根据变量的值，自动把变量转换为正确的数据类型。

在强类型的编程语言中，我们必须在使用变量前先声明（定义）变量的类型和名称。

PHP 变量作用域
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

变量的作用域是脚本中变量可被引用/使用的部分。

PHP 有四种不同的变量作用域：
 - local
 - global
 - static
 - parameter

局部和全局作用域
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在所有函数外部定义的变量，拥有全局作用域。除了函数外，全局变量可以被脚本中的任何部分访问，要在一个函数中访问一个全局变量，需要使用 global 关键字。

在 PHP 函数内部声明的变量是局部变量，仅能在函数内部访问::

    <?php 
    $x=5; // 全局变量 

    function myTest() 
    { 
        $y=10; // 局部变量 
        echo "<p>测试函数内变量:<p>"; 
        echo "变量 x 为: $x"; 
        echo "<br>"; 
        echo "变量 y 为: $y"; 
    }  

    myTest(); 

    echo "<p>测试函数外变量:<p>"; 
    echo "变量 x 为: $x"; 
    echo "<br>"; 
    echo "变量 y 为: $y"; 
    ?>

PHP global 关键字
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

global 关键字用于函数内访问全局变量。

在函数内调用函数外定义的全局变量，我们需要在函数中的变量前加上 global 关键字::

    $x=5;
    $y=10;
     
    function myTest()
    {
        global $x,$y;
        $y=$x+$y;
    }
     
    myTest();
    echo $y; // 输出 15
    ?>

PHP 将所有全局变量存储在一个名为 $GLOBALS[index] 的数组中。 index 保存变量的名称。这个数组可以在函数内部访问，也可以直接用来更新全局变量。

上面的实例可以写成这样::

    <?php
    $x=5;
    $y=10;
     
    function myTest()
    {
        $GLOBALS['y']=$GLOBALS['x']+$GLOBALS['y'];
    } 
     
    myTest();
    echo $y;
    ?>

Static 作用域
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当一个函数完成时，它的所有变量通常都会被删除。然而，有时候您希望某个局部变量不要被删除。

要做到这一点，请在您第一次声明变量时使用 static 关键字::

    <?php
    function myTest()
    {
        static $x=0;
        echo $x;
        $x++;
    }
     
    myTest();
    myTest();
    myTest();
    ?>

echo 和 print 语句
------------------------------------------------------------------

echo 和 print 区别:
 - echo - 可以输出一个或多个字符串
 - print - 只允许输出一个字符串，返回值总为 1

提示：echo 输出的速度比 print 快， echo 没有返回值，print有返回值1。


PHP EOF(heredoc) 使用说明
------------------------------------------------------------------

PHP EOF(heredoc)是一种在命令行shell（如sh、csh、ksh、bash、PowerShell和zsh）和程序语言（像Perl、PHP、Python和Ruby）里定义一个字串的方法。

使用概述：
 1. 必须后接分号，否则编译通不过
 2. EOF 可以用任意其它字符代替，只需保证结束标识与开始标识一致。
 3. 结束标识必须顶格独自占一行(即必须从行首开始，前后不能衔接任何空白和字符)。
 4. 开始标识可以不带引号或带单双引号，不带引号与带双引号效果一致，解释内嵌的变量和转义符号，带单引号则不解释内嵌的变量和转义符号。
 5. 当内容需要内嵌引号（单引号或双引号）时，不需要加转义符，本身对单双引号转义，此处相当与q和qq的用法。

::

    <?php
    echo <<<EOF
        <h1>我的第一个标题</h1>
        <p>我的第一个段落。</p>
    EOF;
    // 结束需要独立一行且前后不能空格
    ?>

PHP 5 数据类型
------------------------------------------------------------------

String（字符串）, Integer（整型）, Float（浮点型）, Boolean（布尔型）, Array（数组）, Object（对象）, NULL（空值）。

PHP 字符串
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

一个字符串是一串字符的序列，就像 "Hello world!"。

你可以将任何文本放在单引号和双引号中::

    <?php 
    $x = "Hello world!";
    echo $x;
    echo "<br>"; 
    $x = 'Hello world!';
    echo $x;
    ?>

PHP 整型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

整数是一个没有小数的数字。

整数规则:
 - 整数必须至少有一个数字 (0-9)
 - 整数不能包含逗号或空格
 - 整数是没有小数点的
 - 整数可以是正数或负数
 - 整型可以用三种格式来指定：十进制， 十六进制（ 以 0x 为前缀）或八进制（前缀为 0）。

PHP 浮点型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

浮点数是带小数部分的数字，或是指数形式。

PHP 布尔型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

布尔型可以是 TRUE 或 FALSE。

PHP 数组
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

数组可以在一个变量中存储多个值。

在以下实例中创建了一个数组， 然后使用 PHP var_dump() 函数返回数组的数据类型和值：

::

    <?php 
    $cars=array("Volvo","BMW","Toyota");
    var_dump($cars);
    ?>

PHP 对象
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

对象数据类型也可以用于存储数据。

在 PHP 中，对象必须声明。

首先，你必须使用class关键字声明类对象。类是可以包含属性和方法的结构。

然后我们在类中定义数据类型，然后在实例化的类中使用数据类型::

    <?php
    class Car
    {
      var $color;
      function __construct($color="green") {
        $this->color = $color;
      }
      function what_color() {
        return $this->color;
      }
    }
    ?>

PHP NULL 值
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NULL 值表示变量没有值。NULL 是数据类型为 NULL 的值。

NULL 值指明一个变量是否为空值。 同样可用于数据空值和NULL值的区别。

可以通过设置变量值为 NULL 来清空变量数据::

    <?php
    $x="Hello world!";
    $x=null;
    var_dump($x);
    ?>    

PHP 5 常量
------------------------------------------------------------------

常量值被定义后，在脚本的其他任何地方都不能被改变。

常量是一个简单值的标识符。该值在脚本中不能改变。

一个常量由英文字母、下划线、和数字组成,但数字不能作为首字母出现。 (常量名不需要加 $ 修饰符)。

注意： 常量在整个脚本中都可以使用。

设置常量，使用 define() 函数，函数语法如下::

    bool define ( string $name , mixed $value [, bool $case_insensitive = false ] )

该函数有三个参数:
 - name：必选参数，常量名称，即标志符。
 - value：必选参数，常量的值。
 - case_insensitive ：可选参数，如果设置为 TRUE，该常量则大小写不敏感。默认是大小写敏感的。

常量在定义后，默认是全局变量，可以在整个运行的脚本的任何地方使用。

PHP 字符串变量
------------------------------------------------------------------

在 PHP 中，只有一个字符串运算符。

并置运算符 (.) 用于把两个字符串值连接起来。

在下面的实例中，我们创建一个名为 txt 的字符串变量，并赋值为 "Hello world!" 。然后我们输出 txt 变量的值::

    <?php 
    $txt="Hello world!"; 
    echo $txt; 
    ?>

PHP 运算符
------------------------------------------------------------------

算术运算符::

    <?php 
    $x=10; 
    $y=6;
    echo ($x + $y); // 输出16
    echo '<br>';  // 换行
     
    echo ($x - $y); // 输出4
    echo '<br>';  // 换行
     
    echo ($x * $y); // 输出60
    echo '<br>';  // 换行
     
    echo ($x / $y); // 输出1.6666666666667
    echo '<br>';  // 换行
     
    echo ($x % $y); // 输出4
    echo '<br>';  // 换行
     
    echo -$x;
    ?>

PHP7+ 版本新增整除运算符 intdiv(),使用实例::

    var_dump(intdiv(10, 3));

PHP 赋值运算符::

    <?php 
    $x=10; 
    echo $x; // 输出10
     
    $y=20; 
    $y += 100;
    echo $y; // 输出120
     
    $z=50;
    $z -= 25;
    echo $z; // 输出25
     
    $i=5;
    $i *= 6;
    echo $i; // 输出30
     
    $j=10;
    $j /= 5;
    echo $j; // 输出2
     
    $k=15;
    $k %= 4;
    echo $k; // 输出3

    $a = "Hello";
    $b = $a . " world!";
    echo $b; // 输出Hello world! 
     
    $x="Hello";
    $x .= " world!";
    echo $x; // 输出Hello world! 

    ?>

PHP 递增/递减运算符::

    <?php
    $x=10; 
    echo ++$x; // 输出11
     
    $y=10; 
    echo $y++; // 输出10
     
    $z=5;
    echo --$z; // 输出4
     
    $i=5;
    echo $i--; // 输出5
    ?>

PHP 比较运算符::

    <?php
    $x=100; 
    $y="100";
     
    var_dump($x == $y);
    echo "<br>";
    var_dump($x === $y);
    echo "<br>";
    var_dump($x != $y);
    echo "<br>";
    var_dump($x !== $y);
    echo "<br>";
     
    $a=50;
    $b=90;
     
    var_dump($a > $b);
    echo "<br>";
    var_dump($a < $b);
    ?>

PHP 逻辑运算符::

    <?php
    $x = array("a" => "red", "b" => "green"); 
    $y = array("c" => "blue", "d" => "yellow"); 
    $z = $x + $y; // $x 和 $y 数组合并
    var_dump($z);
    var_dump($x == $y);
    var_dump($x === $y);
    var_dump($x != $y);
    var_dump($x <> $y);
    var_dump($x !== $y);
    ?>

三元运算符::

    (expr1) ? (expr2) : (expr3) 
    //对 expr1 求值为 TRUE 时的值为 expr2，在 expr1 求值为 FALSE 时的值为 expr3。

    自 PHP 5.3 起，可以省略三元运算符中间那部分。表达式 expr1 ?: expr3 在 expr1 求值为 TRUE 时返回 expr1，否则返回 expr3。    


PHP If...Else 语句
------------------------------------------------------------------

在 PHP 中，提供了下列条件语句：
 - if 语句 - 在条件成立时执行代码
 - if...else 语句 - 在条件成立时执行一块代码，条件不成立时执行另一块代码
 - if...elseif....else 语句 - 在若干条件之一成立时执行一个代码块
 - switch 语句 - 在若干条件之一成立时执行一个代码块

::

    <?php
    $t=date("H");
    if ($t<"20"){
        echo "Have a good day!";
    }
    ?>


PHP Switch 语句
------------------------------------------------------------------

::

    <?php
    switch (n)
    {
    case label1:
        如果 n=label1，此处代码将执行;
        break;
    case label2:
        如果 n=label2，此处代码将执行;
        break;
    default:
        如果 n 既不等于 label1 也不等于 label2，此处代码将执行;
    }
    ?>


PHP 数组
------------------------------------------------------------------
::

    <?php
    $cars=array("Volvo","BMW","Toyota");
    $arrlength=count($cars);
     
    for($x=0;$x<$arrlength;$x++)
    {
        echo $cars[$x];
        echo "<br>";
    }
    ?>

PHP 数组排序
------------------------------------------------------------------
排列::

    $cars=array("Volvo","BMW","Toyota");
    //升序
    sort($cars);
    //降序
    rsort($cars);
    //根据数组的值，对数组进行升序排列
    $age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
    asort($age);
    //根据数组的键，对数组进行升序排列
    $age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
    ksort($age);
    //根据数组的值，对数组进行降序排列
    $age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
    arsort($age);
    //根据数组的键，对数组进行降序排列
    $age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
    krsort($age);

PHP超级全局变量    
------------------------------------------------------------------
PHP中预定义了几个超级全局变量（superglobals） ，这意味着它们在一个脚本的全部作用域中都可用。 你不需要特别说明，就可以在函数及类中使用。

PHP 超级全局变量列表:
 - $GLOBALS
 - $_SERVER
 - $_REQUEST
 - $_POST
 - $_GET
 - $_FILES
 - $_ENV
 - $_COOKIE
 - $_SESSION

详细访问：http://www.runoob.com/php/php-superglobals.html

PHP 循环
------------------------------------------------------------------

在 PHP 中，提供了下列循环语句：
 - while - 只要指定的条件成立，则循环执行代码块
 - do...while - 首先执行一次代码块，然后在指定的条件成立时重复这个循环
 - for - 循环执行代码块指定的次数
 - foreach - 根据数组中每个元素来循环代码块

while 循环::

    $i=1;
    while($i<=5){
        echo "The number is " . $i . "<br>";
        $i++;
    } 

do...while 语句::

    $i=1;
    do{
        $i++;
        echo "The number is " . $i . "<br>";
    }
    while ($i<=5);


for 循环用于您预先知道脚本需要运行的次数的情况::

    for ($i=1; $i<=5; $i++){
        echo "The number is " . $i . "<br>";
    }

foreach 循环用于遍历数组::

    $x=array("one","two","three");
    foreach ($x as $value){
        echo $value . "<br>";
    }

PHP 函数
------------------------------------------------------------------

::

    function writeName(){
        echo "Kai Jim Refsnes";
    }
     
    echo "My name is ";
    writeName();

PHP 函数 - 添加参数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

     <?php
    function writeName($fname){
        echo $fname . " Refsnes.<br>";
    }
     
    echo "My name is ";
    writeName("Kai Jim");
    echo "My sister's name is ";
    writeName("Hege");
    echo "My brother's name is ";
    writeName("Stale");
    ?>

PHP 函数 - 返回值
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    <?php
    function add($x,$y){
        $total=$x+$y;
        return $total;
    }
     
    echo "1 + 16 = " . add(1,16);
    ?>

PHP 魔术常量
------------------------------------------------------------------

PHP 向它运行的任何脚本提供了大量的预定义常量。

不过很多常量都是由不同的扩展库定义的，只有在加载了这些扩展库时才会出现，或者动态加载后，或者在编译时已经包括进去了。

有八个魔术常量它们的值随着它们在代码中的位置改变而改变。

__LINE__: 文件中的当前行号

__FILE__:文件的完整路径和文件名。如果用在被包含文件中，则返回被包含的文件名。

__DIR__:文件所在的目录。如果用在被包括文件中，则返回被包括的文件所在的目录。

__FUNCTION__:函数名称（PHP 4.3.0 新加）。自 PHP 5 起本常量返回该函数被定义时的名字（区分大小写）。在 PHP 4 中该值总是小写字母的。

__CLASS__:类的名称（PHP 4.3.0 新加）。自 PHP 5 起本常量返回该类被定义时的名字（区分大小写）。

__TRAIT__:Trait 的名字（PHP 5.4.0 新加）。自 PHP 5.4.0 起，PHP 实现了代码复用的一个方法，称为 traits。

::

    <?php
    class Base {
        public function sayHello() {
            echo 'Hello ';
        }
    }
     
    trait SayWorld {
        public function sayHello() {
            parent::sayHello();
            echo 'World!';
        }
    }
     
    class MyHelloWorld extends Base {
        use SayWorld;
    }
     
    $o = new MyHelloWorld();
    $o->sayHello();
    ?>

__METHOD__:类的方法名（PHP 5.0.0 新加）。返回该方法被定义时的名字（区分大小写）。

__NAMESPACE__:当前命名空间的名称（区分大小写）。此常量是在编译时定义的（PHP 5.3.0 新增）。

PHP 命名空间(namespace)
------------------------------------------------------------------

PHP 命名空间可以解决以下两类问题：
 1. 用户编写的代码与PHP内部的类/函数/常量或第三方类/函数/常量之间的名字冲突。
 2. 为很长的标识符名称(通常是为了缓解第一类问题而定义的)创建一个别名（或简短）的名称，提高源代码的可读性。

定义命名空间
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

默认情况下，所有常量、类和函数名都放在全局空间下，就和PHP支持命名空间之前一样。

命名空间通过关键字namespace 来声明。如果一个文件中包含命名空间，它必须在其它所有代码之前声明命名空间。语法格式如下；
::

    <?php  
    // 定义代码在 'MyProject' 命名空间中  
    namespace MyProject;  
     
    // ... 代码 ... 

也可以在同一个文件中定义不同的命名空间代码，如::

    <?php  
    namespace MyProject;

    const CONNECT_OK = 1;
    class Connection { /* ... */ }
    function connect() { /* ... */  }

    namespace AnotherProject;

    const CONNECT_OK = 1;
    class Connection { /* ... */ }
    function connect() { /* ... */  }
    ?>  

不建议使用这种语法在单个文件中定义多个命名空间。建议使用下面的大括号形式的语法::

    <?php
    namespace MyProject {
        const CONNECT_OK = 1;
        class Connection { /* ... */ }
        function connect() { /* ... */  }
    }

    namespace AnotherProject {
        const CONNECT_OK = 1;
        class Connection { /* ... */ }
        function connect() { /* ... */  }
    }
    ?>

将全局的非命名空间中的代码与命名空间中的代码组合在一起，只能使用大括号形式的语法。全局代码必须用一个不带名称的 namespace 语句加上大括号括起来，例如::

    <?php
    namespace MyProject {

    const CONNECT_OK = 1;
    class Connection { /* ... */ }
    function connect() { /* ... */  }
    }

    namespace { // 全局代码
    session_start();
    $a = MyProject\connect();
    echo MyProject\Connection::start();
    }
    ?>

在声明命名空间之前唯一合法的代码是用于定义源文件编码方式的 declare 语句。所有非 PHP 代码包括空白符都不能出现在命名空间的声明之前。

::

    <?php
    declare(encoding='UTF-8'); //定义多个命名空间和不包含在命名空间中的代码
    namespace MyProject {

    const CONNECT_OK = 1;
    class Connection { /* ... */ }
    function connect() { /* ... */  }
    }

    namespace { // 全局代码
    session_start();
    $a = MyProject\connect();
    echo MyProject\Connection::start();
    }
    ?>

子命名空间
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    <?php
    namespace MyProject\Sub\Level;  //声明分层次的单个命名空间

    const CONNECT_OK = 1;
    class Connection { /* ... */ }
    function Connect() { /* ... */  }

    ?>

命名空间使用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PHP 命名空间中的类名可以通过三种方式引用：
 - 非限定名称，或不包含前缀的类名称
 - 限定名称,或包含前缀的名称
 - 完全限定名称，或包含了全局前缀操作符的名称

namespace关键字和__NAMESPACE__常量
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PHP支持两种抽象的访问当前命名空间内部元素的方法，__NAMESPACE__ 魔术常量和namespace关键字。

常量__NAMESPACE__的值是包含当前命名空间名称的字符串。在全局的，不包括在任何命名空间中的代码，它包含一个空的字符串。

使用命名空间：别名/导入
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PHP 命名空间支持 有两种使用别名或导入方式：为类名称使用别名，或为命名空间名称使用别名。

在PHP中，别名是通过操作符 use 来实现的. 下面是一个使用所有可能的三种导入方式的例子：

1、使用use操作符导入/使用别名::

    <?php
    namespace foo;
    use My\Full\Classname as Another;

    // 下面的例子与 use My\Full\NSname as NSname 相同
    use My\Full\NSname;

    // 导入一个全局类
    use \ArrayObject;

    $obj = new namespace\Another; // 实例化 foo\Another 对象
    $obj = new Another; // 实例化 My\Full\Classname　对象
    NSname\subns\func(); // 调用函数 My\Full\NSname\subns\func
    $a = new ArrayObject(array(1)); // 实例化 ArrayObject 对象
    // 如果不使用 "use \ArrayObject" ，则实例化一个 foo\ArrayObject 对象
    ?>

2.一行中包含多个use语句::

    <?php
    use My\Full\Classname as Another, My\Full\NSname;

    $obj = new Another; // 实例化 My\Full\Classname 对象
    NSname\subns\func(); // 调用函数 My\Full\NSname\subns\func
    ?>

3、导入和动态名称::

    <?php
    use My\Full\Classname as Another, My\Full\NSname;

    $obj = new Another; // 实例化一个 My\Full\Classname 对象
    $a = 'Another';
    $obj = new $a;      // 实际化一个 Another 对象
    ?>

4、导入和完全限定名称::

    <?php
    use My\Full\Classname as Another, My\Full\NSname;

    $obj = new Another; // 实例化 My\Full\Classname 类
    $obj = new \Another; // 实例化 Another 类
    $obj = new Another\thing; // 实例化 My\Full\Classname\thing 类
    $obj = new \Another\thing; // 实例化 Another\thing 类
    ?>


更详细：http://www.runoob.com/php/php-namespace.html

PHP 面向对象
------------------------------------------------------------------

::

    $mercedes = new Car ();
    $bmw = new Car ();
    $audi = new Car ();

::

    <?php
    class Site {
      /* 成员变量 */
      var $url;
      var $title;
      
      /* 成员函数 */
      function setUrl($par){
         $this->url = $par;
      }
      
      function getUrl(){
         echo $this->url . PHP_EOL;
      }
      
      function setTitle($par){
         $this->title = $par;
      }
      
      function getTitle(){
         echo $this->title . PHP_EOL;
      }
    }
    ?>

变量 $this 代表自身的对象。

PHP 中创建对象
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

类创建后，我们可以使用 new 运算符来实例化该类的对象::

    $runoob = new Site;
    $taobao = new Site;
    $google = new Site;

调用成员方法::

    // 调用成员函数，设置标题和URL
    $runoob->setTitle( "菜鸟教程" );
    $taobao->setTitle( "淘宝" );
    $google->setTitle( "Google 搜索" );

    $runoob->setUrl( 'www.runoob.com' );
    $taobao->setUrl( 'www.taobao.com' );
    $google->setUrl( 'www.google.com' );

    // 调用成员函数，获取标题和URL
    $runoob->getTitle();
    $taobao->getTitle();
    $google->getTitle();

    $runoob->getUrl();
    $taobao->getUrl();
    $google->getUrl();


内容有些多，详情访问：http://www.runoob.com/php/php-oop.html


PHP 表单和用户输入
------------------------------------------------------------------






菜鸟教程的Java教程
==============================================



基础
---------------------------------------------------------------------

**环境搭建、注释、基本语法、循环、判断、类型等**



下载java并安装：https://www.oracle.com/technetwork/java/javase/downloads/index.html


cmd下输入java -version  查看版本 


创建java文件test.java::

    public class HelloWorld {
        public static void main(String []args) {
            System.out.println("Hello World");
        }
    }


run::

    java test.java


基本语法规则：
 - 大小写敏感：Java是大小写敏感的，这就意味着标识符Hello与hello是不同的。
 - 类名：对于所有的类来说，类名的首字母应该大写。如果类名由若干单词组成，那么每个单词的首字母应该大写，例如 MyFirstJavaClass 。
 - 方法名：所有的方法名都应该以小写字母开头。如果方法名含有若干单词，则后面的每个单词首字母大写。
 - 源文件名：源文件名必须和类名相同。当保存文件的时候，你应该使用类名作为文件名保存（切记Java是大小写敏感的），文件名的后缀为.java。（如果文件名和类名不相同则会导致编译错误）。
 - 主方法入口：所有的Java 程序由public static void main(String []args)方法开始执行。


注释::

    public class HelloWorld {
       /* 这是第一个Java程序
        *它将打印Hello World
        * 这是一个多行注释的示例
        */
        public static void main(String []args){
           // 这是单行注释的示例
           /* 这个也是单行注释的示例 */
           System.out.println("Hello World"); 
        }
    }


类::

    public class Dog{
      String breed;
      int age;
      String color;
      void barking(){
      }
     
      void hungry(){
      }
     
      void sleeping(){
      }
    }    


构造方法::

    public class Puppy{
        public Puppy(){
        }
     
        public Puppy(String name){
            // 这个构造器仅有一个参数：name
        }
    }


创建对象::

    public class Puppy{
       public Puppy(String name){
          //这个构造器仅有一个参数：name
          System.out.println("小狗的名字是 : " + name ); 
       }
       public static void main(String []args){
          // 下面的语句将创建一个Puppy对象
          Puppy myPuppy = new Puppy( "tommy" );
       }
    }


访问实例变量和方法::

    /* 实例化对象 */
    ObjectReference = new Constructor();
    /* 访问类中的变量 */
    ObjectReference.variableName;
    /* 访问类中的方法 */
    ObjectReference.methodName();

实例::

    public class Puppy{
       int puppyAge;
       public Puppy(String name){
          // 这个构造器仅有一个参数：name
          System.out.println("小狗的名字是 : " + name ); 
       }
     
       public void setAge( int age ){
           puppyAge = age;
       }
     
       public int getAge( ){
           System.out.println("小狗的年龄为 : " + puppyAge ); 
           return puppyAge;
       }
     
       public static void main(String []args){
          /* 创建对象 */
          Puppy myPuppy = new Puppy( "tommy" );
          /* 通过方法来设定age */
          myPuppy.setAge( 2 );
          /* 调用另一个方法获取age */
          myPuppy.getAge( );
          /*你也可以像下面这样访问成员变量 */
          System.out.println("变量值 : " + myPuppy.puppyAge ); 
       }
    }


源文件声明规则:
 - 一个源文件中只能有一个public类
 - 一个源文件可以有多个非public类
 - 源文件的名称应该和public类的类名保持一致。例如：源文件中public类的类名是Employee，那么源文件应该命名为Employee.java。
 - 如果一个类定义在某个包中，那么package语句应该在源文件的首行。
 - 如果源文件包含import语句，那么应该放在package语句和类定义之间。如果没有package语句，那么import语句应该在源文件中最前面。
 - import语句和package语句对源文件中定义的所有类都有效。在同一源文件中，不能给不同的类不同的包声明。


Import语句::

    import java.io.*;


一个简单的例子:

在该例子中，我们创建两个类：Employee 和 EmployeeTest。

Employee类有四个成员变量：name、age、designation和salary。该类显式声明了一个构造方法，该方法只有一个参数。

::

    import java.io.*;
 
    public class Employee{
       String name;
       int age;
       String designation;
       double salary;
       // Employee 类的构造器
       public Employee(String name){
          this.name = name;
       }
       // 设置age的值
       public void empAge(int empAge){
          age =  empAge;
       }
       /* 设置designation的值*/
       public void empDesignation(String empDesig){
          designation = empDesig;
       }
       /* 设置salary的值*/
       public void empSalary(double empSalary){
          salary = empSalary;
       }
       /* 打印信息 */
       public void printEmployee(){
          System.out.println("名字:"+ name );
          System.out.println("年龄:" + age );
          System.out.println("职位:" + designation );
          System.out.println("薪水:" + salary);
       }
    }


程序都是从main方法开始执行。为了能运行这个程序，必须包含main方法并且创建一个实例对象。

下面给出EmployeeTest类，该类实例化2个 Employee 类的实例，并调用方法设置变量的值。

将下面的代码保存在 EmployeeTest.java文件中。

EmployeeTest.java ::

    import java.io.*;
    public class EmployeeTest{
     
       public static void main(String []args){
          /* 使用构造器创建两个对象 */
          Employee empOne = new Employee("RUNOOB1");
          Employee empTwo = new Employee("RUNOOB2");
     
          // 调用这两个对象的成员方法
          empOne.empAge(26);
          empOne.empDesignation("高级程序员");
          empOne.empSalary(1000);
          empOne.printEmployee();
     
          empTwo.empAge(21);
          empTwo.empDesignation("菜鸟程序员");
          empTwo.empSalary(500);
          empTwo.printEmployee();
       }
    }


这里卡着了  没办法 import  路径不对

还是只能找到idea工具 使用程序来运行了  

复制过来运行命令一行 太长了    必须指定绝对路径     不是个好办法

IDEA注册码：https://blog.csdn.net/q258523454/article/details/79775092

这两个类 不用import的话 同级  的命令运行：
/Library/Java/JavaVirtualMachines/jdk-11.0.2.jdk/Contents/Home/bin/java 
"-javaagent:/Applications/IntelliJ IDEA.app/Contents/lib/idea_rt.jar=52431:/Applications/IntelliJ IDEA.app/Contents/bin" -Dfile.encoding=UTF-8 
-classpath 
/Volumes/mydata/www/java/idea/out/production/idea EmployeeTest

基本数据类型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Java语言提供了八种基本类型。六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。

byte、short、int、long、float、double、boolean、char

引用类型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在Java中，引用类型的变量非常类似于C/C++的指针。引用类型指向一个对象，指向对象的变量是引用变量。这些变量在声明时被指定为一个特定的类型，比如 Employee、Puppy 等。变量一旦声明后，类型就不能被改变了。

对象、数组都是引用数据类型。

所有引用类型的默认值都是null。

一个引用变量可以用来引用任何与之兼容的类型。

例子：Site site = new Site("Runoob")。


Java 常量
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 final 关键字来修饰常量，声明方式和变量类似::

    final double PI = 3.1415927;

强制类型转换
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  public class QiangZhiZhuanHuan{
      public static void main(String[] args){
          int i1 = 123;
          byte b = (byte)i1;//强制类型转换为byte
          System.out.println("int强制类型转换为byte后的值等于"+b);
      }
  }


Java 变量类型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Java语言支持的变量类型有：
 - 类变量：独立于方法之外的变量，用 static 修饰。
 - 实例变量：独立于方法之外的变量，不过没有 static 修饰。
 - 局部变量：类的方法中的变量。

::

  public class Variable{
      static int allClicks=0;    // 类变量
   
      String str="hello world";  // 实例变量
   
      public void method(){
   
          int i =0;  // 局部变量
   
      }
  }

实例变量：
 - 实例变量声明在一个类中，但在方法、构造方法和语句块之外；
 - 当一个对象被实例化之后，每个实例变量的值就跟着确定；
 - 实例变量在对象创建的时候创建，在对象被销毁的时候销毁；
 - 实例变量的值应该至少被一个方法、构造方法或者语句块引用，使得外部能够通过这些方式获取实例变量信息；
 - 实例变量可以声明在使用前或者使用后；
 - 访问修饰符可以修饰实例变量；
 - 实例变量对于类中的方法、构造方法或者语句块是可见的。一般情况下应该把实例变量设为私有。通过使用访问修饰符可以使实例变量对子类可见；
 - 实例变量具有默认值。数值型变量的默认值是0，布尔型变量的默认值是false，引用类型变量的默认值是null。变量的值可以在声明时指定，也可以在构造方法中指定；
 - 实例变量可以直接通过变量名访问。但在静态方法以及其他类中，就应该使用完全限定名：ObejectReference.VariableName。

实例::

  public class Employee{
     // 这个实例变量对子类可见
     public String name;
     // 私有变量，仅在该类可见
     private double salary;
     //在构造器中对name赋值
     public Employee (String empName){
        name = empName;
     }
     //设定salary的值
     public void setSalary(double empSal){
        salary = empSal;
     }  
     // 打印信息
     public void printEmp(){
        System.out.println("名字 : " + name );
        System.out.println("薪水 : " + salary);
     }
   
     public static void main(String[] args){
        Employee empOne = new Employee("RUNOOB");
        empOne.setSalary(1000);
        empOne.printEmp();
     }
  }

类变量（静态变量）：
 - 类变量也称为静态变量，在类中以static关键字声明，但必须在方法构造方法和语句块之外。
 - 无论一个类创建了多少个对象，类只拥有类变量的一份拷贝。
 - 静态变量除了被声明为常量外很少使用。常量是指声明为public/private，final和static类型的变量。常量初始化后不可改变。
 - 静态变量储存在静态存储区。经常被声明为常量，很少单独使用static声明变量。
 - 静态变量在第一次被访问时创建，在程序结束时销毁。
 - 与实例变量具有相似的可见性。但为了对类的使用者可见，大多数静态变量声明为public类型。
 - 默认值和实例变量相似。数值型变量默认值是0，布尔型默认值是false，引用类型默认值是null。变量的值可以在声明的时候指定，也可以在构造方法中指定。此外，静态变量还可以在静态语句块中初始化。
 - 静态变量可以通过：ClassName.VariableName的方式访问。
 - 类变量被声明为public static final类型时，类变量名称一般建议使用大写字母。如果静态变量不是public和final类型，其命名方式与实例变量以及局部变量的命名方式一致。

实例::

  public class Employee {
      //salary是静态的私有变量
      private static double salary;
      // DEPARTMENT是一个常量
      public static final String DEPARTMENT = "开发人员";
      public static void main(String[] args){
      salary = 10000;
          System.out.println(DEPARTMENT+"平均工资:"+salary);
      }
  }


Java 修饰符
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

default private  public  protected 

非访问修饰符：
 - static 修饰符，用来修饰类方法和类变量。
 - final 修饰符，用来修饰类、方法和变量，final 修饰的类不能够被继承，修饰的方法不能被继承类重新定义，修饰的变量为常量，是不可修改的。
 - abstract 修饰符，用来创建抽象类和抽象方法。
 - synchronized 和 volatile 修饰符，主要用于线程的编程


static 修饰符：静态变量：

static 关键字用来声明独立于对象的静态变量，无论一个类实例化多少对象，它的静态变量只有一份拷贝。 静态变量也被称为类变量。局部变量不能被声明为 static 变量。

静态方法：

static 关键字用来声明独立于对象的静态方法。静态方法不能使用类的非静态变量。静态方法从参数列表得到数据，然后计算这些数据

final 修饰符

final 表示"最后的、最终的"含义，变量一旦赋值后，不能被重新赋值。被 final 修饰的实例变量必须显式指定初始值。

final 修饰符通常和 static 修饰符一起使用来创建类常量。

final 方法

类中的 final 方法可以被子类继承，但是不能被子类修改。

声明 final 方法的主要目的是防止该方法的内容被修改。

final 类不能被继承，没有类能够继承 final 类的任何特性。

abstract 修饰符

抽象类不能用来实例化对象，声明抽象类的唯一目的是为了将来对该类进行扩充。

一个类不能同时被 abstract 和 final 修饰。如果一个类包含抽象方法，那么该类一定要声明为抽象类，否则将出现编译错误。

抽象类可以包含抽象方法和非抽象方法。

抽象方法

抽象方法是一种没有任何实现的方法，该方法的的具体实现由子类提供。

抽象方法不能被声明成 final 和 static。

任何继承抽象类的子类必须实现父类的所有抽象方法，除非该子类也是抽象类。

如果一个类包含若干个抽象方法，那么该类必须声明为抽象类。抽象类可以不包含抽象方法。

抽象方法的声明以分号结尾，例如：public abstract sample();。

synchronized 修饰符

synchronized 关键字声明的方法同一时间只能被一个线程访问。synchronized 修饰符可以应用于四个访问修饰符。

transient 修饰符

序列化的对象包含被 transient 修饰的实例变量时，java 虚拟机(JVM)跳过该特定的变量。

该修饰符包含在定义变量的语句中，用来预处理类和变量的数据类型。

volatile 修饰符

volatile 修饰的成员变量在每次被线程访问时，都强制从共享内存中重新读取该成员变量的值。而且，当成员变量发生变化时，会强制线程将变化值回写到共享内存。这样在任何时刻，两个不同的线程总是看到某个成员变量的同一个值。

Java 运算符
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

算术运算符

+ - \* \/ ++ -- %

关系运算符

== ！= > < >= <=

位运算符 [少用]

& | ^ 

逻辑运算符

&&  ||  ！

赋值运算符
 
略

条件运算符（?:）


instanceof 运算符

该运算符用于操作对象实例，检查该对象是否是一个特定类型（类类型或接口类型）。

算是比较运算符把，，比较是否是这个对象

循环
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


while 循环::

  while( 布尔表达式 ) {
    //循环内容
  }

do…while 循环::

  do {
         //代码语句
  }while(布尔表达式);

for 循环::

  for(初始化; 布尔表达式; 更新) {
      //代码语句
  }

增强 for 循环::

  for(声明语句 : 表达式)
  {
     //代码句子
  }


**break 关键字**

**continue  关键字**


条件语句
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  if(布尔表达式)
  {
     //如果布尔表达式为true将执行的语句
  }

  if(布尔表达式){
     //如果布尔表达式的值为true
  }else{
     //如果布尔表达式的值为false
  }

  if(布尔表达式 1){
     //如果布尔表达式 1的值为true执行代码
  }else if(布尔表达式 2){
     //如果布尔表达式 2的值为true执行代码
  }else if(布尔表达式 3){
     //如果布尔表达式 3的值为true执行代码
  }else {
     //如果以上布尔表达式都不为true执行代码
  }


switch case 语句
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  switch(expression){
      case value :
         //语句
         break; //可选
      case value :
         //语句
         break; //可选
      //你可以有任意数量的case语句
      default : //可选
         //语句
  }


异常处理
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  try
  {
     // 程序代码
  }catch(ExceptionName e1)
  {
     //Catch 块
  }





















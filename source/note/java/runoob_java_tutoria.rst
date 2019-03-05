菜鸟教程的Java教程
==============================================


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








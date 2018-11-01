菜鸟教程的python3教程
==================================

查看版本::

    python -V

第一个Python3.x程序::

    print("Hello, World!")


Python3 环境搭建
---------------------------------------------------------------------

Python3 可应用于多平台包括 Windows、Linux 和 Mac OS X。
 - Unix (Solaris, Linux, FreeBSD, AIX, HP/UX, SunOS, IRIX, 等等。)
 - Win 9x/NT/2000
 - Macintosh (Intel, PPC, 68K)
 - OS/2
 - DOS (多个DOS版本)
 - PalmOS
 - Nokia 移动手机
 - Windows CE
 - Acorn/RISC OS
 - BeOS
 - Amiga
 - VMS/OpenVMS
 - QNX
 - VxWorks
 - Psion
 - Python 同样可以移植到 Java 和 .NET 虚拟机上。

Python3 下载
---------------------------------------------------------------------

python3 最新源码，二进制文档，新闻资讯等可以在 Python 的官网查看到：

Python 官网：https://www.python.org/

你可以在以下链接中下载 Python 的文档，你可以下载 HTML、PDF 和 PostScript 等格式的文档。

Python文档下载地址：https://www.python.org/doc/


Python 安装
---------------------------------------------------------------------

Python 已经被移植在许多平台上（经过改动使它能够工作在不同平台上）。

您需要下载适用于您使用平台的二进制代码，然后安装 Python。

如果您平台的二进制代码是不可用的，你需要使用C编译器手动编译源代码。

编译的源代码，功能上有更多的选择性， 为 Python 安装提供了更多的灵活性。


Unix & Linux 平台安装 Python3::

    这里菜鸟教程的安装方式会有一定的问题，请参照我的笔记，Linux下升级Python

Window 平台安装 Python:

直接下载双击运行exe安装即可，没这么复杂。

环境变量配置
---------------------------------------------------------------------

程序和可执行文件可以在许多目录，而这些路径很可能不在操作系统提供可执行文件的搜索路径中。

path(路径)存储在环境变量中，这是由操作系统维护的一个命名的字符串。这些变量包含可用的命令行解释器和其他程序的信息。

Unix或Windows中路径变量为PATH（UNIX区分大小写，Windows不区分大小写）。

在Mac OS中，安装程序过程中改变了python的安装路径。如果你需要在其他目录引用Python，你必须在path中添加Python目录。

在 Unix/Linux 设置环境变量
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 csh shell: 输入::

    setenv PATH "$PATH:/usr/local/bin/python"

在 bash shell (Linux): 输入 ::

    export PATH="$PATH:/usr/local/bin/python" 

在 sh 或者 ksh shell: 输入 ::

    PATH="$PATH:/usr/local/bin/python" 

**注意: /usr/local/bin/python 是 Python 的安装目录。**

在 Windows 设置环境变量
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在环境变量中添加Python目录：

在命令提示框中(cmd) : 输入 ::

    path=%path%;C:\Python 

按下"Enter"。

**注意: C:\Python 是Python的安装目录。**

也可以通过以下方式设置：
 - 右键点击"计算机"，然后点击"属性"
 - 然后点击"高级系统设置"
 - 选择"系统变量"窗口下面的"Path",双击即可！
 - 然后在"Path"行，添加python安装路径即可(我的D:\Python32)，所以在后面，添加该路径即可。 

ps：记住，路径直接用分号"；"隔开！最后设置成功以后，在cmd命令行，输入命令"python"，就可以有相关显示。


运行Python
---------------------------------------------------------------------

有三种方式可以运行Python：

1、交互式解释器：

你可以通过命令行窗口进入python并开在交互式解释器中开始编写Python代码。

你可以在Unix，DOS或任何其他提供了命令行或者shell的系统进行python编码工作。

::

    $ python # Unix/Linux 
    或者 
    C:>python # Windows/DOS

以下为Python命令行参数：
 - 选项  描述
 - -d  在解析时显示调试信息
 - -O  生成优化代码 ( .pyo 文件 )
 - -S  启动时不引入查找Python路径的位置
 - -V  输出Python版本号
 - -X  从 1.6版本之后基于内建的异常（仅仅用于字符串）已过时。
 - -c cmd  执行 Python 脚本，并将运行结果作为 cmd 字符串。
 - file    在给定的python文件执行python脚本。

Python3 基础语法
---------------------------------------------------------------------

**编码**

默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
::

    # -*- coding: cp-1252 -*-

标识符
 - 第一个字符必须是字母表中字母或下划线 _ 。
 - 标识符的其他的部分由字母、数字和下划线组成。
 - 标识符对大小写敏感。

在 Python 3 中，非 ASCII 标识符也是允许的了。

python保留字
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字::

    >>> import keyword
    >>> keyword.kwlist
    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

注释
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python中单行注释以 # 开头，实例如下::

    #!/usr/bin/python3
 
    # 第一个注释
    print ("Hello, Python!") # 第二个注释

执行以上代码，输出结果为::

    Hello, Python!

多行注释可以用多个 # 号，还有 ''' 和 """::

    #!/usr/bin/python3
     
    # 第一个注释
    # 第二个注释
     
    '''
    第三注释
    第四注释
    '''
     
    """
    第五注释
    第六注释
    """
    print ("Hello, Python!")

执行以上代码，输出结果为::

    Hello, Python!

行与缩进
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下::


    if True:
        print ("True")
    else:
        print ("False")

以下代码最后一行语句缩进数的空格数不一致，会导致运行错误::

    if True:
        print ("Answer")
        print ("True")
    else:
        print ("Answer")
      print ("False")    # 缩进不一致，会导致运行错误

以上程序由于缩进不一致，执行后会出现类似以下错误::

    File "test.py", line 6
        print ("False")    # 缩进不一致，会导致运行错误
                                      ^
    IndentationError: unindent does not match any outer indentation level

多行语句
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如::

    total = item_one + \
            item_two + \
            item_three

在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如::

    total = ['item_one', 'item_two', 'item_three',
            'item_four', 'item_five']

数字(Number)类型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

python中数字有四种类型：整数、布尔型、浮点数和复数。
 - int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
 - bool (布尔), 如 True。
 - float (浮点数), 如 1.23、3E-2
 - complex (复数), 如 1 + 2j、 1.1 + 2.2j

字符串(String)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
：
 - python中单引号和双引号使用完全相同。
 - 使用三引号('''或""")可以指定一个多行字符串。
 - 转义符 '\'
 - 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
 - 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
 - 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
 - Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
 - Python中的字符串不能改变。
 - Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
 - 字符串的截取的语法格式如下：变量[头下标:尾下标]

::
    word = '字符串'
    sentence = "这是一个句子。"
    paragraph = """这是一个段落，
    可以由多行组成"""

::

    #!/usr/bin/python3
     
    str='Runoob'
     
    print(str)                 # 输出字符串
    print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
    print(str[0])              # 输出字符串第一个字符
    print(str[2:5])            # 输出从第三个开始到第五个的字符
    print(str[2:])             # 输出从第三个开始的后的所有字符
    print(str * 2)             # 输出字符串两次
    print(str + '你好')        # 连接字符串
     
    print('------------------------------')
     
    print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

这里的 r 指 raw，即 raw string。输出结果为::

    Runoob
    Runoo
    R
    noo
    noob
    RunoobRunoob
    Runoob你好
    ------------------------------
    hello
    runoob
    hello\nrunoob

空行
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

记住：空行也是程序代码的一部分。

等待用户输入
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

执行下面的程序在按回车键后就会等待用户输入::


    #!/usr/bin/python3
    input("\n\n按下 enter 键后退出。")

以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

同一行显示多条语句
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例::

    #!/usr/bin/python3
    import sys; x = 'runoob'; sys.stdout.write(x + '\n')

使用脚本执行以上代码，输出结果为::

    runoob

使用交互式命令行执行，输出结果为::

    >>> import sys; x = 'runoob'; sys.stdout.write(x + '\n')
    runoob
    7

此处的 7 表示字符数。

多个语句构成代码组
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

缩进相同的一组语句构成一个代码块，我们称之代码组。

像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。

如下实例::

    if expression : 
       suite
    elif expression : 
       suite 
    else : 
       suite

Print 输出
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

    x="a"
    y="b"
    # 换行输出
    print( x )
    print( y )
     
    print('---------')
    # 不换行输出
    print( x, end=" " )
    print( y, end=" " )
    print()

以上实例执行结果为::

    a
    b
    ---------
    a b

import 与 from...import
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *

导入 sys 模块::

    import sys
    print('================Python import mode==========================');
    print ('命令行参数为:')
    for i in sys.argv:
        print (i)
    print ('\n python 路径为',sys.path)

导入 sys 模块的 argv,path 成员::

    from sys import argv,path  #  导入特定的成员
     
    print('================python from import===================================')
    print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

命令行参数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

很多程序可以执行一些操作来查看一些基本信息，Python可以使用-h参数查看各参数帮助信息::

    $ python -h
    usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
    Options and arguments (and corresponding environment variables):
    -c cmd : program passed in as string (terminates option list)
    -d     : debug output from parser (also PYTHONDEBUG=x)
    -E     : ignore environment variables (such as PYTHONPATH)
    -h     : print this help message and exit

    [ etc. ]

我们在使用脚本形式执行 Python 时，可以接收命令行输入的参数，具体使用可以参照 Python 3 命令行参数。



Python3 基本数据类型
---------------------------------------------------------------------

Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如::


    #!/usr/bin/python3
     
    counter = 100          # 整型变量
    miles   = 1000.0       # 浮点型变量
    name    = "runoob"     # 字符串
     
    print (counter)
    print (miles)
    print (name)


执行以上程序会输出如下结果::

    100
    1000.0
    runoob

多个变量赋值
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python允许你同时为多个变量赋值。例如::

    a = b = c = 1

以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。

您也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "runoob"
以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

标准数据类型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python3 中有六个标准的数据类型:
 - Number（数字）
 - String（字符串）
 - List（列表）
 - Tuple（元组）
 - Set（集合）
 - Dictionary（字典）

Python3 的六个标准数据类型中：
 - 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
 - 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

Number（数字）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

内置的 type() 函数可以用来查询变量所指的对象类型。

::

    >>> a, b, c, d = 20, 5.5, True, 4+3j
    >>> print(type(a), type(b), type(c), type(d))
    <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
    此外还可以用 isinstance 来判断：

::

    >>>a = 111
    >>> isinstance(a, int)
    True
    >>>

isinstance 和 type 的区别在于::

    class A:
        pass

    class B(A):
        pass

    isinstance(A(), A)  # returns True
    type(A()) == A      # returns True
    isinstance(B(), A)    # returns True
    type(B()) == A        # returns False

区别就是:
 - type()不会认为子类是一种父类类型。
 - isinstance()会认为子类是一种父类类型。

.. Note:: 注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

当你指定一个值时，Number 对象就会被创建::

    var1 = 1
    var2 = 10

您也可以使用del语句删除一些对象引用。

del语句的语法是::

    del var1[,var2[,var3[....,varN]]]

您可以通过使用del语句删除单个或多个对象。例如::

    del var
    del var_a, var_b
    数值运算
    实例
    >>>5 + 4  # 加法
    9
    >>> 4.3 - 2 # 减法
    2.3
    >>> 3 * 7  # 乘法
    21
    >>> 2 / 4  # 除法，得到一个浮点数
    0.5
    >>> 2 // 4 # 除法，得到一个整数
    0
    >>> 17 % 3 # 取余 
    2
    >>> 2 ** 5 # 乘方
    32

注意：
    1、Python可以同时为多个变量赋值，如a, b = 1, 2。
    2、一个变量可以通过赋值指向不同类型的对象。
    3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
    4、在混合计算时，Python会把整型转换成为浮点数。

数值类型实例:
 - int float   complex
 - 10  0.0 3.14j
 - 100 15.20   45.j
 - -786    -21.9   9.322e-36j
 - 080 32.3e+18    .876j
 - -0490   -90.    -.6545+0J
 - -0x260  -32.54e100  3e+26J
 - 0x69    70.2E-12    4.53e-7j

Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

String（字符串）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

字符串的截取的语法格式如下：

变量[头下标:尾下标]

索引值以 0 为开始值，-1 为从末尾的开始位置。

图略

加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，紧跟的数字为复制的次数。实例如下：

实例::

    #!/usr/bin/python3
     
    str = 'Runoob'
     
    print (str)          # 输出字符串
    print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
    print (str[0])       # 输出字符串第一个字符
    print (str[2:5])     # 输出从第三个开始到第五个的字符
    print (str[2:])      # 输出从第三个开始的后的所有字符
    print (str * 2)      # 输出字符串两次
    print (str + "TEST") # 连接字符串

执行以上程序会输出如下结果::

    Runoob
    Runoo
    R
    noo
    noob
    RunoobRunoob
    RunoobTEST

Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：

::

    >>> print('Ru\noob')
    Ru
    oob
    >>> print(r'Ru\noob')
    Ru\noob
    >>> 

另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。

注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。

::

    >>>word = 'Python'
    >>> print(word[0], word[5])
    P n
    >>> print(word[-1], word[-6])
    n P

与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。

注意：
    1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
    2、字符串可以用+运算符连接在一起，用*运算符重复。
    3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
    4、Python中的字符串不能改变。

List（列表）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

列表截取的语法格式如下：

变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。



加号 + 是列表连接运算符，星号 * 是重复操作。如下实例：
::

    #!/usr/bin/python3
 
    list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
    tinylist = [123, 'runoob']
     
    print (list)            # 输出完整列表
    print (list[0])         # 输出列表第一个元素
    print (list[1:3])       # 从第二个开始输出到第三个元素
    print (list[2:])        # 输出从第三个元素开始的所有元素
    print (tinylist * 2)    # 输出两次列表
    print (list + tinylist) # 连接列表

以上实例输出结果::

    ['abcd', 786, 2.23, 'runoob', 70.2]
    abcd
    [786, 2.23]
    [2.23, 'runoob', 70.2]
    [123, 'runoob', 123, 'runoob']
    ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']

与Python字符串不一样的是，列表中的元素是可以改变的::

    >>>a = [1, 2, 3, 4, 5, 6]
    >>> a[0] = 9
    >>> a[2:5] = [13, 14, 15]
    >>> a
    [9, 2, 13, 14, 15, 6]
    >>> a[2:5] = []   # 将对应的元素值设置为 [] 
    >>> a
    [9, 2, 6]

List内置了有很多方法，例如append()、pop()等等，这在后面会讲到。

注意：
    1、List写在方括号之间，元素用逗号隔开。
    2、和字符串一样，list可以被索引和切片。
    3、List可以使用+操作符进行拼接。
    4、List中的元素是可以改变的。

Tuple（元组）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

元组中的元素类型也可以不相同::

    #!/usr/bin/python3
     
    tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
    tinytuple = (123, 'runoob')
     
    print (tuple)             # 输出完整元组
    print (tuple[0])          # 输出元组的第一个元素
    print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
    print (tuple[2:])         # 输出从第三个元素开始的所有元素
    print (tinytuple * 2)     # 输出两次元组
    print (tuple + tinytuple) # 连接元组

以上实例输出结果::

    ('abcd', 786, 2.23, 'runoob', 70.2)
    abcd
    (786, 2.23)
    (2.23, 'runoob', 70.2)
    (123, 'runoob', 123, 'runoob')
    ('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob')

元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。

其实，可以把字符串看作一种特殊的元组::

    >>>tup = (1, 2, 3, 4, 5, 6)
    >>> print(tup[0])
    1
    >>> print(tup[1:5])
    (2, 3, 4, 5)
    >>> tup[0] = 11  # 修改元组元素的操作是非法的
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment
    >>>

虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。

构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则::

    tup1 = ()    # 空元组
    tup2 = (20,) # 一个元素，需要在元素后添加逗号
    string、list和tuple都属于sequence（序列）。

注意：
    1、与字符串一样，元组的元素不能修改。
    2、元组也可以被索引和切片，方法一样。
    3、注意构造包含0或1个元素的元组的特殊语法规则。
    4、元组也可以使用+操作符进行拼接。

Set（集合）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式::

    parame = {value01,value02,...}
    或者
    set(value)

    #!/usr/bin/python3
     
    student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
     
    print(student)   # 输出集合，重复的元素被自动去掉
     
    # 成员测试
    if 'Rose' in student :
        print('Rose 在集合中')
    else :
        print('Rose 不在集合中')
     
     
    # set可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')
     
    print(a)
     
    print(a - b)     # a和b的差集
     
    print(a | b)     # a和b的并集
     
    print(a & b)     # a和b的交集
     
    print(a ^ b)     # a和b中不同时存在的元素

以上实例输出结果::

    {'Mary', 'Jim', 'Rose', 'Jack', 'Tom'}
    Rose 在集合中
    {'b', 'a', 'c', 'r', 'd'}
    {'b', 'd', 'r'}
    {'l', 'r', 'a', 'c', 'z', 'm', 'b', 'd'}
    {'a', 'c'}
    {'l', 'r', 'z', 'm', 'b', 'd'}

Dictionary（字典）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的::

    #!/usr/bin/python3
     
    dict = {}
    dict['one'] = "1 - 菜鸟教程"
    dict[2]     = "2 - 菜鸟工具"
     
    tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
     
     
    print (dict['one'])       # 输出键为 'one' 的值
    print (dict[2])           # 输出键为 2 的值
    print (tinydict)          # 输出完整的字典
    print (tinydict.keys())   # 输出所有键
    print (tinydict.values()) # 输出所有值

以上实例输出结果：
    1 - 菜鸟教程
    2 - 菜鸟工具

::

    {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
    dict_keys(['name', 'code', 'site'])
    dict_values(['runoob', 1, 'www.runoob.com'])

构造函数 dict() 可以直接从键值对序列中构建字典如下::

    >>>dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
    {'Taobao': 3, 'Runoob': 1, 'Google': 2}
     
    >>> {x: x**2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}
     
    >>> dict(Runoob=1, Google=2, Taobao=3)
    {'Runoob': 1, 'Google': 2, 'Taobao': 3}

另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。

注意：
    1、字典是一种映射类型，它的元素是键值对。
    2、字典的关键字必须为不可变类型，且不能重复。
    3、创建空字典使用 { }。

Python数据类型转换
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

函数  描述
 - int(x [,base]) 将x转换为一个整数
 - float(x) 将x转换到一个浮点数
 - complex(real [,imag]) 创建一个复数
 - str(x) 将对象 x 转换为字符串
 - repr(x) 将对象 x 转换为表达式字符串
 - eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象
 - tuple(s) 将序列 s 转换为一个元组
 - list(s) 将序列 s 转换为一个列表
 - set(s) 转换为可变集合
 - dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
 - frozenset(s) 转换为不可变集合
 - chr(x)  将一个整数转换为一个字符
 - ord(x)  将一个字符转换为它的整数值
 - hex(x)  将一个整数转换为一个十六进制字符串
 - oct(x)  将一个整数转换为一个八进制字符串




Python3 注释
---------------------------------------------------------------------

确保对模块, 函数, 方法和行内注释使用正确的风格

Python中的注释有单行注释和多行注释：

Python中单行注释以 # 开头，例如::

    # 这是一个注释
    print("Hello, World!") 

多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来，例如:

1、单引号（'''）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    #!/usr/bin/python3 
    '''
    这是多行注释，用三个单引号
    这是多行注释，用三个单引号 
    这是多行注释，用三个单引号
    '''
    print("Hello, World!") 

2、双引号（"""）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/python3 
    """
    这是多行注释，用三个双引号
    这是多行注释，用三个双引号 
    这是多行注释，用三个双引号
    """
    print("Hello, World!") 












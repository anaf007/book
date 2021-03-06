第一章、基本概念
=======================================================================

本章将建立汇编语言编程的一些核心概念。比如，汇编语言是如何适应各种语言和应用程序的。本章还将介绍虚拟机概念，它在理解软件与硬件层之间的关系时非常重要。本章还用大量的篇幅说明二进制和十六进制的数制系统，展示如何执行转换和基本的算术运算。本章的最后将介绍基础逻辑操作（AND、OR和NOT），后续章节将证明这些操作是很重要的。

1.1、欢迎来到汇编语言的世界
---------------------------------------------------------------------

本书主要介绍与运行 Microsoft Windows Intel和AMD处理器相兼容的微处理器编程。

配合本书应使用Microsoft宏汇编器(称为MASM)的最新版本。Microsoft Studio的大多数版本（专业版，旗舰版，精简版）都包含MASM。

在运行 Microsoft Windows 的X86系统中，有一些其他有名的汇编器包括：TASM、NASM、MAsm32。GAS（GNU汇编器）和NASM是两种基于 Linux的汇编器。在这些汇编器中，NASM的语法与MASM的最相似。

汇编语言是最古老的编程语言，在所有的语言中，它与原生机器语言最为接近。它能直接访问计算机硬件，要求用户了解计算机架构和操作系统。

本书有助于学习计算机体系结构、机器语言和底层编程的基本原理。读者可以学到足够的汇编语言，来测试其掌握的当今使用最广泛的微处理器系列的知识。

如果读者计划成为C或C++开发者，就需要理解内存、地址和指令是如何在底层工作的。在高级语言层次上，很多编程错误不容易被识别。因此，程序员经常会发现需要“深入”到程序内部，才能找出程序不工作的原因。

1.1.1、读者可能会问的问题
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**需要怎样的背景知识？** 在阅读本书之前，读者至少使用过一种结构化高级语言进行编如ava、C、 Python或C++需要了解如何使用正F语句、数组和函数来解决编程问题。

**什么是汇编器和链接器？** 汇编器是一种工具程序，用于将汇编语言源程序转换为机器语言。连接器也是一种工具程序员，他把汇编器生成的单个文件组合为一个可执行文件。还有一个相关的工具，称为调试器（ bugger）使程序员可以在程序运行时，单步执行程序并检查寄存器和内存状态。

**要哪些硬件和软件？** 一台运行32位或64位 Microsoft Windows系统的计算机，并已安装了近期版本的 Microsoft Visual Studio。

MASM能创建那些类型的程序？
 - 32位保护模式（32-Bite-Protected-Mode）:32位保护模式程序运行于所有的32位和64位版本的 Microsoft Windows系统。它们通常比实模式程序更容易编写和理解。从现在开始，将其简称为32位模式。
 - 64位模式（64-Bit-Mode）64位程序运行与所有的64位版本的Microsoft Windows 系统。
 - 16位实地址模式（116-Bit6- Real-Address Mode）16位程序运行于32位版本Windows 和嵌入式系统，由于64位Windows不支持这类程序，本书只在14-17章讨论这种模式。这些章节是电子版的。可以从出版社网站获取。

能学到什么？本书将使读者更好地了解数据表示、调试编程和硬件控制。读者将学到:
 - x86处理器应用的计算机体系结构的基本原理。
 - 基本布尔逻辑，以及它是如何应用于编程和计算机硬件的。
 - 使用保护模式和虚模式时，x86处理器如何管理内存。
 - 高级语言编译器（如C++）如何将其语句转换为汇编语言和原生机器代码。
 - 高级语言如何在机器级实现算术表达式、循环和逻辑结构。
 - 数据表示，包括有符号和无符号整数、实数以及字符数据。
 - 如何在机器级调试程序。使用C和C++语言时，它们生成的是原生机器代码，这个技术显得至关重要。
 - 应用程序如何通过中断处理程序和系统调用与计算机操作系统进行通信。
 - 如何连接汇编语言代码与C++程序。
 - 如何创建汇编语言应用程序。

**汇编语言与机器语言有什么关系？** 机器语言（ machine language）是一种数字语言，专门设计成能被计算机处理器（CPU）理解。所有x86处理器都理解共同的机器语言。江编语言（ assembly language）包含用短助记符如ADD、MOV、SUB和CALL书写的语句。汇编语言与机器语言是一对一（ one-to-one）的关系:每一条汇编语言指令对应一条机器语言指令。

**C++和Java与汇编语言有什么关系？** 高级语言如 Python、C++和Java与汇编语言和机器语言的关系是一对多（one-to-many）。比如，C++的一条语句就会扩展为多条汇编指令或机器指令。大多数人无法阅读原始机器代码，因此，本书探讨的是与之最接近的汇编语言。例如、下面的C++代码进行了两个算术操作，并将结果赋给一个变量。假设X和Y是整数

::

    int Y;
    int X = (Y+4)*3;

与之等价的汇编语言程序如下所示。这种转换需要多条语句，因为每条汇编语句只对应条机器指令::
    
    mov eax, Y  ;Y送入EAX寄存器
    add eax, 4  ;EAX存器内容加4
    mov ebx, 3  ;3送入EBX寄存器
    imul ebx    ;EAX与EBX相乘
    mov X,eax   ;EAX的值送入X

（寄存器（ register）是CPU中被命名的存储位置，用于保存操作的中间结果。）这个例子的重点不是说明C++与汇编语言哪个更好，而是展示它们的关系。


**汇编语言可移植吗？** 一种语言，如果它的源程序能够在各种各样的计算机系统中进行编译和运行，那么这种语言被称为是可移植的（ portable）。例如，一个C++程序，除非需要特别引用某种操作系统的库函数，否则它就几乎可以在任何一台计算机上编译和运行。Java语言的一大特点就是，其编译好的程序几乎能在所有计算机系统中运行。

汇编语言不是可移植的，因为它是为特定处理器系列设计的。目前广泛使用的有多种不同的汇编语言，每一种都基于ー个处理器系列。对于ー些广为人知的处理器系列如Mola［468x00、x86、 SUN Sparc、Vax和IBM-370，汇编语言指令会直接与该计算机体系结构相匹配，或者在执行时用一种被称为微代码解释器（ microcode interpreter）的处理器内置程序来进行转换。

**为什么要学习汇编语言？** 如果对学习汇编语言还心存疑虑，考虑一下这些观点
 - 如果是学习计算机工程，那么很可能会被要求写嵌入式（ embedded）程序。嵌入式程序是指一些存放在专用设备中小容量存储器内的短程序，这些专用设备包括:电话、汽车燃油和点火系统、空调控制系统、安全系统、数据采集仪器、显卡、声卡、硬盘驱动器、调制解调器和打印机。由于汇编语言占用内存少，因此它是编写嵌入式程序的理想工具。
 - 处理仿真和硬件监控的实时应用程序要求精确定时和响应。高级语言不会让程序员对编译器生成的机器代码进行精确控制。汇编语言则允许程序员精确指定程序的可执行代码。
 - 电脑游戏要求软件在减少代码大小和加快执行速度方面进行高度优化。就针对一个目标系统编写能够充分利用其硬件特性的代码而言，游戏程序员都是专家。他们经常选择汇编语言作为工具，因为汇编语言允许直接访问计算机硬件，所以，为了提高速度可以对代码进行手工优化。
 - 汇编语言有助于形成对计算机硬件、操作系统和应用程序之间交互的全面理解。使用汇编语言，可以运用并检验从计算机体系结构和操作系统课程中获得的理论知识。
 - 一些高级语言对其数据表示进行了抽象，这使得它们在执行底层任务时显得有些不方便，如位控制。在这种情况下，程序员常常会调用使用汇编语言编写的子程序来完成他们的任务。
 - 硬件制造商为其销售的设备创建设备驱动程序。设备驱动程序（device driver）是一种程序，它把通用操作系统指令转换为对硬件细节的具体引用。比如，打印机制造商就为他们销售的每一种型号都创建了一种不同的 MS-Windows设备驱动程序。通常，这些设备驱动程序包含了大量的汇编语言代码。

 **汇编语言有规则吗？** 大多数汇编语言规则都是以目标处理器及其机器语言的物理局限性为基础的。比如，CPU要求两个指令操作数的大小相同。与C++或Java相比，汇编语言的规则较少，因为，前者是用语法规则来减少意外的逻辑错误，而这是以限制底层数据访问为代价的。汇编语言程序员可以很容易地绕过高级语言的限制性特征。例如，Java就不允许访问特定的内存地址。程序员可以使用JNI（java Native Interface）类来调用C函数绕过这个限制，可结果程序不容易维护。反之，汇编语言可以访问所有的内存地址。但这种自由的代价也很高:汇编语言程序员需要花费大量的时间进行调试。

1.1.2、汇编语言的应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

早期在编程时，大多数应用程序部分或全部用汇编语言编写。它们不得不适应小内存，并尽可能在慢速处理器上有效运行。随着内存容量越来越大，以及处理器速度急速提高，程序变得越来越复杂。程序员也转向高级语言如C、 FORTRAN COBOL，这些语言具有很多结构化能力。最近， Python、C++、c＃和Java等面向对象语言已经能够编写含数百万行代码的复杂程序了。

很少能看到完全用汇编语言编写的大型应用程序，因为它们需要花费大量的时间进行编写和维护。不过，汇编语言可以用于优化应用程序的部分代码来提升速度，或用于访问计算机硬件。表1-1比较了汇编语言和高级语言对各种应用类型的适应性。

.. list-table:: 汇编语言与高级语言的比较
    :header-rows: 1

    * - 应用类型
      - 高级语言
      - 汇编语言
    * - 商业或科学应用程序，为单一的中型或大型平台编写
      - 规范结构使其易于组织和维护大量代码
      - 最小规范结构，因此必须由具有 不同程度经验的程序员来维护结构。这导致对已有代码的维护困难
    * - 硬件设备驱动程序
      - 语言不一定提供对硬件的直接访问。
      - 对硬件的访问直接且简单。当程序较短且文档良好时易于维护
    * - 为多个平台（不同的操作系统）编写的商业或科学应用程序
      - 通常可移植。在每个目标操作系统上，源程序只做少量修改就能重新编译
      - 需要为每个平台单独重新编写代码，每个汇编器都使用不同的语法，维护困难
    * - 需要直接访问硬件的嵌人式系统和电脑游戏
      - 可能生成很大的可执行文件，以至于超出设备的内存容量
      - 理想，因为可执行代码小，运行速度快

C和C++语言具有一个独特的特性，能够在高级结构和底层细节之间进行平衡。直接访问硬件是可能的，但是完全不可移植。大多数C和C++编译器都允许在其代码中嵌人汇编语句，以提供对硬件细节的访问。

1.1.3、本节回顾
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - 汇编器和链接器是如何一起工作的？
 - 学习汇编语言如何能提高你对操作系统的理解？
 - 比较高级语言和机器语言时，一对多关系是什么意思？
 - 解释编程语言中的可移植性概念。
 - x86处理器的汇编语言与Vax或Motorola8x00等机器的汇编语言是一样的吗？ 
 - 举一个嵌入式系统应用程序的例子。
 - 什么是设备驱动程序？
 - 汇编语言和C/C++语言中的指针变量类型检查，哪一个更强（更严格）？
 - 给出两种应用类型，与高级语言相比，它们更适合使用汇编语言。
 - 编写程序来直接访问打印机端口时，为什么高级语言不是理想工具？
 - 为什么汇编语言不常用于编写大型应用程序？
 - 挑战:参考本章前面给出的例子，将下述C++表达式转换为汇编语言: X = (Y*4) +3 

1.2、虚拟机的概念
---------------------------------------------------------------------

虚拟机概念是一种说明计算机硬件和软件关系的有效方法。在安德鲁·塔嫩鲍姆中可以找到对这个模型广为人知的解释。要说明这个概念，先从计算机的最基本功能开始，即执行程序。

计算机通常可以执行用其原生机器语言编写的程序。这种语言中的每一条指令都简单到可以用相对少量的电子电路来执行。了简便，称这种语言为LO。

由于LO极其详细，并且只由数字组成，因此，程序员用其编写程序就非常困难。如果能够构造一种较易使用的新语言L1，那么就可以用L1编写程序。有两种实现方法:

 - **解释（Interpretation）:** 运行L1程序时，它的每一条指令都由一个用LO语言编写的程序进行译码和执行。L1程序可以立即开始运行，但是在执行之前，必须对每条指令进行译码。
 - **翻译（Translation）:** 由一个专门设计的L程序将整个L1程序转换为L0程序。然后，得到的L0程序就可以直接在计算机硬件上执行。



1.3、数据表示
---------------------------------------------------------------------

汇编语言程序员处理的是物理级数据，因此他们必须善于检查内存和寄存器。

1.3.1、二进制整数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

计算机以电子电荷集合的形式在内存中保存指令和数据。用数字来表示这些内容就需要系统能够适应开关的概念。二进制数用2个数字作基础，其中每一个二进制数字不是0就是1.位自右向左，从0开始顺序增量编号。左边的位称为最高有效位-MSB，右边的位称为最低有效位-LSB

二进制整数可以是有符号的，也可以是无符号的。有符号整数又分为正数和负数。

1.3.2、二进制加法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

两个二进制数相加时，是位对位处理的，从最低的以为(右边)开始，依序将每一个对位进行加法运算。

1.3.3、整数存储大小
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在x86计算机中，所有数据存储的基本单位都是字节（byte）一个字节由8位，其他的存储单位还有字word、双子DWORD、四字qword，一个字=2个字节 byte

1.3.4、十六进制整数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

大的二进制读起来很麻烦，因此十六进制数字就提供同了简单的方式来表示二进制数据。十六进制整数中的1个数字就表示了4位二进制，两个十六进制数字就能表示一个字节。一个十六进制数字表示的范围是十进制数0到15.所以字母A到F代表十进制数10-15

1.3.5、十六进制加法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

调试工具程序 通常用十六进制表示内存地址。为了定位一个新地址常常需要将两个地址相加。十六进制加法与十进制加法是一样的，只需要更换基数就可以了。

1.3.6、有符号二进制整数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

有符号二进制整数有正数和负数。在x86处理器中，msb表示的是符号位：0表示正数。1表示负数

这里补码概念不做多解释，需要阅读其他书籍学习。

1.3.7、二进制减法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果采用与十进制减法相同的方法，那么从一个较大的二进制数中减去一个较小的无符号二进制数就很容易了。

1.3.8、字符存储
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

计算机使用的是字符集，将字符映射为整数。
 - ANSI字符集：美国国家标准协会定了了8位字符集来表示多大256个字符。前128个字符对应标准美国键盘上的字母和符号。后128位字符表示特殊字符。window早期版本使用ANSI字符集。
 - Unicode标准：当前，计算机必须能表示计算机软件中世界中各种各样的语言，因此Unicode被创建出来，用于提供一种定义文字和符号的通用方法，他定了数字代码，定义的对象为文字、符号以及所有主要语言中使用的标点符号。代码特点转换可现实字符的格式有三种:
   UTF-8用于html，与ascii有相同的字节数值
   UTF-16用于结余使用内存与高校访问字符相互平衡的环境中。
   UTF-32用于不考虑空间，但需要固定宽度字符的环境中，每个字符都有32位的编码。

 - ASCII字符串 有一个或多个字符的序列被称为字符串。更具体的说，一个ASCII字符串是保存在内存中的，包含了ASCII代码的连续字节。有对应的ASCII表


1.3.9、本节回顾
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
略

1.4、布尔表达式
---------------------------------------------------------------------

与或非 not  and or 

1.4.1、布尔函数真值表
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

略

1.4.2、本节回顾
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

略

1.5、本章小结
---------------------------------------------------------------------

暂略

1.6、关键术语
---------------------------------------------------------------------

略

1.7、复习题和练习
---------------------------------------------------------------------

略

1.7.1、简答题
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

略

1.7.2、算法基础
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

略





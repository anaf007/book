第二章：numpy基础
==============================================

完成时间：2018-11-07

本章涵盖知识：
 - 数据类型
 - 数组类型
 - 类型转换
 - 创建数组
 - 数组切片
 - 改变维度

numpy中的ndarray是一个多维数组对象，该对象由两部分组成：
 - 实际的数据
 - 描述这些数据的元数据

创建多维数组::

    array([arange(2),arange(2)]) 

ndarray对象的维度属性是以 元祖  python tuple对象存储的。

numpy数据类型：
 - bool     ：布尔
 - inti     ：平台决定精度的整数
 - int8     ：整数 
 - int16    ：整数 
 - int32    ：整数 
 - int64    ：整数 
 - uint8    ：无符号整数 
 - uint16   ：无符号整数 
 - uint32   ：无符号整数 
 - uint64   ：无符号整数 
 - float16  ：半精度浮点数
 - float32  ：单精度浮点数
 - float64或float：双精度浮点数
 - complex64    ：复数
 - complex128或complex   ：复数

数据类型对象时numpy.dtype类的实例。numpy数组中的每一个元素均为相同的数据类型。
数据类型对象可以给出单个数组元素在内存中占用的字节数。即dtype类的itemsize属性::

    a.dtype.itemsize

字符编码：
 - i：整数
 - u：无符号整数
 - f：单精度浮点数
 - d：双精度浮点数
 - b：布尔值
 - D：复数
 - S：字符串
 - U：unicode字符串
 - V：void空

创建单精度浮点数数组::

    arange(7,dtype='f') 

获取数据类型的字符编码::

    t = dtype('float64')
    t.char
    >>d
    #对应的数据类型
    t.type

一维数组切片::

    a = arange(9)
    a[3:7]
    #下标0-7，步长为2
    a[:7:2]

创建一个数组并改变其维度::

    arange(24).reshape(2,3,4)

获取维度::

    b.shape

多维数组的切片：可用逗号隔开切片


展平维度：转换为一维数组::

    #1.ravel
    b.ravel()

    #2.flatten,与上面ravel不同的是，这里会请求内存来保存结果，上面只是返回数组的一个视图。
    b.flatten()

    #3.用元祖设置维度
    b.shape = (6,4)

    #4.transpose 在线性代数中，转置矩阵是很常见的操作。
    b.transpose()

    #5.resize和reshape函数功能一样，但是resize会直接修改所操作的数组
    b.resize((2,12))


组合数组::

    hstack()    

    concatenate()

    #垂直组合：

    vstack()
    #concatenate的axis设置为0也是垂直组合。
    concatenate((a,b),axis=0)

    #深度组合
    dstack()

    #列组合
    column_stack((a,b))

    #行组合

    row_stack()

分割数组::

    #1.水平分割
    hsplit()    

    #2.垂直分割
    vsplit()

    #3.深度分割
    dsplit()

数组属性：
 - ndim属性：给出数组的未读 数轴的个数
 - size属性：数组元素的总个数
 - itemsize：给出数组中的元素在内存中所占的字节数
 - nbytes：数组所占的存储空间
 - T属性：和transpose函数一样
 - 对于一维数组，T属性就是原数组
 - 复数的虚部是用j表示
 - real属性给出复数数组的实部
 - imag属性给出复数数组的虚部

numpy数组转换python数组::

    tolist()









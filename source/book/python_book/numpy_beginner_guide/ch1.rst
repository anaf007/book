第一章：numpy快速入门
==============================================

完成时间：2018-11-07

安装::

    pip install numpy

标量：普通的数

矩阵：多维数组

向量（一维数组）加法:

python代码实现::

    def pythonsum(n):
        a = range(n)
        b = range(n)
        c = []

        for i in range(len(a)):
            a[i] = i ** 2
            b[i] = i ** 3
            c.append(a[i]+b[i])

        return c

numpy实现::

    def numpysum(n):

        a = numpy.arange(n) ** 2
        b = numpy.arange(n) ** 3

        c = a +b

        return c

numpy等价的代码比纯python的运行速度要快得多。        











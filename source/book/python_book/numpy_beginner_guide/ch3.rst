第三章：常用函数
============================

完成时间：2018-11-07

创建方阵::

    np.eye(2)

读取csv文件::
    
    c,v = np.loadtext('data.csv',delimiter=',',usecols=(6,7),unpack=True)    
    #读取文件设置分隔符为逗号，usecols参数设置为一个元祖

需要理解加权平均的含义

``加权`` 平均价格::

    average(c,weights=v)

算数平均值::

    np.mean(c)

时间加权平均值::
    
    t = np.arange(len(c))    
    np.average(c,weights=t)

找到最大、最小值::

    np.max(c)    
    np.min(c)

取值范围，最大最小的差值（极差）::

    np.ptp(c)    

中位数::

    np.median(c)    

    #排序：
    np.msort()

需要理解 ``方差`` 意思：

    方差 是指各个数据与所有数据算数平均数的离差平方和除以数据个数所得到的值

计算 ``方差`` ::    

    np.var(c)

计算标准差::

    np.std()

结果对比::

    np.diff(np.log(c))    

创建包含5个元素的数组::

    np.zeros(5)    

::

    np.onew(N)
    #创建一个长度为iN的元素均初始化为1的数组

exp函数计算数组每个元素的指数::

    np.exp(x)


理解 ``布林带``

数组的修建和压缩：

chip方法返回一个修建过的数组    

compress方法返回一个根据给定条件筛选后的数组

计算乘积：

prod方法计算数组中所有元素的乘积









第七章：方法和装饰器
================================================
装饰器是修改函数的一种便捷方式

创建装饰器::

    def identity(f):
        return f

    @identity
    def foo():
        return "foo"

    #过程和下面的类似
    def foo():
        return "foo"

    foo = identity(foo)

静态方法：@staticmethod

类方法：@classmethod


还需要了解super的用法
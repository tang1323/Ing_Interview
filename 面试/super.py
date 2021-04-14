
# class A(object):
#     def __init__(self):
#         print('a')
#
#
# class B(A):
#     def __init__(self):
#         super(B, self).__init__()
#         print('b')
#
#
# b = B()


# 当一个类继承多个类时，问题就复杂起来了，请看下例：


# class A(object):
#     def __init__(self):
#         print('a')
#
#
# class B(object):
#     def __init__(self):
#         print('b')
#
#
# class C(A, B):
#     def __init__(self):
#         super(C, self).__init__()
#         print('c')
#
#
# c = C()


# 结果输出a, c嘛。没错！但是如果C类想同时调用A与B的__init__()呢？有童鞋就要说了，我显示调用不就OK了嘛？

# class A(object):
#     def __init__(self):
#         print('a')
#
#
# class B(object):
#     def __init__(self):
#         print('b')
#
#
# class C(A, B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print('c')


# 这样的确是可以输出abc，但还不够好，因为还没有调用super，
# 调用super的好处是当父类的名字修改时，其继承类不用修改调用方法
# c = C()


# 以下就是调用super（）方法， 还有显示abc
class A(object):
    def __init__(self):
        super(A, self).__init__()
        print('a')


class B(object):
    def __init__(self):
        super(B, self).__init__()
        print('b')


class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print('c')


print(C.mro())
c = C()

"""这里就要用上面的mro()输出来解释了。MRO全称Method Resolution Order,  
就是用来定义继承方法的调用顺序，自Python2.3以来，
MRO采用广度优先（区别于深度优先）的规则定义。
按广度优先的规则，出来的顺序就是："""

"""而每次调用super()则是，调用MRO中下一个函数。上面的例子中：
super(C, self)则指向MRO中的下一个类(A), 于是调用A的init --> 在A的init中，
又调用了super()，于是调用MRO中的下一个函数(B)  -->  B调用下一个(object), 
object啥也不干  -->  返回B中，print('b')  -->  返回A中，print('a')  -->  返回C中，
print('c')。"""











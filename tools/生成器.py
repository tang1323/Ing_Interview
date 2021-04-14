

"""简单一句话：我又想要得到庞大的数据，又想让它占用空间少，那就用生成器！"""
# 1.第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
# g = (x * x for x in range(10))
# print(type(g))
# print(g)
# ----------------------------------------------------


# 生成器
def myGen():
    yield 1
    yield 2
    yield 3
    return 4


def myfun():
    return 5


"""
生成器的特点：是可以停止的函数
我们只能用一个for循环才能把mygen()全部yield拿出来

"""
# for data in myGen():
#     print(data)

"""
是可以停止的函数，它只会运行到第一个yield
不像其他函数那样，会从上向下运行完
所以它会停止。当它再次运行时，会接着从下一个yield的地方再次取数据运行
或者调用它，用next()去获取

"""
# mygen = myGen()
# print(next(mygen))
# print(next(mygen))
# print(next(mygen))


# ---------------------------------
# 使用yield生成器
# def gen(n):
#     for i in range(n):
#         yield i**2
#         # yield是返回这个数据，然后下次函数再进入的时候，会从yield开始继续执行
#
#
# for i in gen(5):
#     print(i, " ", end="")


# ---------------------------------------------
def yield_test(n):
    for i in range(n):
        yield call(i)       # 在这里会yield到call，再yield到计算的结果，最后才执行到print("i=", i)然后不会立马执行print("i=",i)
        print("i=", i)
    print("Done.")
#
#
def call(i):
    return i*2


for i in yield_test(5):
    print("计算得出的结果", i,)
#  理解的关键在于：下次迭代时，代码从yield的下一条语句开始执行。


# -----------------------------------------------------------

"""什么是生成器？

生成器仅仅保存了一套生成数值的算法，
并且没有让这个算法现在就开始执行，
而是我什么时候调它，它什么时候开始计算一个新的值，并给你返回。"""


# def count_down(n):
#     while n >= 0:
#         newn = yield n
#         print('newn', newn)
#         if newn:
#             print('if')
#             n = newn
#             print('n =', n)
#         else:
#             n -= 1
#
#
# cd = count_down(5)
# for i in cd:
#     print(i, ',')
#     if i == 5:
#         cd.send(3)
















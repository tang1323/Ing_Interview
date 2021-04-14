
def dec(f):
    n = 3   # 执行第一步的时候n=3

    def wrapper(*args, **kw):   # 执行第3步,拿到2会跑wrapper方法和2*n=6
        return f(*args, **kw) * n   # 拿到2会跑wrapper方法和2*n=6
    return wrapper  # 第4步返回到foo方法下拿得到的6与2相乘


@dec    # 执行第一步，跑到dec方法下
def foo(n):
    return n * 2    # 第5步：和6相乘，所以2*6=12


print(foo(2))   # 执行第二步，跑到foo方法下，但是没有立即执行里面的内容，拿到2会跑wrapper方法和2*n=6

# -----------------------------------------------------------------

# def outer(a, b):
#     def inner(c):
#         return a*b/c
#     return inner
#
#
# o1 = outer(3, 4)
# o2 = outer(5, 6)
# print(o1(2))        # 6.0
# print(outer(3, 4)(2))   # 6.0
# print(o2(3))        # 10.0
# print(outer(5, 6)(3))   # 10.0
"""
函数inner与变量a,b构成闭包。
在创建闭包的时候，我们通过outer的参数a,b说明了这两个变量的取值，
根据传递参数的不同，就可以获得不同表现函数。所以闭包也具有提高代码可复用性的作用。
"""
# -------------------------------------------------------------------------------

# 装饰器
"""
简单来说python装饰器就是用于拓展原来函数功能的一种函数，
这个函数的特殊之处在于它的返回值也是一个函数，
使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能
"""


# 这是未使用装饰器
# def set_func(func):
#     print("call_func外部")
#
#     def call_func(*args, **kwargs):
#         print("call_func执行了")
#         return func(*args, **kwargs)    # 拆包
#     return call_func
#
#
# def test(*args, **kwargs):
#     print("test函数执行了----->%d" % args)
#     return "test返回值"
#
#
# test = set_func(test)
# t = test(10)
# print("这是test返回的t：", t)
"""
输出
call_func外部
call_func执行了
test函数执行了----->10
这是test返回的t：test返回值
"""


# --------------------------------------------------
# 使用一个装饰器
# def set_func(func):
#     print("call_func外部")
#
#     def call_func(*args, **kwargs):
#         print("call_func执行了")
#         return func(*args, **kwargs)   # 拆包
#     return call_func
#
#
# @set_func
# def test(value, *args, **kwargs):
#     print("test函数执行了----->%d" % value)
#     return "test返回值"
#
#
# t = test(10)
# print("这是test返回的t：", t)
# 输出
"""
call_func外部
call_func执行了
test函数执行了----->10
这是test返回的t：test返回值
"""
# 与上一段代码执行结果相同，改动只是去掉了原来的test = set_func(test)，而在一个test函数前加上@set_func，这便是装饰器

# ----------------------------------------------------------------


# 这是使用两个装饰器的
# def set_func1(func):
#     print("***装饰器1开始装饰***")
#
#     def call_func(*args, **kwargs):
#         print("***装饰器1的功能***")
#         return func(*args, **kwargs)
#     return call_func
#
#
# def set_func2(func):
#     print("***装饰器2开始装饰***")
#
#     def call_func(*args, **kwargs):
#         print("***装饰器2的功能***")
#         return func(*args, **kwargs)
#     return call_func
#
#
# @set_func1
# @set_func2
# def test(*args, **kwargs):
#     print("test1运行.........")
#     return "test的返回值"
#
#
# t = test()
# print("这是test返回的t：", t)

"""
输出结果：
***装饰器2开始装饰***
***装饰器1开始装饰***
***装饰器1的功能***
***装饰器2的功能***
test1运行.........
这是test返回的t：test的返回值
"""


"""
所以在一个函数被多个装饰器装饰时（自上而下看装饰器）：

装饰器装饰的顺序：最下----------->最上
装饰器功能执行的顺序：最上---------->最下
"""



















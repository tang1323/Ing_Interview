"""闭包"""


# 举例1
def make_adder(addend):
    def adder(augend):
        return augend + addend      # addend是adder的变量，也是外部函数的参数
    return adder


p = make_adder(23)      # 这里先进入外部函数
q = make_adder(44)      # 这里先进入外部函数


print(p(100))       # 这里是进入内部函数，123
print(q(100))       # 这里是进入内部函数，144


# --------------------------------------------------
# 举例2
# def hellocounter(name):
#     count = [0]
#     def counter():
#         count[0] += 1
#         print("Hello", name, ",", str(count[0]) + 'access!!')
#     return counter
#
#
# hello = hellocounter("ma6174")
# hello()
# hello()
# hello()


# --------------------------------------------------
"""
一般在函数结束时，会释放临时变量,
但在闭包中，由于外函数的临时变量在内函数中用到，
此时外函数会把临时变量与内函数绑定到一起，这样虽然外函数结束了，
但调用内函数时依旧能够使用临时变量，即闭包外层的参数可以在内存中进行保留
"""


# --------------------------------------------------
# 如果想要在内函数中修改外函数的值，需要使用 nonlocal 关键字声明变量
# 举例3
# def func(a, b):
#     def line(x):
#         nonlocal a
#         a = 3
#         return a * x - b
#
#     return line
#
#
# line = func(2, 3)   # 先运行到外函数
# print(line(5))      # 再运行内函数里


# -----------------------下面就是使用闭包的方法----------------------
# def 外层函数(参数)：
#     def 内层函数():
#         print("内层函数执行", 参数)
#     return 内层函数
#
#
# 内层函数的引用 = 外层函数("传入参数")
# 内层函数的引用()




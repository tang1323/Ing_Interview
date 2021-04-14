

# 简述面向对象中__new__和__init__区别
# class Bike:
#     def __init__(self, newWheelNum, newColor):
#         self.WheelNum = newWheelNum
#         self.color = newColor
#
#     def move(self):
#         print('车会飞')
#
#
# BM = Bike(2, 'green')
# print('车的颜色是:{}'.format(BM.color))
# print('车轮子数量为：{}'.format(BM.WheelNum))


# class A(object):
#     def __init__(self):
#         print("这是init方法", self)#__init__有一个参数self，就是这个__new__返回的实例,__init__不需要返回值
#
#     def __new__(cls):
#         print("这里cls的ID", id(cls))
#         print("这是 new 方法", object.__new__(cls))
#
#         """
#         通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例,
#         如果__new__创建的是当前类的实例，会自动调用__init__函数,
#          __new__必须要有返回值
#         """
#         return object.__new__(cls)
#
#
# A()
# print("这是类A的ID ", id(A))


# 13.列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]

# lis = [1, 2, 3, 4, 5]
#
#
# def fn(x):
#     return x**2
#
#
# res = map(fn, lis)
#
# # print(list(res))
#
# result = [i for i in res if i > 10]
#
# print(result)

# 2.如果有if条件语句,for遍历后紧跟着进行条件判断.

# for d in range(6):
#     if d % 2 != 0:
#         print(d)
# 和上面的是一样的功能
# list_d = [d for d in range(6) if d % 2 != 0]
# print(list_d)

# ------------------------------------------------------


# 14、python中生成随机整数、随机小数、0--1之间小数方法
# 随机整数：random.randint(a,b),生成区间内的整数
# 随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数
# 0-1随机小数：random.random(),括号中不传参
# import random
# import numpy as np
# result = random.randint(10, 20)
# res = np.random.randn(5)
# ret = random.random()
# print("正整数", result)
# print("5个随机小数", res)
# print("0-1随机小数", ret)

# -----------------------------------------

# 16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的

# import re
# str = '<div class="nam">中国</div>'
# res = re.findall(r'<div class=".*">(.*?)</div>', str)
# print(res)

# ---------------------------
# a = 3
# assert(a > 1)
# print("断言成功，程序继续向下执行")
#
# b = 4
# assert(b > 7)
# print("断言失败， 程序报错")

# ------------------------------------------


# 21。列出python中可变数据类型和不可变数据类型，并简述原理
# 不可变数据类型：数值型、字符串型string和元组tuple
# a = 3
# b = 3
# print(id(a))
# print(id(b))


# 可变数据类型：列表list和字典dict；
# a = [1, 2]
# b = [1, 2]
# print(id(a))
# print(id(b))

# 22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"

# s = "ajldjlajfdljfddd"
# s = set(s)# set去重
# s = list(s)# ，去重转成list
# s.sort(reverse=False)# reverse=False是从小到大排
# res = "       ".join(s)
# print(res)

# ---------------------------------------------------------

# 23、用lambda函数实现两个数相乘

# sum = lambda a, b: a * b
# print(sum(5, 5))
# ---------------------------------------------------------

# 24、字典根据键从小到大排序
# dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
# lis = sorted(dic.items(), key=lambda i: i[0], reverse=False)
# print(lis)
# print(dict(lis))
"""
sort 与 sorted 区别：

1. sort 是应用在 list 上的方法，属于列表的成员方法，sorted 可以对所有可迭代的对象进行排序操作。
2. list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
3. sort使用方法为ls.sort()，而sorted使用方法为sorted(ls)。
"""

# ---------------------------------------------------------
# 25、利用collections库的Counter方法统计字符串每个单词出现的次数
# from collections import Counter
# a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# res = Counter(a)
# print(dict(res))
# print(res)



# ---------------------------------------------------------
# 26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，
# 用正则过滤掉英文和数字，最终输出"张三  深圳"

# import re
# a = "not 404 found 张三 99 深圳"
# list = a.split(" ")
# print(list)
# res = re.findall('\d+\.?\d*|[a-zA-Z+]', a)
# # res = re.findall('\d+|[a-zA-Z]+', a)
# print(res)
# for i in res:
#     if i in list:
#         list.remove(i)
#
# new_str = " ".join(list)
#
# print(new_str)

# ---------------------------------------------------------

# filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def fn(a):
#     return a % 2 == 1
#
#
# newlist = filter(fn, a)
# newlist = [i for i in newlist]
# print(newlist)


# ---------------------------------------------------------
# 28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2.如果有if条件语句,for遍历后紧跟着进行条件判断.
# res = [i for i in a if i % 2 == 1]
# print(res)

#  ---------------------------------------------------------

# 30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据

# a=(1)
# b=(1,)
# c=("1")
#
# print(type(a))
#
# print(type(b))
#
# print(type(c))

#  ---------------------------------------------------------

# 31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]

# list1 = [1, 5, 7, 9]
# list2 = [2, 2, 6, 8]
#
# list1.extend(list2)
# print(list1)
#
# list1.sort(reverse=False)
# res = sorted(list1, reverse=False)
#
# print(list1)



#  ---------------------------------------------------------
# 32、用python删除文件和用linux命令删除文件方法
#
# python：os.remove(文件名)
#
# linux:       rm  文件名

#  ---------------------------------------------------------

# 33、log日志中，我们需要用时间戳记录error,warning等的发生时间，
# 请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
# %H:%M:%S尽量大写
# import datetime
# a = str(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')) + '星期：' + str(datetime.datetime.now().isoweekday())
# print(a)


# ---------------------------------------------------------

# 35 、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
#
# pychart、matplotlib


# ---------------------------------------------------------

# 36、写一段自定义异常代码
#
# 自定义异常用raise抛出异常

# def fn():
#     try:
#         for i in range(5):
#             if i > 2:
#                 raise Exception("数字大于2了。重来吧，帅哥")
#             # else:
#             #     print("帅哥，你的数字小于4了")
#     except Exception as ret:
#         print(ret)
#
#
# fn()



# ---------------------------------------------------------
# 37、正则表达式匹配中，（.*）和（.*?）匹配区别？
#
# （.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
#
# （.*?）是非贪婪匹配，会把满足正则的尽可能少匹配

# s = "<a>哈哈</a><a>呵呵</a><a>你好</a>"
# import re
# res1 = re.match("<a>(.*)</a>", s)
# if res1:
#     print("是贪婪匹配", res1.group(1))
    # .*是贪婪匹配 哈哈</a><a>呵呵</a><a>你好,取所有的值
    # .*?是非贪婪匹配


# res2 = re.match("<a>(.*?)</a>", s)
# if res1:
#     print("是贪婪匹配", res1.group(1))
    # 只返回一个第一个哈哈

"""
(1)re.match用法是返回一个对象，要加上print(res1.group(1))
(2)re.findall是返回一个列表，里面包含很多东西，直接print(res1)
"""
# res1 = re.findall("<a>(.*)</a>", s)
# print("是贪婪匹配", res1)
# 是贪婪匹配 ['哈哈</a><a>呵呵</a><a>你好']

#
# res2 = re.findall("<a>(.*?)</a>", s)
# print("是非贪婪匹配", res2)
# 是非贪婪匹配 ['哈哈', '呵呵', '你好']


# ---------------------------------------------------------

# 39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
#
# 列表推导式的骚操作

# a = [[1,2],[3,4],[5,6]]
# x = [j for i in a for j in i]
# print(x)

# a = [[1,2],[3,4],[5,6]]
# import numpy as np
# b = np.array(a).flatten().tolist()
# print(b)


# ---------------------------------------------------------
# 40、x="abc",y="def",z=["d","e","f"],
# 分别求出x.join(y)和x.join(z)返回的结果

# x = "abc"
# y = "def"
# z = ["d","e","2"]
#
# m = x.join(y)
# n= x.join(z)
# print(m)
# print(n)


# ---------------------------------------------------------
















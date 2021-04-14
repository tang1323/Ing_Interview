

# 91、简述python引用计数机制
#
# python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，
# 其中标记-清除和分代回收主要是为了处理循环引用的难题。
#
# 引用计数算法
# 当有1个变量保存了对象的引用时，此对象的引用计数就会加1
# 当使用del删除变量指向的对象时，如果对象的引用计数不为1，
# 比如3，那么此时只会让这个引用计数减1，即变为2，当再次调用del时，
# 变为1，如果再调用1次del，此时会真的把对象进行删除
# import time
#
#
# class Animal(object):
#     def __init__(self, name):
#         print('__init__方法被调用')
#         self.__name__ = name
#
#     # 当对象被删除，会自动被调用
#     def __del__(self):
#         print("__del__方法被调用")
#         print("{}对象马上被 干 掉。。。。。。。。".format(self.__name__))
#
#
# cat = Animal("波斯猫")
# cat2 = cat
# cat3 = cat
#
# print(id(cat), id(cat2), id(cat3))
# print("---马上删除cat对象")
# del cat
# print("---马上删除cat2对象")
# del cat2
# print("---马上删除cat3对象")
# del cat3
#
# print("程序2秒后结束")
# time.sleep(2)

# --------------------------------------------------------------------

# print(int("1.4"))
# print(int(1.4))

# --------------------------------------------------------------------


# 93、列举3条以上PEP8编码规范
#
# 1、顶级定义之间空两行，比如函数或者类定义。
#
# 2、方法定义、类定义与第一个方法之间，都应该空一行
#
# 3、三引号进行注释
#
# 4、使用Pycharm、Eclipse一般使用4个空格来缩进代码

# --------------------------------------------------------------------

# 94、正则表达式匹配第一个URL
import re
s = '<img date-original="https://r.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyuchdn.cn/appCovers/2016/11/13/1213973_21611_small.jpg" style="display:inline;">'

# findall结果无需加group(),search需要加group()提取,match()需要加group()提取
# 加了？，只取第一个
# res = re.findall(r"https://.*?\.jpg", s)[0]
# print(res)
# res = re.search(r"https://.*?\.jpg", s)
# print(res.group())
# --------------------------------------------------------------------
# 95.正则匹配中文
import re
# title = '你好, hello, 世界'
# pattern = re.compile(r'[\u4e00-\u9fa5]+')
# result = pattern.findall(title)
# result = re.findall(r'[\u4e00-\u9fa5]+', title)
# print(result)


# --------------------------------------------------------------------
# import re
# labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
# for label in labels:
#     ret = re.match(r'<(\w*)><(\w*)>.*?</\2></\1>', label)
#     if ret:
#         print("{}是符合要求的标签".format(ret.group()))
#     else:
#         print("{}不符合要求".format(label))

# --------------------------------------------------------------------

# def selfAdd(a):
#     a += a
#
# a_int = 1
# print(a_int)
# selfAdd(a_int)
# print(a_int)
#
#
# a_list = [1, 2]
# print(a_list)
# selfAdd(a_list)
# print(a_list)

# --------------------------------------------------------------------

# a = [1, 2, 3, 4]
# b = [4, 3, 5, 6]
# jj1 = [i for i in a if i in b]  # 在a中的i，并且在也b中，就是交集
# jj2 = list(set(a).intersection(set(b)))
#
# bj1 = list(set(a).union(set(b)))    # 用union
#
# cj1 = list(set(b).difference(set(a)))   # b中有而a中没有的   非常高效！
# cj2 = list(set(a).difference(set(b)))   # a中有而b中没有的   非常高效！
#
# print("交集", jj1)
# print("交集", jj2)
#
# print("交集", bj1)
#
# print("差集", cj1)
# print("差集", cj2)

# --------------------------------------------------------

# 102 生成0-100的随机数
# import random
# res1 = 100 * random.random()
# res2 = random.choice(range(0, 101))
# res3 = random.randint(1, 100)
# print(res1)
# print(res2)
# print(res3)
# --------------------------------------------------------

# 103.lambda匿名函数好处
# a = ["苏州", "中国", "哈哈", "", "", "日本", "", "", "德国"]
# res = list(map(lambda x: "填充值" if x == "" else x, a))
# print(res)

# --------------------------------------------------------
# import pandas as pd
# df = pd.read_excel("D:/windows_file/333.xlsx")
# print(df)
# ---------------------------------------------------------

# import re
# s = "小明年龄28岁  工资10001"
# res = re.search(r"\d+", s).group()  # search 匹配到第一个匹配到的数据
# print("search结果", res)
# #
#
# res = re.findall(r"\d+", s)     # 满足正则，都匹配，不用加group
# print("findall结果", res)
#
# res = re.match("小明", s).group()     # 匹配以"小明"开头的字符串，并匹配出小明
# print("match结果", res)
#
# res = re.match(r"\d+", s)
# print("试错，不加group为none,匹配不到", res)  # 不加group是不对的
#
# res = re.match("工资", s).group()     # 这里去除group()就能正常运行
# print("match结果", res)   # 工资不是字符串开头，匹配不到，报错















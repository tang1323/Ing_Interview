

# 41、举例说明异常模块中try except else finally的相关意义
# try..except..else没有捕获到异常，执行else语句

# try..except..finally不管是否捕获到异常，都执行finally语句

# try:
#     num = 100
#     print(num)
# except NameError as errorMsg:
#     print('产生错误了 ：%s' % errorMsg)
# else:
#     print('没有捕获到异常，则执行这个语句')
#
#
# try:
#     num = 100
#     print(num)
# except NameError as errorMsg:
#     print('产生错误了：%s' % errorMsg)
# finally:
#     print('不管是否捕获到异常， 都执行这个语句')

# -------------------------------------------------------------------

# 43、举例说明zip（）函数用法

# a = [1, 2]
# b = [3, 4]
# res = [i for i in zip(a, b)]
# print(res)
# print(type(res))
#
# a = (1, 5)
# b = (3, 4)
# res = [i for i in zip(a, b)]
# print(res)
# print(type(res))
#
# a = "ab"
# b = "xyz"
# res = [i for i in zip(a, b)]
# print(res)
# print(type(res))


# -------------------------------------------------------------------
# 44、a="张明 98分"，用re.sub，将98替换为100
# import re
# a = "张明 98分"
# ret = re.sub(r"\d+", "100", a)
# print(ret)


# -------------------------------------------------------------------

# 45、写5条常用sql语句

# show databases;
# show tables;
# desc 表名
# select * from 表名
# delete from 表名 where id = 5
# update students set gender=0, hometown='北京' where id = 5

# -------------------------------------------------------------------
# 46、a="hello"和b="你好"编码成bytes类型
# encode是编码，decode是解码
# 只用encode的话，那就是bytes类型码
# 一个编码一个解码，就成字符串

# a = "hello".encode()
# print(a)
#
# b = "你好".encode().decode()
# print(b)
#
# print(type(a), type(b))


# -------------------------------------------------------------------
# 47、[1,2,3]+[4,5,6]的结果是多少？
# a = [1, 2, 3]
# b = [4, 5, 6]
# res = a+b
# print(res)


# -------------------------------------------------------------------
# 48 .提高python运行效率的方法
# 1、使用生成器，因为可以节约大量内存
#
# 2、循环代码优化，避免过多重复代码的执行
#
# 3、核心模块用Cython  PyPy等，提高效率
#
# 4、多进程、多线程、协程
#
# 5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率

# -------------------------------------------------------------------

# 49、简述mysql和redis区别

# redis： 内存型非关系数据库，数据保存在内存中，速度快
#
# mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢

# -------------------------------------------------------------------
# 50、遇到bug如何处理

# 1、细节上的错误，通过print（）打印，能执行到print（）说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alert或console.log
#
# 2、如果涉及一些第三方框架，会去查官方文档或者一些技术博客。
#
# 3、对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会一条一条进行修改，修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都会收藏做一些笔记记录。
#
# 4、导包问题、城市定位多音字造成的显示错误问题

# -------------------------------------------------------------------

# 51、正则匹配，匹配日期2018-03-20
# import re
# url = 'https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
# result = re.findall(r"dateRange=(.*?)%7C(.*?)&", url)
# print(result)
"""
(1)re.match用法是返回一个对象，要加上print(res1.group(1))
(2)re.findall是返回一个列表，里面包含很多东西，直接print(res1)
"""

# -------------------------------------------------------------------
# list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
#
# 利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作

# list = [2, 3, 5, 4, 9, 6]
# new_list = []
# def get_min(list):
#     # 获取列表最小值
#     a = min(list)
#
#     # 删除最小值
#     list.remove(a)
#
#     # 将最小值加入新列表
#     new_list.append(a)
#     print(new_list)
#
# #     # 保证最后列里面有值，递归调用获取最小值
# #     # 直到所有值获取完， 并加入新列表返回
#     if len(list) > 0:
#         get_min(list)
#     return new_list
#
# new_list = get_min(list)
# print(new_list)


# -------------------------------------------------------------------
# 53、写一个单列模式
# 因为创建对象时__new__方法执行，并且必须return
# 返回实例化出来的对象所cls.__instance是否存在，
# 不存在的话就创建对象，存在的话就返回该对象，
# 来保证只有一个实例对象存在（单列），打印ID，值一样，说明
# 对象同一个

# class Singleton(object):
#     __instance = None
#
#     def __new__(cls, age, name):
#         """
#         如果类属性__instance的值为None
#         那么就创建一个对象，并且赋值为这个对象的引用，
#         保证下次调用这个方法时
#         能够知道之前已经创建过对象了，这样就保证了只有一个对象
#         """
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#             print(cls.__instance)
#         return cls.__instance
#
#
# a = Singleton(18, "dongGe")
# b = Singleton(8, "dongGe")
#
# print(id(a))
# print(id(b))
#
# a.age = 19
# print(b.age)












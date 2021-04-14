# global val
# val = 10
#
#
# def test1():
#     global val
#     val = 4
#     print('test1 global val:', val)
#
#
# def test2():
#     val = 8
#     print('test2 global val:', val)
#
#
# class Test():
#     def __init__(self):
#          global val
#          val = 5
#          #zoo()
#          #xy()
#
#     def connect(self):
#          print("class in connect global val:", val)
#          if 5 == val:
#              print("global val is:", val)
#
#
# if __name__ == "__main__":
#     # 可以看出，函数内赋值并不能改变全局变量的值，所以需要global关键字
#     # 全局变量值改变必须要有global关键字：
#     test = Test()
#     test.connect()
#     test1()
#     test2()




# *args的用法
# def import_args(test, *args):
#      print('param1', test)
#      for item in args:
#          print('other param', item)
#
#
# # 解压数据
# # args = ['hello', '2019']
# # import_args('123', *args)
#
# # 123传给test，'hello', '2019'传给*args
# import_args('123', 'hello', '2019')




# **kwargs的用法
# def import_kwargs(test, **kwargs):
#      print('param1', test)
#      for key, value in kwargs.items():
#          print(key, value)
#
#
# d = {'name': 'jack', 'age': 26}
# import_kwargs('123', **d)


# 统计如下list单词及其出现的次数。
# a = ['apple', 'banana', 'apple', 'tomato', 'orange', 'apple', 'banana', 'watermeton']
# dic = {}
# for key in a:
#     dic[key] = dic.get(key, 0) + 1
# print(dic)


# x, y, z是接收参数
# f = lambda x, y, z: x+y+z
# print(f(1, 2, 3))


# reduce是减少的意思
# from functools import reduce
# n = 5
# res = reduce(lambda x, y: x*y, range(1, n+1))
# print(res)


# def actions(x):
#     return lambda y:x+y
#
# a = actions(2)
# print(a(22))
# a是action函数的返回值，a(22)，即是调用了action返回的lambda表达式。


alist = [{"name": "a", "age": 20}, {"name": "b", "age": 30}, {"name": "c", "age": 25}]
alist.sort(key=lambda x: x['age'])
print(alist)

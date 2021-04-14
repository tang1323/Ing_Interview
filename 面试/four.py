
# 16、计算平方根

# num = int(input('请输入一个数字：'))
# num_sqrt = num ** 0.5
# print('{0}的平方根为{1}'.format(num, num_sqrt))



# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#
#     return False


# 18、判断奇偶数
# num = int(input("请输入一个数字："))
# if (num % 2) == 0:
#     print("{0}是偶数".format(num))
# else:
#     print("{0}是奇数".format(num))


# while True:
#     try:
#         num = int(input('请输入一个整数：'))
#     except ValueError:
#         print("你输入的不是整数，请重新输入!!")
#         continue
#
#     if num % 2 == 0:
#         print('{0}是偶数'.format(num))
#     else:
#         print('{0}是奇数'.format(num))
#     break

# 20、获取最大值

# N = int(input('输入需要对比大小数字的个数：'))
# print("请输入需要对比的数字：")
# num = []
# for i in range(1, N+1):
#     temp = int((input('输入第{0}个数字：'.format(i))))
#     num.append(temp)
#
# print('你输入的数字为：', num)
# print('最大值：', max(num))


# 22、十进制转二进制、八进制、十六进制

# dec = int(input("请输入数字："))
#
# print("十进制数为：", dec)
#
# print("转换为二进制为：", bin(dec))
#
# print("转换为八进制为：", oct(dec))
#
# print("转换为十六进制为：", hex(dec))


# 24、简单计算器
# 定义函数
# def add(x, y):
#     """相加"""
#     return x + y
#
#
# def subtract(x, y):
#     """相减"""
#     return x - y
#
#
# def multiply(x, y):
#     """相乘"""
#     return x * y
#
#
# def divide(x, y):
#     """相除"""
#     return x / y
#
#
# # 用户输入
# print("请选择运算：")
# print("1, 相加")
# print("2, 相减")
# print("3, 相乘")
# print("4, 相除")
#
#
# choice = input("输入你的选择（1/2/3/4）:")
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
#
#
# if choice == '1':
#     print(num1, "+", num2, "=", add(num1, num2))
# elif choice == '2':
#     print(num1, "-", num2, "=", subtract(num1, num2))
# elif choice == '3':
#     print(num1, "*", num2, "=", multiply(num1, num2))
# elif choice == '4':
#     if num2 != 0:
#         print(num1, "/", num2, "=", divide(num1, num2))
#     else:
#         print("被除数不能为0")
# else:
#     print("非法输入")


# 25、生成日历

# import calendar
#
# yy = int(input("输入年份："))
# mm = int(input("输入月份："))
#
# print(calendar.month(yy, mm))


# 26、文件IO
# 字符写入到文件
# with open("test.txt", 'wt') as out_file:
#     out_file.write("该文本会写入到文件中\n看到我了吧！！")

# 读取文件
# with open("test.txt", "rt") as in_file:
#     test = in_file.read()
#
# print(test)

# 28、字符串大小写转换
# str = "https://www.cnblogs.com/ailiailan/"
# print(str.upper())# 把所有小写字母换成大写
# print(str.lower())# 把所有大写字母换成小写
# print(str.capitalize())# 把第一个字母转化为大写，其他的小写
# print(str.title())# 把每个单词的第一个字母换成大写，其他的小写

# 30、获取昨天的日期


# import datetime
# def getYesterday():
#     today = datetime.date.today()
#     oneday = datetime.timedelta(days=1)
#     yesterday = today - oneday
#     return yesterday
#
#
# print(getYesterday())


# 31、Python list常用操作
# li = ['a', 'b', 'mpilgrim', 'z', 'example']
# print(li[::-1])
# print(li[::-3])
# print(li[-3])
# # 下标左边从0开始，比如下面这个是从1开始，但是这个3，不包括3
# print(li[1:3])
# # 下标左边从0开始，比如下面这个是从1开始，
# # 这个-1是要取到最后一个，但是不包括最后一个
# print(li[1:-1])
#
# # 下标左边从0开始，包括0，在3结束，不包括第3个
# print(li[0:3])


# 2.list增加元素

# li = ['a', 'b', 'mpilgrim', 'z', 'example']
# li.append("new")
# print(li)
#
# li.insert(2, "new2")
# print(li)
#
# li.extend(["two", 'elements'])
# print(li)

# 3.list搜索
# li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
# 从下标0开始，index也是查找下标的
# res = li.index("example")
# print(res)




# list删除元素
# li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
# # 删除第一个出现的z
# li.remove('z')
# print(li)
#
# # 删除第一个出现的new
# li.remove('new')
# print(li)
#
# # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
# result = li.pop()
# print(result)


# 5.list运算符
# li = ['a', 'b', 'mpilgrim']
# # 在列表下添加这两个['a', 'b', 'mpilgrim', 'example', 'new']
# li = li + ['example', 'new']
# print(li)
#
# li += ['two']
# print(li)
#
# li = [1, 2] * 3
# print(li)

# 6.使用join链接list成为字符串
# params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
# 这是列表
# res = ["{0}={1}".format(k, v) for k, v in params.items()]
# print(res)

# 用join拼接成字符串
# result = ";".join(["{0}={1}".format(k, v) for k, v in params.items()])
# print(type(result))


# 7.list分割字符串

# li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
# s = ";".join(li)
# print(s)

# 必须要变成字符串类型才能分割
# res = s.split(";")
# print(type(res))

# res2 = s.split(";", 2)
# print(type(res2))


# 8.list的映射关系
# li = [1, 9, 8, 4]
# res = [elem*2 for elem in li]
# print(res)
#
# print(li)
#
# li = [elem*2 for elem in li]
# print(li)


# 9.字典中的解析

# params = {"server": "mpilgrim", 'database': 'master', "uid": "sa", "pwd": "secret"}
#
# print(params.keys())
#
# print(params.values())
#
# print(type(params.items()))

# 把keys变成列表输出
# res = [k for k, v in params.items()]
# print(res)


# 把values变成列表输出
# res2 = [v for k, v in params.items()]
# print(res2)

# 把keys和values都输出到一个列表
# res3 = ["{}={}".format(k, v) for k, v in params.items()]
# print(res3)

# 10.list过滤
# li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
# for elem in li:
#     # 只出现一次
#     if li.count(elem) == 1:
#         print(elem)

# 这是列表推导式
# [elem for elem in li if li.count(elem) == 1]


# 在for循环执行时，每次循环都会执行fab函数内部的代码，
# 执行到yield b时，fab函数就返回一个迭代值，下次迭代时，
# 代码从 yield b 的下一条语句继续执行，
# 而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，
# 直到再次遇到 yield。参考实例如下


def gen(n):
    for i in range(n):
        yield i**2
        # yield是返回这个数据，然后下次函数再进入的时候，会从yield开始继续执行


for i in gen(5):
    print(i, " ", end="")












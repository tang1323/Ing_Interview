
# 九九乘法表
# for x in range(1, 10):
#     for y in range(1, 1+x):
#         print("{0}*{1}={2}".format(x, y, x*y), end=' ')
#     print()


# 计算x的N次方
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s


# 3*1=3*3=9*3=27*3=81*3=243*3=729
# 3*3*3*3*3*3=729
# print(power(3, 6))


# 计算a*a + b*b + c*c + d*d + .....
# def Clac(*args):
#     sum = 0
#     for n in args:
#         sum = sum + n * n
#     return sum
#
#
# print(Clac(2, 3, 4, 6))


# 计算阶乘n!
# def fac():
#     num = int(input("请输入一个数字："))
#     factorial = 1
#
#     # 查看数字是负数，0或正数
#     if num < 0:
#         print("抱歉，负数没有阶乘")
#     elif num == 0:
#         print("0的阶乘为1")
#     else:
#         # num+1是不包括最后的数的，所以才加1
#         for i in range(1, num + 1):
#             factorial = factorial * i
#         print("{0}的阶乘为{1}".format(num, factorial))
#
#
# if __name__ == '__main__':
#     fac()


# 5、列出当前目录下的所有文件和目录名
# import os
# print([d for d in os.listdir('.')])


# 6、把一个list中所有的字符串变成小写：

# lists = ['HELLO', 'worD', 'aPPLE']
# # res = [s.lower() for s in list]
# for list in lists:
#     print(list.lower(), end=' ')


# 7、输出某个路径下的所有文件和文件夹的路径
# import os
#
#
# def print_dir():
#     # d:\Py-Project
#     filepath = input("请输入一个路径：")
#     if filepath == "":
#         print("请输入正确的路径：")
#     else:
#         # 获取目录中的文件及子目录列表
#         for i in os.listdir(filepath):
#             # 把路径组合起来, d:\Py-Project+文件名
#             print(os.path.join(filepath, i))
#
#
# print(print_dir())


# 8、输出某个路径及其子目录下的所有文件路径
# import os
#
#
# def show_dir(filepath):
#   for i in os.listdir(filepath):
#     path = (os.path.join(filepath, i))
#     print(path)
#     if os.path.isdir(path):      #isdir()判断是否是目录
#       show_dir(path)             #如果是目录，使用递归方法
#
#
# filepath = "C:\Program Files\Internet Explorer"
# show_dir(filepath)


# 12、替换列表中所有的3为3a

# num = ["harden","lampard",3,34,45,56,76,87,78,45,3,3,3,87686,98,76]
#
# #获取3出现的次数
# for i in range(num.count(3)):
# #     # 获取首次3出现的坐标,这个是索引下标
# #     ele_index = num.index(3)
# #     num[ele_index] = "3a"
# #     print(num)



# 13、打印每个名字

# L = ['James', 'Meng', 'Xin']
# for i in L:
#     print('Hello, {0}'.format(i))

# L = ['James', 'Meng', 'Xin']
# for i in range(len(L)):
#     print("Hello, %s" %L[i])


# 14、合并去重

# list1 = [2, 3, 8, 4, 9, 5, 6]
# list2 = [5, 6, 10, 17, 11, 2]
#
# list3 = list1 + list2
# print(list3)
# print(set(list3))
# print(list(set(list3)))

# 15、随机生成验证码的两种方式

# import random
# list1 = []
# # 这是大写A到Z
# for i in range(65, 91):
#     list1.append(chr(i))
#
# # 这是小写a到z
# for j in range(97, 123):
#     list1.append(chr(j))
#
# # 这是0到9
# for k in range(48, 58):
#     list1.append(chr(k))
#
# # sample的用法：从序列list1随机抽取出6个元素， 并将6个元素以list形式返回
# ma = random.sample(list1, 6)
# print(ma)
#
# ma = "".join(ma)
# print(ma)


# 这是第二种方法
# import random, string
#
# str1 = "0123456789"
# # string.ascii_letters 包含所有字母（大写或小写）的字符串
# str2 = string.ascii_letters
# str3 = str1+str2
#
# # 多个字符中选取特定数量的字符
# ma1 = random.sample(str3, 6)
# ma2 = ''.join(ma1)
# print(ma2)



# 随机数字小游戏
# import random
# i = 1
# a = random.randint(0, 100)
# b = int(input("请输入0-100中的一个数字\n然后查看是否与电脑一样："))
# while a != b:
#     if a > b:
#         print('你第{0}输入的数字小于电脑随机数字'.format(i))
#         b = int(input('请再次输入数字：'))
#     else:
#         print('你第{0}输入的数字大于电脑随机数字'.format(i))
#         b = int(input('请再次输入数字：'))
#     i += 1
# else:
#     print('恭喜你，你第{0}次输入的数字与电脑的随机数字{1}是一样的'.format(i, b))










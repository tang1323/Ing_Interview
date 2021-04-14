# -*- coding: utf-8 -*-

# 闭包
# def outer(a):
#     b = 10
#
#     def inner():
#         print(a+b)
#     return inner
#
#
# if __name__ == '__main__':
#     demo = outer(5)
#     print(demo) # <function outer.<locals>.inner at 0x000001E32BC26AF8>


    # demo = outer(7)
    # print(demo)# <function outer.<locals>.inner at 0x000001C449E86AF8>

# 我们每次调用外函数，它都创建一个内函数，虽然代码一样，但是却创建了不同的对象


# class Solution:
#     def stringMatching(self, words):
#         rs = set()
#         mark = [0]*len(words)
#         for i in range(len(words)):
#             for j in range(len(words)):
#                 if i==j:
#                     break
#                 if words[j].find(words[i])!=-1:
#                     # 找到了包含words[i]的字符串
#                     rs.add(i)
#                 elif words[i].find(words[j])!=-1:
#                     rs.add(j)
#         rs0 = [words[x] for x in rs]
#         return rs0
#
#
# sol = Solution()
# words = ["mass", "as", "hero", "superhero"]
# res = sol.stringMatching(words)
# print(res)



# class A:
#     def __init__(self, args):
#         self.__p = args
#
#     def showA(self):
#         print("self.__p=", self.__p)
#
#
# a = A(100)
# print(a.__p)


import os


# 打印目录内容
# def print_directory_contents(sPath):
#
#     for sChild in os.listdir(sPath):
#
#         # 拼凑路径sPath=D:\Py-Project\Ing_Interview\\tools，
#         # sChild循环sPath这个目录下的文件
#         # 传进来的路径加上每个文件
#         sChildPath = os.path.join(sPath, sChild)
#
#         # 判断是否还有文件夹，如果还有再来循环
#         if os.path.isdir(sChildPath):
#             print_directory_contents(sChildPath)
#         else:
#             print("the path is:", sChildPath)
#
#
# if __name__ == "__main__":
#     print_directory_contents("D:\Py-Project\Ing_Interview")


# def multi():
#     return [lambda x : i*x for i in range(4)]
#
#
# print([m(4) for m in multi()])


def multi():
    sub = []
    for i in range(4):
        def multi2(x):
            return i*x
        sub.append(multi2)

    return sub


# print([m(4) for m in multi()])
for m in multi():
    print(m(4))







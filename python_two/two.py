


# a = 1.23e-4+5.67e+8j.real
# print(a)

# s = "11+5in"
# result = eval(s[1:-2])
# print(result)

# result = abs(-3+4j)
# print(result)

# a = "python等级考试"
# b = "="
# c = ">"
# print("{0:{1}{3}{2}}".format(a, b, 40, c))



# f = open("D:\Py-Project\Ing_Interview\python_two\city", "r")
# ls = f.read().split(",")
# f.close()
# print(ls)


# d = {}
# for i in range(26):
#     d[chr(i+ord("a"))] = chr((i+13) % 26 + ord("a"))
# for c in "Python":
#     print(d.get(c, c), end="")

# s = input("请输入：")
# print("===={}=====".format(s))
# print("{:=^20}".format(s[0:15]))

# a,b = 0, 1
# while a<=100:
#     print(a, end = ",")
#     a, b = b, a+b


# import turtle
# d = 0
# for i in range(3):
#     turtle.fd(200)
#     d = d + 120
#     turtle.seth(d)

# dict = {"数学": 101, "语文": 202, "英语": 203, "物理": 204, "生物": 206}
# dict["化学"] = 205
# dict["数学"] = 201
# del dict["生物"]
# for key in dict:
#     print("{}:{}".format(dict[key], key))


# import random
# random.seed(0x1010)
# s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
# ls = []
# excludes = ""
# while len(ls) < 10:
#     pwd = ""
#     for i in range(10):
#         pwd += s[random.randint(0, len(s)-1)]
#     if pwd[0] in excludes:
#         continue
#     else:
#         ls.append(pwd)
#         excludes += pwd[0]
#
# # 直接打印
# print("\n".join(ls))


















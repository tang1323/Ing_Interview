
# ss = [2, 3, 6, 9, 7, 1]
# for i in ss:
#     print(max(ss), end=',')
#     ss.remove((max(ss)))



# a = [3,6,9]
# b = eval(input()) #例如：[1,2,3]
# j=1
# for i in range(len(a)):
#     b.insert(j, a[i])
#     j += 2
# print(b)



# num = input().split(",")
# for i in num:
#     print("{:>10}".format(i), end="")


# import turtle as t
# ls = [69, 292, 33, 131, 61, 254]
# X_len = 400
# Y_len = 300
# x0 = -200
# y0 = -100
#
# t.penup()
# t.goto(x0, y0)
# t.pendown()
#
# t.fd(X_len)
# t.fd(-X_len)
# t.seth(90)
# t.fd(Y_len)
#
# t.pencolor('red')
# t.pensize(5)
# for i in range(len(ls)):
#     t.penup()
#     t.goto(x0 + (i+1)*50, y0)
#     t.seth(90)
#     t.pendown()
#     t.fd(ls[i])
# t.done()





# import turtle as t
# import random as r
# color = ['red','orange','blue','green','purple']
# r.seed(1)
# for i in range(5):
#     rad = r.randint(20,50)
#     x0 = r.randint(-100,100)
#     y0 = r.randint(-100,100)
#     t.color(r.choice(color))
#     t.penup()
#     t.goto(x0,y0)
#     t.pendown()
#     t.circle(rad)
# t.done()

# fi = open("D:/Py-Project/Ing_Interview/历年经典/txt/data (1).txt", "r")
# f = open("D:/Py-Project/Ing_Interview/历年经典/txt/univ.txt", "w")
# for line in fi:
#     if "alt" in line:
#         dx = line.split("alt=")[-1].split('"')[1]
#         print(dx)
#         f.write("{}\n".format(dx))
# f.close()
# fi.close()

# f = open("D:/Py-Project/Ing_Interview/历年经典/txt/vote.txt", encoding="utf-8")
# names = f.readlines()
# f.close()
# n = 0
# for name in names:
#     num = len(name.split())
#     print(num)
#     if num == 1:
#         n += 1
# print("有效票{}张".format(n))


# import jieba
# fi = open('D:/Py-Project/Ing_Interview/历年经典/txt/data (2).txt', 'r')
# fo = open('out1.txt', 'w')
#
# fio = fi.readlines()
# D = []
# for word in fi:
#     fio_s = jieba.lcut(word)
#     for fio_lis in fio_s:
#         if len(fio_lis) < 3:
#             continue
#         else:
#             if fio_lis not in D:
#                 D.append(fio_lis)
# fo.writelines("\n".join(D))
#
# fi.close()
# fo.close()





# while True:
#     s = input("请输入不带数字的文本:")
#     n = 0
#     for p in s:
#         if "0" <= p <= "9":
#             n += 1
#     if n == 0:
#         break
# print(len(s))


# import jieba
#
# fi = open('D:/Py-Project/Ing_Interview/历年经典/txt/data (3).txt', 'r')
# fo = open('out.txt', 'w')
# lines = fi.read()
# ls = jieba.lcut(lines)
# for line in ls:
#
#     if line not in ["\n"]:
#         fo.writelines('\n'.format(line))  # 将分词结果存到文件out.txt中
# fo.close()
# fi.close()
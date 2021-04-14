
# x = 0o1010
# print(x)



# x = 10
# y = 3
# print(divmod(x, y))

# for s in "Helloworld":
#     if s =="w":
#         continue
#     print(s, end="")


# s = ["seashell", "gold", "pink", "brown", "purple", "tomato"]
# print(s[0:4])# ['seashell', 'gold', 'pink', 'brown']
# print(s[1:4:2])# ['gold', 'brown'], 2是步长，从哪个数跑到哪个数距离为2
# s = ["seashell", "gold", "pink", "brown", "purple", "tomato"]
# print(s[3:5])# 从下标开始，3包括第3个值，而5是结束，不包括第5个值


# d = {"大海": "蓝色", "天空": "灰色", "大地": "黑色"}
# str = "大海是蓝色的，天空是灰色的，大地是黑色的"
# print(d["大地"])
# print(d.get("天空", "黄色"))

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# s = 0
# for c in a:
#     for j in range(3):
#         s += c[j]
# print(s)

# test = open("D:/Py-Project/Ing_Interview/python_two/book", "r")
# test = open("D:/Py-Project/Ing_Interview/python_two/book", "a", encoding='utf-8')
# name = ['abc', 'xiaozi', 'xiaobai', 'xiaohei', 'xiaoming', 'xiaolan']
# test.write(',\n\n'.join(name))
# print(test)
# test.close()

# import jieba
# s = "中国特色社会主义进入新时代，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾。"
# n = len(s)
# m = len(jieba.lcut(s))
# m = jieba.lcut_for_search(s)
# print("中文字符数为{}，中文词语数为{}。".format(n, m))


#
# ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合",
#       "综合", "综合", "师范", "理工", "综合", "理工", "综合", "综合",
#       "综合", "综合", "综合", "理工", "理工", "理工", "理工", "师范",
#       "综合", "农林", "理工", "综合", "理工", "理工", "理工", "综合",
#       "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
# d = {}
# for word in ls:
#     d[word] = d.get(word, 0) + 1
# for k in d:
#     print("{}:{}".format(k, d[k]))



# a = 10
# b = 20
# a, b = a, a + b
# print(a, b)



# a = b
# b = a + b
# print(a, b)


# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# num = eval(input("请输入一个整数："))
# print(fact(abs(int(num))))

# import time
# print(time.ctime())


# import sys
# print(sys.version)

# x = 0b1010
# print(x)

# x = 3.1415926
# print(round(x, 2), round(x))


# a = False!= 0
# print(a)

# a = 1000000
# b = "-"
# print("{0:{2}^{1},}\n{0:{2}>{1},}".format(a, 30, b))

# import turtle as t
# def DrawCctCircle(n):
#     t.penup()
#     t.goto(0, -n)
#     t.pendown()
#     t.circle(n)
# for i in range(20, 80, 20):
#     DrawCctCircle(i)
# t.done()

# N = eval(input("请输入0-100的整数："))
# print("{:>3}%@{}".format(N, "="*(N//5)))


# N = input("请输入一个整数: ")
# s = 0
# for i in range(eval(N), eval(N)+100):
#     if i%2 == 1:
#         s += i
# print(s)



# fi = open("D:\Py-Project\Ing_Interview\python_two\天龙八部-网络版", "r", encoding="utf-8")
# fo = open("天龙八部-汉字统计.txt", "w",encoding="utf-8")
# test = fi.read()
# d = {}
# for i in test:
#     d[i] = d.get(i, 0)+1
# del d[' ']
# del d['\n']
# ls=[]
# for key in d:
#     print("{}:{}".format(key, d[key]))
# fo.write(','.join(ls))
# fi.close()
# fo.close()












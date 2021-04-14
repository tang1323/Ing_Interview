



# a = "python等级考试"
# b = "="
# c = ">"
# print("{0:{1}{3}{2}}".format(a, b, 25, c))
# {0:=>25}


# def func(num):
#     num *= 2
#     return num
# x = 20
# func(x)
# print(x)

# s = input()  # 请输入一个由1和0组成的二进制数字串
# d = 0
# while s:
#     d = d * 2 + (ord(s[0]) - ord('0'))
#     s = s[1:]
# print("转换成八进制数是：{:o}".format(d))

# import turtle
# def drawCircle():
#     turtle.pendown()
#     turtle.circle(20)
#     turtle.penup()
#     turtle.fd(40)
# def drawRowCircle(n):
#     for j  in range(n,1,-1):
#         for i in range(j):
#             drawCircle()
#         turtle.fd(-j*40-20)
#         turtle.right(90)
#         turtle.fd(40)
#         turtle.left(90)
#         turtle.fd(40)
#     drawCircle()
# drawRowCircle(5)
# turtle.hideturtle()
# turtle.done()


picd = {}
fi = open("D:/Py-Project/Ing_Interview/精品真题/txt/dir_50.txt", 'r')
for l in fi:
    l = l.strip()
    if len(l):
        l = l.split("_")
        if l[0] != '':
            lkey, lvalue = l[1][:-4], eval(l[0])
            lv = []
            for v in lvalue:
                if v != '0':
                    lv.append(v)

            print("{}:{}".format(lkey, lv))
            picd[lkey] = lv

fi.close()


idd= {}
for key in picd:
    for num in picd[key]:
        idd[num] = idd.get(num, 0) + 1


count = len(idd)
s = sum(idd.values())























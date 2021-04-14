

# import time
# import turtle
# turtle.color('red', 'pink')
# turtle.begin_fill()
#
# # 从左边画起，角度135
# turtle.left(135)
#
# # 画100长
# turtle.fd(100)
#
# # 从右边画起角度180
# turtle.right(180)
#
# # 画一半圆，50是圆的大小，-180是画多长，-是向右连画
# turtle.circle(50, -180)
#
# # 开始转向左
# turtle.left(90)
#
# # 画一半圆，50是圆的大小，-180是画多长，-是向右连画
# turtle.circle(50, -180)
#
# # 从右边画起角度180
# turtle.right(180)
#
# # 画100长
# turtle.fd(100)
#
# # 开始填充颜色
# turtle.end_fill()
#
# turtle.hideturtle()
# turtle.done()


# import time
# import turtle
# turtle.setup(400, 400)
# # 抬起画笔，不画
# turtle.penup()
# turtle.goto(-100, 50)
# time.sleep(3)
#
# # 落下画笔，之后，移动画笔
# turtle.pendown()
# turtle.color("red")
# turtle.begin_fill()
# time.sleep(3)
# for i in range(5):
#     turtle.forward(200)
#     turtle.right(144)
# turtle.end_fill()
# turtle.hideturtle()
# turtle.done()


# import time
# import turtle
# n = 10
# for i in range(1, 10, 1):
#     time.sleep(2)
#     for j in [90, 180, -90, 0]:
#         # time.sleep(2)
#         turtle.seth(j)
#         turtle.fd(n)
#         n += 5



# import time
# import turtle
# turtle.setup(800,300)
# turtle.penup()
# turtle.fd(-350)
# turtle.pendown()
# def DrawLine(size):
#     for angle in [0,90,-90,-90,90]:
#         time.sleep(2)
#         turtle.left(angle)
#         turtle.fd(size)
# for i in [20, 30, 40, 50, 40, 30, 20]:
#     DrawLine(i)
# turtle.hideturtle()
# turtle.done()



# import turtle as t
# def DrwaCctCircle(n):
#     t.penup()
#     t.goto(0,-n)
#     t.pendown()
#     t.circle(n)
# for i in range(20,100,20):
#     DrwaCctCircle(i)
# t.hideturtle()
# t.done()


# import turtle as t
# t.setup(500,300)
# t.penup()
# t.goto(-180, -50)#将画笔移动到绝对位置(–180,–50)处
# t.pendown() #画笔落下
# def Drawrect():
#     t.fd(40)
#     t.left(90)
#     t.fd(120)
#     t.left(90)
#     t.fd(40)
#     t.left(90)
#     t.fd(120)
#     t.penup()
#     t.left(90)
#     t.fd(42)
#     t.pendown()
# for i in range(7):
#     Drawrect()
# t.penup()
# t.goto(-150, 0)
# t.pendown
# def DrawRectBlack():
#     t.color('black')
#     t.begin_fill()
#     t.fd(30)
#     t.left(90)
#     t.fd(70)
#     t.left(90)
#     t.fd(30)
#     t.left(90)
#     t.fd(70)
#     t.end_fill()
#     t.penup()
#     t.left(90)
#     t.fd(40)
#     t.pendown()
# DrawRectBlack()
# DrawRectBlack()
# t.penup()
# t.fd(48)
# t.pendown()
# DrawRectBlack()
# DrawRectBlack()
# DrawRectBlack()
# t.hideturtle()
# t.done()



# import turtle as t
# t.colormode(255)
# t.color(255, 215, 0)    #设置颜色取值为金色（255,215,0）
# t.begin_fill()
# for x in range(1, 9):      #绘制8条线
#     t.forward(200)
#     t.left(225)
# t.end_fill()
# t.hideturtle()
# t.done()



# import turtle
# for i in range(5):
#     turtle.penup()
#     turtle.goto(-200+100*i,-50)
#     turtle.pendown()
#     turtle.circle(40,steps=3+i)
# turtle.done()



# import turtle as t
# def tree(length,level):#树的层次
#     if level <= 0:
#         return
#     t.forward(length)  #前进方向画 length距离
#     t.left(45)
#     tree(0.6*length,level-1)
#     t.right(90)
#     tree(0.6*length,level-1)
#     t.left(45)
#     t.backward(length)
#     return
# t.pensize(3)
# t.color('green')
# t.left(90)
# tree(100,6)



# N = eval(input())
# if N == 1 :
#     flag = False
#     print(flag)
# else:
#     flag = True
#     for i in range(2,N):
#         print(i)
#         if N % i == 0:
#             flag = False
#             break
#     print(flag)

# N = eval(input())
# print(N**2)
# s = 0
# for c in N:
#     s += eval(c)**2
# print(s)








# N = input("请输入一个整数：")
# s = 0
# while N != "":
#     s += eval(N)
#     N = input("请你再输入一个整数")
# print(s)

# N = input("请你他么的输入一个整数：")
#
# while True:
#     flag = True
#     for c in N:
#         if c in "1234567890":
#             N = input("你他么的傻啊，叫你不要输入一个整数：")
#             flag = False
#             break
#     if flag:
#         break
# print(N)

# while True:
#     N = input("请输入全数字的数据：")
#     try:iii8
#         print(eval(N))
#         break
#     except:
#         pass

# while True:
#     N = input("请输入一个带有小数点的数字：")
#     if type(eval(N)) == type(1.0):
#         print(eval(N))
#         break



# a, b = 1, 2
# ls = []
# ls.append(str(a))
# while b<1000*1000:
#     a, b = b, a**2 + b**2
#     ls.append(str(a))
# print(",".join(ls))



import random as r
r.seed(17)
s = ""
for i in range(20):
    s += str(r.randint(0,999))
print(s)











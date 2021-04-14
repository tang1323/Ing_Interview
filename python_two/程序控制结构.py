

# for i in "Python":
#     print(i, end=",")

# sum = 0
# for i in range(1, 11):
#     sum += i
#     print(sum)

# age = 23
# start = 2
# if age % 2 != 0:
#     start = 1
# for x in range(start, age+2, 2):
#     print(x)


# k = 10000
# sum = 0
# while k > 1:
#     print(k)
#     k = k / 2
#     sum += 1
#     print(sum)


# for i in range(1, 6):
#     if i / 3 == 0:
#         break
#     else:
#         print(i, end=",")

# sum = 0
# for i in range(2, 101):
#     if i % 2 == 0:
#         sum += i
#     else:
#         sum -= i
# print(sum)

# a = []
# for i in range(2, 10):
#     count = 0
#     for x in range(2, i-1):
#         if i % x == 0:
#             count += 1
#     if count != 0:
#         a.append(i)
#         print(a)
# print(a)


# x2 = 1
# for day in range(4, 0, -1):
#     x1 = (x2 + 1) * 2
#     x2 = x1
# print(x1)

# for num in range(2, 10):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)


# for n in range(100, 200):
#     i = n // 100
#     j = n // 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print(n)


# a = 2.0
# b = 1.0
# s = 0
# for n in range(1, 4):
#     s += a / b
#     t = a
#     a = a + b
#     b = t
# print(round(s, 2))


# for a in 'mirror':
#     print(a, end="")
#     if a == 'r':
#         break


# s = 1
# while(s <= 1):
#     print('计数：', s)
#     s = s + 1


# for i in ["pop star"]:
#     pass
#     print(i, end="")

# i = 1
# while i < 6:
#     j = 0
#     while j < i:
#         print("*", end='')
#         j += 1
#
#     print("\n")
#     i += 1


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{}*{}={}\t".format(j, i, i*j), end='')
#     print("")

# a = 1
# if isinstance(a, int):
#     print("{} is int".format(a))
# else:
#     print("{} is not int".format(a))


# a = input("").split(",")
# x = 0
# while x < len(a):
#     print(a[x], end="")
#     x += 1


# ls = ["car", "truck"]
# def func(a):
#     ls = []
#     ls.append(a)
#     return
# func("bus")
# print(ls)


# import turtle
# def drawLine(draw):
#     turtle.pendown() if draw else turtle.penup()
#     turtle.fd(250)
#     turtle.right(90)
#
# drawLine(True)
# drawLine(0)
# drawLine(True)
# drawLine(True)
# turtle.left(90)
# drawLine(0)
# drawLine(True)
# drawLine(True)





















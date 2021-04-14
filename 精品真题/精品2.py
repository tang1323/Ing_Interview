
# tstr = 'china520'
# print(eval(tstr[5:-1]))


# n = eval(input("请输入一个整数:"))
# s = 0
# if n >= 7:
#     n -= 1
#     s = 4
# if n < 7:
#     n -= 1
#     s = 3
#
# print(s)

# fo = open('', 'r')
# ls = []
# for line in fo.readlines():
#     ls.append(line.replace("\n", '').split(','))
# s = input("请输入星座中文名称(例如,双子座):")
# for i in range(len(ls)):
#     if s == ls[i][1]:
#         print("{}的生日位于{}-{}之间".format(s, ls[i][2], ls[i][3]))




# fo = open('', 'r')
# ls = []
# for line in fo.readlines():
#     ls.append(line.replace("\n", '').split(','))
# sall = input("请输入星座中文名称(例如,双子座):")
#
#
# while sall != '':
#     lsNum = sall.split()
#     for s in lsNum:
#
#         for i in range(len(ls)):
#             if s == ls[i][0]:
#                 print("{}({})的生日是{}月{}日{}之间".format(ls[i][1], ls[i][4], ls[i][2][:-2], ls[i][2][-2:], ls[i][3][:-2], ls[i][3][-2:]))
#     sall = input('请输入星座序号(例如, 5):')



# fo = open('', 'r')
# ls = []
# for line in fo.readlines():
#     ls.append(line.replace("\n", '').split(','))
# sall = input("请输入星座中文名称(例如,双子座):")
#
#
# while sall != '':
#     lsNum = sall.split()
#     for s in lsNum:
#         if 1 <= int(s) <= 12:
#             for i in range(len(ls)):
#                 if s == ls[i][0]:
#                     print("{}({})的生日是{}月{}日{}之间".format(ls[i][1], ls[i][4], ls[i][2][:-2], ls[i][2][-2:], ls[i][3][:-2], ls[i][3][-2:]))
#         else:
#             print("输入星座编号有误！")
#     sall = input('请输入星座序号(例如, 5):')

























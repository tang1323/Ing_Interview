# fi = open("D:/Py-Project/Ing_Interview/历年经典/txt/论语.txt", 'r')
# fo = open("论语-原文.txt", 'w')
# wflag = False
# for line in fi:
#     if "【" in line:
#         wflag = False
#     if "【原文】" in line:
#         wflag = True
#         continue
#     if wflag == True:
#         fo.write(line)
#
# fi.close()
# fo.close()


# f=open("name.txt")
# names=f.readlines()
# f.close()
# f=open("vote.txt")
# votes=f.readlines()
# f.close()
# D={}
# NUM=0
# for vote in votes:
#     num = len(vote.split())
#     if num==1 and vote in names:
#         D[vote[:-1]]= D.get(vote[:-1], 0)+1
#         NUM+=1
#     else:
#         with open("vote1.txt","a+",encoding="utf-8") as fi:
#             fi.write("{}".format(vote))

# fo = open("D:/Py-Project/Ing_Interview/历年经典/txt/PY301-SunSign.csv", 'r')
#
# ls = []
# for line in fo.readlines():
#     ls.append(line.replace("\n","").split(","))
# s = input("请输入星座中文名称(例如, 双子座):")
# for i in range(len(ls)):
#     if s == ls[i][1]:
#         print("{}的生日位于{}-{}之间".format(s,ls[i][2], ls[i][3]))

fo = open("D:/Py-Project/Ing_Interview/历年经典/txt/PY301-SunSign.csv", 'r')
#
# ls = []
# for line in fo.readlines():
#     ls.append(line.replace("\n", "").split(","))
# sall = input("请输入星座序号(例如,5 10):")
# while sall != '':
#     IsNum = sall.split()
#     for s in IsNum:
#         for i in range(len(ls)):
#             if s == ls[i][0]:
#                 print("{}({})的生日是{}月{}日至{}月{}日之间".format(ls[i][1], ls[i][4], ls[i][2][:-2], ls[i][2][-2:],
#                                                          ls[i][3][:-2], ls[i][3][-2:]))
#         sall = input("请输入星座序号(例如,5 10):")


# fo = open("D:/Py-Project/Ing_Interview/历年经典/txt/PY301-SunSign.csv", 'r',encoding='UTF-8')
# ls = []
# for line in fo.readlines():
#       ls.append(line.replace("\n", '').split(','))
#       # li = line.strip().split(',')
# sall = input('请输入星座序号(例如,5 10):')
# while sall != '':
#     lsNum = sall.split()
#     for s in lsNum:
#         if 1 <= int(s) <=12:
#             for i in range(len(ls)):
#                 if s == ls[i][0]:
#                     print("{}({})的生日是{}月{}日至{}月{}日之间".format(ls[i][1],ls[i][4],ls[i][2][:-2],ls[i][2][-2:],ls[i][3][:-2],ls[i][3][-2:]))
#         else:
#             print("输入星座序号有误！")
#     sall = input('请输入星座序号(例如,5 10):')

n = 0
m = 0
fi = open("D:/Py-Project/Ing_Interview/历年经典/txt/univ.txt", "r")
lines = fi.readlines()
for line in lines:
    if "大学生" in line:
        continue
    elif "大学" in line and "学院" in line:
        if "大学" in line:
            n += 1
        elif "学院" in line:
            m += 1
    elif "大学" in line:
        print("{}".format(line))
        n += 1
    elif "学院" in line:
        print("{}".format(line))
        m += 1

fi.close()

print("包含大学的名称数量是{}".format(n))
print("包含学院的名称数量是{}".format(m))  # 此处一行



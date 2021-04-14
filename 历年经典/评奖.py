# fi = open("D:/Py-Project/Ing_Interview/历年经典/txt/score.txt","r")
# D = [] #单个学生的数据
# L = [] #所有学生原始成绩和总成绩
# #读取学生单科成绩并计算总成绩i
# for line in fi.readlines():
#     D = line.split()
#     s = 0
#     for i in range(10):
#         s += int(D[i+2])
#     D.append(s)
#     L.append(D)
#
# L.sort(key=lambda x:x[-1],reverse=True) #按学生总成绩从大到小排序
#
# fo = open('candidate0.txt','w')
# for i in range(10): #前十个学生数据写入文件中
#     for j in range(len(L[i])):
#         print("{} ".format(L[i][j]))
#     fo.write("\n")
# fi.close()
# fo.close()

fi = open("candidate0.txt", 'r')
lines = fi.readlines()
fo = open("candidate.txt", 'w')

D = []
for line in lines:
    D = line.split()
    for i in range(10):
        if int(D[i + 2]) < 60:
            break
    else:
        print("{}{}\n".format(D[i][0], D[i][1]))

fi.close()
fo.close()
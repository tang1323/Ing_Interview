#编程模板2：PY301-2.py
# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

# n = 0
# m = 0
# f = open("univ.txt", "r")
#
# for line in f: # 此处可多行
#     if "大学生" in line:
#         continue
#     elif "大学" in line and "学院" in line:
#         if line[-3:-1] == "学院":
#             n += 1
#             print(line, end='')
#         elif line[-3:-1] == "大学":
#             m += 1
#             print(line, end='')
#     elif "学院" in line:
#         n += 1
#         print(line, end='')
#     elif "大学" in line:
#         m += 1
#         print(line, end='')
#
# f.close()
#
# print("包含学院的名称数量是{}".format(n))
# print("包含大学的名称数量是{}".format(m))

#
# studs= [{'sid':'103','Chinese': 90},
# {'sid':'101','Chinese': 80},
# {'sid':'102','Chinese': 70}]
# scores = {}
# for stud in studs:
#     sv = stud.items()
#     print(sv)
#     for it in sv:
#         if it[0] =='sid':
#             k = it[1]
#         else:
#             scores[k]  = it[1]
# so = list(scores.items())
# so.sort(key = lambda x:x[0],reverse = False)
# for l in so:
#     print('{}:{}'.format(l[0],l[1]))



# import turtle
# d = 0
# k = 1
# for j in range(100):
#    for i in range(4):
#        turtle.fd(k)
#        d += 91
#        turtle.seth(d)
#        k += 1
# turtle.done()

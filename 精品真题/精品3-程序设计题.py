
# fi = open("D:/Py-Project/Ing_Interview/精品真题/txt/论语.txt", 'r', encoding='utf-8')
# fo = open("D:/Py-Project/Ing_Interview/精品真题/txt/论语.txt-提取版", 'w', encoding='utf-8')
#
# wflag = False
#
# for line in fi:
#     if "【" in line:
#         wflag = False
#     if "原文】" in line:
#         wflag = True
#         continue
#     if wflag == True:
#
#         fo.write(line)
# fi.close()
# fo.close()


# fi = open("D:/Py-Project/Ing_Interview/精品真题/txt/论语.txt-提取版", 'r', encoding='utf-8')
# fo = open("D:/Py-Project/Ing_Interview/精品真题/txt/论语.txt-原文", 'w', encoding='utf-8')
#
#
# for line in fi:
#     for i in range(100):
#         line = line.replace("({}) ".format(i), "")
#     fo.write(line)
# fi.close()
# fo.close()








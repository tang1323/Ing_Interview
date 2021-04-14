
# fi = open("天龙八部-网络版", "r", encoding="utf-8")
# fo = open("天龙八部-汉字统计.txt", "w", encoding="utf-8")
# txt = fi.read()
# d = {}
# for c in txt:
#     d[c] = d.get(c, 0) + 1
# del d[' ']
# del d['\n']
# ls = []
# for key in d:
#     ls.append("{}:{}".format(key, d[key]))
# fo.write(",".join(ls))
# fi.close()
# fo.close()


# fi = open("txt/天龙八部-汉字统计.txt", "r", encoding='utf-8')
# txt = fi.read()
# cnt = 0
# flag = False
# for c in txt:
#     if c == "“":
#         flag = True
#         continue
#     if c == "”":
#         flag = False
#     if flag:
#         cnt += 1
# print("占总字符比例：{:.0%}。".format(cnt/len(txt)))
# fi.close()



# import jieba
# fi = open("txt/射雕英雄传-网络版.txt", "r", encoding='utf-8')
# txt = fi.read()
# fi.close()
# ls = jieba.lcut(txt)
# d = {}
# for w in ls:
#     d[w] = d.get(w, 0) + 1
# for x in " \n，。！“”：":
#     del d[x]
# rst = []
# for i in range(8):
#     mx = 0
#     mxj = 0
#     for j in d:
#         if d[j] > mx:
#             mx = d[j]
#             mxj = j
#     rst.append(mxj)
#     del d[mxj]
# print("，".join(rst))























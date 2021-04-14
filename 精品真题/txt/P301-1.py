#编程模板1：P301-1.py
# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

fi = open("data .txt", 'r')  # 此处可多行

f = open("univ.txt", "w")

for line in fi:# 此处可多行
    if "alt" in line:
        dx = line.split("alt=")[-1].split('"')[1]
        print(dx)
        f.write("{}\n".format(dx))

fi.close()
f.close()
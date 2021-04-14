
# TempStr = "Hello World"
# print(TempStr[-5:])
# print(TempStr[-5:-1])

# s = "PYTHON"
# print("{0:1}".format(s))


# import turtle
# edge = 6
# d = 0
# k = 1
# for j in range(10):
#     for i in range(edge):
#       turtle.fd(k)
#       d += 360/edge
#       turtle.seth(d)
#       k += 3
# turtle.done()



import jieba                                #导入中文分词库jieba
import turtle as t                          #导入turtle库，并给turtle去一个别名t

def drawCircle(x,y,radius,color,name):          #自定义函数drawCircle,包含了5个参数
    t.pencolor(color)                           #设置绘圆的颜色,color是一个必选参数，调用函数时可以设置为'red'、'blue'...
    t.penup()                                   #绘图笔提前起来，表示不落下去绘图，
    t.goto(x, y)                                #将笔的坐标定位到(x,y),x,y都是必选参数
    t.write(name, font=('Arial', 10, 'normal')) #在当前的(x,y),写上name内容，文字属性由font决定。name是必选参数
    t.seth(-90)                                 #将绘图方向设置为-90度方向
    t.pendown()                                 #绘图笔放下，表示落下去绘图，有颜色啦:)
    t.circle(radius)                            #按半径为radius绘制圆形
    return t.pos()                              #返回t.pos()当前的位置,例如:(-300.00,0.00)

dws = {}                                            #定义一个字典，注意不是集合哦
with open('D:/Py-Project/Ing_Interview/精品真题/txt/lizhi.txt', 'r', encoding="utf-8") as f:  #用with语句以只读方式打开lizhi.txt文件
    for l in f.readlines():                         #遍历列表f.readlines()中的每一个元素
        ws = jieba.lcut(l.strip('\n'))              #去掉行字符串最后的"\n"不可显示换行符，
                                                    #使用jieba.lcut(str)函数进行中文分词，返回一个列表
        for w in ws:
            if len(w) >= 2:                         #统计词语长度>=2 的词语出现频次
               dws[w] = dws.get(w,0) + 1            #逐步构建字典dws,词语:次数的键值对
                                                    #如果w在dws的keys中，则键值+1，如果w不在dws的keys中，则构建健值对dws[w] = 0 + 1

dls = list(dws.items())                             #将dws.items()转换为列表并赋值给dls,形如[("abc",10),("edf","12"),...]，目前是无序的
dls.sort(key = lambda x:x[1], reverse= True)        #对dls进行排序，按列表元素中索引为1，这行代码考试时会给出。但一定要理解。


x,y = -300,0                                        #设置初始坐标位置
for i in range(10):                                 #根据统计结果绘制图形
    print(dls[i][0],dls[i][1])                      #输出结果
    x,y = drawCircle(x,y,dls[i][1]*4 ,'red',dls[i][0]+str(dls[i][1]))
    x +=  dls[i][1] * 8                             #改变x初始位置，y值不变
t.done()














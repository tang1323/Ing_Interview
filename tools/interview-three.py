# 54、保留两位小数
#
# 题目本身只有a="%.03f"%1.3335,让计算a的结果，为了扩充保留小数的思路，
# 提供round方法（数值，保留位数）

# a = "%.03f" % 1.3335
# print(a, type(a))
#
# b = round(float(a), 1)
# print(b, type(b))
#
# b = round(float(a), 2)
# print(b, type(b))
#
# A = zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5))
# A0 = dict(A)
# print(A0, type(A0))

# ----------------------------------------

# 55、求三个方法打印结果
#
# fn("one",1）直接将键值对传给字典；
#
# fn("two",2)因为字典在内存中是可变数据类型，所以指向同一个地址，传了新的额参数后，会相当于给字典增加键值对
#
# fn("three",3,{})因为传了一个新字典，所以不再是原先默认参数的字典


# def fn(k, v, dic={}):
#     dic[k] = v
#     print(dic)
#
#
# fn("one", 1)
# fn("two", 2)
# fn("three", 3, {})

# ----------------------------------------

# 58、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}

# dic = {"name": "zg", "age": 18}
# dic.pop("name")
# print(dic)
#
# dic = {"name": "zs", "age": 19}
# del dic["name"]
# print(dic)


# ---------------------------------------------------

# 59、列出常见MYSQL数据存储引擎
#
# InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。
# 如果需要对事务的完整性要求比较高（比如银行），要求实现并发控制（比如售票），
# 那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，
# 也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。
#
# MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，
# 那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求比较低，也可以使用。
#
# MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。
# 如果需要很快的读写速度，对数据的安全性要求较低，可以选择MEMOEY。
# 它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在相对较小的数据库表。

# ---------------------------------------------------
# 60、计算代码运行结果，zip函数历史文章已经说了，
# 得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]
# A = zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5))
# A0 = list(A)
# print(A0, type(A0))
#
# A = zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5))
# A0 = dict(A)
# A1 = range(10)
# A2 = [i for i in A1 if i in A0] # 想在这里取，但A0己经转换成了dict了， 是取不了0-9了
# A3 = [A0[s] for s in A0] # 这里取的是A0的键，它之前是dict，所以取的是键
# print("A0", A0)
# print(list(zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5))))
# print(A2)
# print(A3)

# dict()创建字典新方法
# s = dict([["name", "zs"], ["age", 18]])
# print(s)
#
# s = dict([("name", "zs"), ("age", 18)])
# print(s)



# ---------------------------------------------------

# 66、python中copy和deepcopy区别
#
# 1、复制不可变数据类型，不管copy还是deepcopy,
# 都是同一个地址  当浅复制的值是不可变对象（数值，字符串，元组）
# 时和=“赋值”的情况一样，对象的id值与浅复制原来的值相同。
# import copy
#
# a = "哈哈哈"
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
# print(a, id(a))
# print(b, id(b))
# print(c, id(c))
# print(d, id(d))


# 2、复制的值是可变对象（列表和字典）
# import copy
# list = [1, 2, [3, 4]]
# a = copy.copy(list)
# b = copy.deepcopy(list)
# # 外层列表：[1，2，[3, 4]]
# # 内层列表：[3,4]
# # 复杂子对象：[3，4]，我们认为包含嵌套结构的内层列表（字典）为复杂子对象
# # 简单子对象：1，2
# print("测试原始数据和copy和deepcopy后的结果及ID地址")
# print("结果表明对于外层列表来说，三者是独立的对象")
# print("原始数据和id", list, id(list))
# print("原始数据和id", a, id(a))
# print("原始数据和id", b, id(b))
# print("*************************")
# print("测试修改外层列表的简单子对象，也就是修改1或者2")
# print("结果表明修改了原始list之后，a和b并没有随之改变，符合我们的正常逻辑，因为是三个不同的对象")
# list[0] = 10
# print("将1改成10结果", list)
# print("将1改成10结果", a)
# print("将1改成10结果", b)
# print("*********************************************")
# print("测试内层列表的值的修改，也就是测试复杂子对象的值的修改")
# print("结果表明copy浅拷贝并没有真正将内层表明（字典）独立拷贝出来，导致修改了list内层列表（字典）后a的内层列表（字典）值也变了")
# list[2][0] = 5
# print("将3改成5结果", list)
# print("将3改成5结果", a)
# print("将3改成5结果", b)

# ---------------------------------------------------
# 列表排序
# list = [0, -1, 3, -10, 5, 9]
# list.sort(reverse=False)
# print("list.sort在list基础上修改，无返回值", list)
#
# list = [0, -1, 3, -10, 5, 9]
# res = sorted(list, reverse=False)
# print("sorted有返回值是新的list为res,list还是原来的list", list)
# print("返回 值 ", res)

# ---------------------------------------------------

# 72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],
# 使用lambda函数从小到大排序

# foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
# # foo.sort(key=lambda x:x)
# a = sorted(foo, key=lambda x : x)
# print(a)

# ---------------------------------------------------
# 73、使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为

# [0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小

# foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
# a = sorted(foo, key=lambda x: (x < 0, abs(x)))
# foo.sort(key=lambda x: (x < 0, abs(x)))
# print(a)
# print(foo)


# ---------------------------------------------------
# 74、列表嵌套字典的排序，分别根据年龄和姓名排序

# foo = [{"name": "zs", "age": 19}, {"name": "ll", "age": 54},
#
#      {"name": "wa", "age": 17}, {"name": "df", "age": 23}]
#
# a = sorted(foo, key=lambda x: x["age"], reverse=True)# reverse=True从大到小
# print(a)
# b = sorted(foo, key=lambda x: x["age"], reverse=False)# reverse=False年龄从小到大
# print(b)

# ---------------------------------------------------
# 75、列表嵌套元组，分别按字母和数字排序
#
# foo = [("zs", 19), ("ll", 54), ("wa", 17), ("df", 23)]
#
# a = sorted(foo, key=lambda x: x[1], reverse=True)# x[1]指的是"19",reverse=True从大到小
# print(a)
# b = sorted(foo, key=lambda x: x[0], reverse=False)# x[0]指的是"zs",reverse=False年龄从小到大
# print(b)

# ---------------------------------------------------
# foo = [["zs", 19], ["ll", 54], ["wa", 23], ["df", 23], ["xf", 23]]
# a = sorted(foo, key=lambda x: (x[1], x[0]))# 不写reverse那就默认是False，就是从小到大,先是x[1]从小到大排，如果x[1]一样，再x[0]从小到大排，x[0]是"zs"
# print(a)
# b = sorted(foo, key=lambda x: x[0])# 不写reverse那就默认是False，就是从小到大,x[0]是"zs"
# print(b)


# ---------------------------------------------------

# 77、根据键对字典排序（方法一，zip函数）

# dic = {"name": "zs", "sex": "man", "city": "bj"}
# foo = zip(dic.keys(), dic.values())# 字典转列表嵌套元组
# foo = [i for i in foo]
# print("字典转成列表嵌套元组", foo)
#
# b = sorted(foo, key=lambda x: x[0])# 字典嵌套元组排序，不写reverse那就默认是False，就是从小到大
# print("根据键排序", b)
# new_dic = {i[0]: i[1] for i in b}# 排序完构造新字典
# print("字典推导式构造新字典", new_dic)


# ---------------------------------------------------
# 78、根据键对字典排序（方法二,不用zip)
# 有没有发现dic.items和zip(dic.keys(),dic.values())
# 都是为了构造列表嵌套字典的结构，方便后面用sorted()构造排序规则

#
# dic = {"name": "zs", "sex": "man", "city": "bj"}
# foo = zip(dic.keys(), dic.values())
# foo = [i for i in foo]
# print("字典转成列表嵌套元组", foo)
#
#
# print(dic.items())# 跟zip(dic.keys(),dic.values()))一样
# b = sorted(dic.items(), key=lambda x: x[0])# 不写reverse那就默认是False，就是从小到大
# print("根据键排序", b)
# new_dic = {i[0]: i[1] for i in b}
# print("字典推导式构造新字典", new_dic)

# ---------------------------------------------------

# 79、列表推导式、字典推导式、生成器
# import random
# td_list = [i for i in range(10)]
# print("列表推导式", td_list, type(td_list))
#
# ge_list = (i for i in range(10))
# print("生成器", ge_list, type(ge_list))
#
# dic = {k: random.randint(4, 9) for k in ["a", "b", "c", "d"]}
# print("字典推导式", dic, type(dic))


# ---------------------------------------------------

# 80、最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用

# s = ["ab", "abc", "a", "djkj"]
# b = sorted(s, key=lambda x: len(x))     # sorted有返回值，在这里是返回到b身上，所以不改变s本身
# print(b, s)
# s.sort(key=len)     # sort无返回值，所以在s自身修改
# print(s)


# -----------------------这是lambda的用法，lambda是有返回值的----------------------
# li = [{"age": 20, "name": "def"}, {"age": 25, "name": "abc"}, {"age": 10, "name": "ghi"}]
# li = sorted(li, key=lambda x: x["age"])
# li.sort(key=lambda x: x["age"])
# print(li)


# def comp(x):
#     return x["age"]
# li = [{"age": 20, "name": "def"}, {"age": 25, "name": "abc"}, {"age":10, "name": "ghi"}]
# li = sorted(li, key=comp)
# print(li)
# -----------------------这是lambda的用法，lambda是有返回值的----------------------


#
# 81、举例说明SQL注入和解决办法
#
# 当以字符串格式化书写方式的时候，
# 如果用户输入的有;+SQL语句，后面的SQL语句会执行，
# 比如例子中的SQL注入会删除数据库demo

# input_name = "zs"
# sql = 'select * from demo where name = "%s"' % input_name
# print("正常SQL语句", sql)
#
# input_name = "zs; drop database demo"
# sql = 'select * from demo where name ="%s"' % input_name
# print("SQL注入语句", sql)


# -----------------------------------------------
# 82、s="info:xiaoZhang 33 shandong",用正则切分字符串输出
# ['info', 'xiaoZhang', '33', 'shandong']
# |表示或，根据冒号或者空格切分
# import re
# s = "info:xiaoZhang 33 shandong"
# res = re.split(r":| ", s)
# print(res)
# -----------------------------------------------


# 83、正则匹配以163.com结尾的邮箱
# import re
# email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihe", ".com.xiaoWang@qq.com"]
#
# for email in email_list:
#     ret = re.match(".*?163.com$", email)
#     if ret:
#         print("是符合规定的邮件地址，匹配后的结果是：{}".format((ret.group())))
#     else:
#         print("%s 不符合要求" % email)


# -----------------------------------------------

# 84、递归求和

# def get_sum(num):
#     if num >= 1:
#         res = num + get_sum(num-1)
#
#     else:
#         res = 0
#
#     return res
#
# res = get_sum(10)
# print(res)


# -----------------------------------------------
# 85、python字典和json字符串相互转化方法
#
# json.dumps()字典转json字符串，json.loads()json转字典
# import json
# dic = {"name": "zs"}
# res = json.dumps(dic)
# print(res, type(res))
# ret = json.loads(res)
# print(ret, type(ret))

# -----------------------------------------------
# 87、统计字符串中某字符出现次数

# str = "张三, 美国, 张三, 哈哈, 张三"
# res = str.count("张三")
# print(res)
# -----------------------------------------------
# 88、字符串转化大小写
# str = "HHHuuu"
# print(str.upper())
# print(str.lower())
# -----------------------------------------------

# 89、用两种方法去空格
# str = "hello world ha ha"
# res = str.replace(" ", "")
# print(res)
#
# list = str.split(" ")
# print(list)
# res = "".join(list)
# print(res)

# -----------------------------------------------
# 90、正则匹配不是以4和7结尾的手机号
# import re
# tels = ["13100001234", "18912344321", "10086", "18800007777"]
# for tel in tels:
#     ret = re.match("^1\d{9}[0-3,5-6,8-9]$", tel)
#     if ret:
#         print("想要的结果", ret.group())
#
#     else:
#         print("{}不是想要 的手机号码".format(tel))

# a = "k:1|k1:2|k2:3|k3:4"
# di = a.split("|")    # ['k:1', 'k1:2', 'k2:3', 'k3:4']
# # print(di)
#
# res = {}
# for d in di:
#      key, value = d.split(":")
#      res[key] = int(value)
# print(res)


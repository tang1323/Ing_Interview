import re

"""
# findall结果无需加group(),
search需要加group()提取,
match()需要加group()提取
# 加了？，只取第一个
"""

# ^b必须是b开头
# .任意字符，用的比较多
# *前面的任意字符出现多少次都可以，用的比较多
# $是以什么结尾的，比如下面是以3$结尾的

# ?是一个非贪婪匹配的模式，从后面开始取，也就是反向取值，".*(b.*b).*"，.*就是后面是什么字符我不管，b遇到b了就取，.*中间不管是什么就取什么，再遇到b再取b就行

# .*一般我们是贪婪的模式，还要向后面取
# .*?只取第一个， 非贪婪匹配的模式

# .*?(b.*?*).*,从前面开始.*不管什么都取，？从左边开始取，然后遇到b就取,?b)到第一个b结束就行ob，不用再取后面三个b

# line = "booooooobbbby123"
# regex_str = "^b.3$"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))
#
# regex_str = ".*?(b.*?b).*"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))



# +的意思是在两个b之间有什么就取什么，大于一次都可以提取出来
# line = "booooaaaooobbbcaby123"
# regex_str = ".*(b.+b).*"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))



# {n}满足几次
# {n, m}满足在n与m之间
# line = "booooaaaooobbbcaby123"
# line = "点赞 1"
# line = 'https://bbs.csdn.net/topics/397712664?page=2'
# regex_str = ".*(b.{5}b).*"
# regex_str = ".*?(\d+)"
# regex_str = ".*?(\d+)\?"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))



# | 或，满足一个就能打印出来
# line = "bobby123"
# regex_str = "((bobby|boobby)123)"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(2))# 现在取括号第二个值



# []括号里面只要满足其中一个字符就行了
# [0-9]是一个区间，0到9都 可以
# [0-3,5-6,8-9]正则匹配不是以4和7结尾的手机号
# [^1]不能等于1，等于1就不取
# [年/-]，只有出现在其中一个，就可以取出来，中括号是非常强大的
# {8}取8个字符

# line = "18782902222"
# regex_str = "(1[648357][0-9]{8})"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))# 现在取括号第二个值




# \s就是一个空格
# \S就是不是一个空格， 相反的意思
# \w就是[A-Za-z0-9_]
# \W就是[A-Za-z0-9_]和包括空格
# line = "你 好"
# regex_str = "(你\W好)"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))


# [\u4E00-\u9FA5]只提取汉字
# \d是取数字的意思
# line = "study in 南京大学"
# line = "134出生于2001年"
# regex_str = ".*?(\d+)年"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))





# 举例

# line = "xxx出生于2001年6月1日"
# line1 = "xxx出生于2001年/6/1"
# line2 = "xxx出生于2001年-06-01"
# line3 = "xxx出生于2001年-6-1"
# line4 = "xxx出生于2001年-06"
# regex_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))"
# match_obj = re.match(regex_str, line1)
# if match_obj:
#     print(match_obj.group(1))


#
# text = 'var __signature = "b099061608302187119";'
#
# text_re = "__signature = \"(.*)\""
# match_obj = re.search(text_re, text)
# if match_obj:
#     print(match_obj.group(1))






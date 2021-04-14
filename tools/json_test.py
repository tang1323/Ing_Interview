
"""
loads有三种情况：
1.dict1 = [{"age": "12"}]
json_info = json.loads(dict1)
print((type(json_info)))
这个会出类型错误

2.dict1 = '[{"age": "12"}]'
json_info = json.loads(dict1)
print((type(json_info)))
这个就是list类型，输出：[{'age': '12'}]
也就是说str类型变成list类型

3.dict1 = '{"age": "12"}'
json_info = json.loads(dict1)
print((type(json_info)))
这个就是字典类型，输出{"age": "12"}
也就是说str类型变成dict类型

"""

"""
dumps有以下情况：
1.dict1 = '[{"age": "12"}]'
json_info = json.dumps(dict1)
这个str转换还是str,输出："[{\"age\": \"12\"}]"，因为原本就是字符串类型，再转换就得加上转义字符

2.dict1 = [{"age": "12"}]
json_info = json.dumps(dict1)
这个是list类型转换成str类型，输出：[{"age": "12"}]

3.dict1 = {"age": "12"}
json_info = json.dumps(dict1)
这个是dict转换成字符串，输出：{"age": "12"}


"""

import json

# json.dumps()函数的使用，将字典转化为字符串
dict1 = {"age": "12"}
json_info = json.dumps(dict1)
print("dict1的类型："+str(type(dict1)))
print("通过json.dumps()函数处理：{}".format(json_info))
print((type(json_info)))












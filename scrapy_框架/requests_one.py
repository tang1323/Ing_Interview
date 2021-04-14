

# requests使用流程
#     pip install requests
#     指定url
#     发起请求
#     获取响应回来的页面数据
#     持久化存储

import requests
# # 1.指定url
# url = 'https://www.sogo.com/'
#
# # 2.发起请求：get方法会返回一个响应对象
# response = requests.get(url=url)
#
# # 3.获取页面数据
# page_text = response.text
#
# # 4.持久化存储
# with open('sogou.html', 'w', encoding='utf-8') as fp:
#     fp.write(page_text)

# -----------------------------------------------------------------------


# 3.带User-Agent的请求

# url = 'https://www.qiushibaike.com/text/'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111'
# }
#
# response = requests.get(url=url, headers=header)
#
# # print(response.text)
#
#
# def parse(response):
#     content = response.xpath('//*[@id="qiushi_tag_123812929"]/a[1]/div/span[1]')
#     pass


# -----------------------------------------------------------------------


# 　5.带coockies的请求

# import uuid
# import requests
#
# url = 'http://httpbin.org/cookies'
# cookies = dict(sbid=str(uuid.uuid4()))
#
#
# res = requests.get(url=url, cookies=cookies)
# print(res.text)


# 实例化一个是session对象,session对象包含着cookies
# session = requests.session()
# # session对象可以直接发起请求的
# session.get()
# session.post()


# 7.request的post请求 　

# 来看一个例子,爬取百度翻译的结果

import requests
import json
url = 'https://recomm.cnblogs.com/api/v2/recomm/blogpost/reco'

cookie = {
    ' _ga': 'GA1.2.1194887636.1605493684',
    'UM_distinctid':'175d3d597ce116-0867e12fda9c5e-567a7466-151800-175d3d597cfed',
    '_gid':'GA1.2.1819536129.1605695853',
    'Hm_lvt_1e91e188a793fc12acbf77cc47464552':'1605759652,1605778012,1605779072',
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111',
    'accept': 'application/json, text/javascript, */*; q=0.01'
}

# kw = input('请输入一个词:')
# data = {
#     'kw': kw
# }

response = requests.post(url=url, headers=header, cookies=cookie)
print(json.loads(response.text))











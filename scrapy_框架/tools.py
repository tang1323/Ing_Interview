import requests
from scrapy import Selector
import re

# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3080.5 Safari/537.36"}
#
# response = requests.get("https://www.lagou.com", headers=headers)
# sel_css = Selector(text=response.text)
# sel = sel_css.css('.unick').extract()
#
# print(sel)



value = "25K-29K"
# # 把点赞数量或者评论数量变成int类型，这样在数据更好检索
match_re = re.match("k-(\d+)k$", value)
# match_re = re.match(r".*?(\d+).*", value)
if match_re:
    nums = int(match_re.group())
    nums *= 1000
else:
    nums = 0
print(nums)


# ------------------------------------------------------------------------------
# value = "\n             广州-\n            成都\n         -世纪城\n     查看地图\n     "
#
# addr_list = value.split("\n")
# addr_list = [item.strip() for item in addr_list if item.strip()!="查看地图"]
# print("".join(addr_list))
# ---------------------------------------------------------------------------------
# value = "三国梦-lk,编辑,收藏"
# tags = value.split(",")[0]
# # tag = tags[0]
#
# print(tags)


# -----------------------------------------

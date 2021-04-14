from collections import Counter
from wordcloud import WordCloud
import itertools
import jieba
import jieba.posseg
import json

# stopwords = set(open("stopwords_cn.txt", encoding="utf-8").read().splitlines())
#
# # 启用基于深度学习的切字模式
# jieba.enable_paddle()
#
# # 加载潦草的数据
# data = json.load(open(r"data.json", encoding="utf-8"))
#
# # 提取所有的单词
# words = [word for title in data for word, _ in jieba.posseg.cut(title)]
#
# # 过滤掉停止词
# words = filter(lambda x: x not in stopwords, words)
#
# # 过滤掉长度小于等于1的单词
# words = filter(lambda x: len(x) > 1, words)
#
# # 根据出现次数选择前100个单词
# counter = Counter(list(words))
# most_common_words = counter.most_common(100)
# print(most_common_words)
#
#
# wordcloud = WordCloud(
#     font_path="SourceHanSerifSC-Medium", width=1920, height=1080, colormap="Blues",
# ).generate_from_frequencies(dict(most_common_words))
#
# im = wordcloud.to_image()
# im.save("word-cloud.png")


import imageio
def get_word():

    # 选择同一个文件夹下的luoxiang.jpg图片
    # mask = imageio.imread('千库网12005065.png')
    data = open("D:/js-project/web-scraping/data.json", encoding="utf-8").read().splitlines()

    # 使用jieba模块的lcut()精确模式进行分词，并用空格连接词语
    danmu_word = jieba.lcut(" ".join(data))
    # 将分词结果再次用空格连接，并转化成制作词云需要的字符串形式
    danmu_str = " ".join(danmu_word)

    # 构造词云对象,字体为微软雅黑,背景颜色为白色
    # w = WordCloud(font_path="msyh.ttc", width=1920, height=1080, colormap="Blues", background_color='white', mask=mask)

    # 构造词云对象,字体为微软雅黑,背景颜色为黑色
    w = WordCloud(font_path="msyh.ttc", width=1920, height=1080, colormap="Blues", background_color='black')

    # 将处理好的分词弹幕加载到词云中
    w.generate(danmu_str)
    # 将生成的词云保存为danmu.png图片
    w.to_file('bilibili.png')


if __name__ == "__main__":
    get_word()


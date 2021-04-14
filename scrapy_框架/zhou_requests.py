
from bs4 import BeautifulSoup
import requests
import sys
import pymysql
import re


# 设置页面的数量
def set_download_urls():
    """
    http://www.agri.cn/kj/syjs/zzjs/index_1.htm
    页面形态
    :return:
    """
    downloadUrls = []
    baseUrl = 'http://www.agri.cn/kj/syjs/zzjs/'
    downloadUrls.append('http://www.agri.cn/kj/syjs/zzjs/index.html')
    for i in range(1, 10):
        url = baseUrl + 'index_' + str(i) + '.htm'
        downloadUrls.append(url)
    return downloadUrls


# 获取下载页面网址
def get_download_tables():
    downloadUrls = set_download_urls()
    tables = []
    for url in downloadUrls:
        req = requests.get(url)
        req.encoding = 'utf-8'
        html = req.text
        table_bf = BeautifulSoup(html)
        tables.append(table_bf.find('table', width=500, align='center'))
    return tables


# 获取文章链接

def get_download_url():
    downloadTables = get_download_tables()
    articles = []
    for each in downloadTables:
        articles.append(each.find_all('a', class_='link03'))
    return articles


def read_articles_info():
    articles = get_download_url()
    baseUrl = 'http://www.agri.cn/kj/syjs/zzjs/'
    dict = {}

    for each in articles:
        for item in each:
            dict[item.string] = baseUrl + item.get('href')[1:]
    return dict


# 保存到mysql下
def save_mysql(title, date, source, content, tech_code, info_code):
    db = pymysql.connect('localhost', 'tangming', '130796', 'persona')

    cursor = db.cursor()

    sql = 'INSERT INTO information_stock (title,date,source,content,tech_code,info_code) VALUES ("%s","%s","%s","%s",%s,%s)' % (title,date,source,content,tech_code,info_code)

    try:
        cursor.execute(sql)
        db.commit()
        print("write success")
    except Exception as e:
        db.rollback()
        print("write fail")
        print(e)

    db.close()


# 获取内容信息并保存

def get_content(title, url):
    print(title + '---->' + url)

    req = requests.get(url)
    req.encoding = 'utf-8'
    html = req.text
    table_bf = BeautifulSoup(html)
    article = table_bf.find('table', width=640)


    # 文章内容
    content = article.select("p")
    info = article.find(class_="hui_12-12").get_text()
    date = info[3:19]
    source = info.split(":")[3]
    text = ""


    for item in content:
        text += item.get_text()
        text += "\n"

    save_mysql(title, date, source, text, 0, 0)


# 保存全部文章
def save_date():
    dict = read_articles_info()
    for key, value in dict.items():
        get_content(key, value)


save_date()













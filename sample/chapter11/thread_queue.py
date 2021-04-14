"""
线程间通信
"""
import time
import threading
from threading import RLock
from sample.chapter11 import variables

from threading import Condition


# 1. 生产者当生产10个url以后就就等待，保证detail_url_list中最多只有十个url
# 2. 当url_list为空的时候，消费者就暂停


# detail_url_list = []
#
#
# def get_detail_html(lock):
#     # 爬取文章详情页
#     # 这是使用全局变量来实现线程间的通信问题，是一种比较简单粗暴的方法
#     # 用global来声明引用全局变量
#     global detail_url_list
#     # 用pop从队尾取数据
#     url = detail_url_list.pop()
#     # for url in detail_url_list: # 用for循环很慢，所以用pop从队尾取数据
#     print("get detail html started")
#     time.sleep(2)
#     print("get detail html end")
#
#
# def get_detail_url():
#     # 爬取文章列表页
#     # 这是使用全局变量来实现线程间的通信问题，是一种比较简单粗暴的方法
#     # 用global来声明引用全局变量
#     global detail_url_list
#     print("get detail url started")
#     time.sleep(4)
#     # 这里假装在爬取20个url
#     for i in range(20):
#         # 这里是往全局变量里append加数据
#         detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
#     print("get detail url end")
#
#
# # 1. 线程通信方式- 共享变量,全局变量
#
# if __name__ == "__main__":
#     thread_detail_url = threading.Thread(target=get_detail_url)
#     # 这是直接启动10个线程，假设启动10个，线程启动多了对操作系统是一种负担
#     for i in range(10):
#         html_thread = threading.Thread(target=get_detail_html)
#         html_thread.start()
#     start_time = time.time()
#     #
#     # thread1.join()
#     # thread2.join()
#
#     # 当主线程退出的时候， 子线程kill掉
#     print ("last time: {}".format(time.time()-start_time))


# 这下面是进化版本
def get_detail_html(lock):
    # 爬取文章详情页
    # 我们把全局变量放在variables中
    # 还是引用全局变量
    detail_url_list = variables.detail_url_list
    while True:
        # 先判断detail_url_list里面是否有数据
        if len(variables.detail_url_list):
            lock.acquire()
            if len(detail_url_list):
                url = detail_url_list.pop()
                lock.release()
                # for url in detail_url_list:
                print("get detail html started")
                time.sleep(2)
                print("get detail html end")
            else:
                lock.release()
                time.sleep(1)


def get_detail_url(lock):
    # 爬取文章列表页
    detail_url_list = variables.detail_url_list
    while True:
        print("get detail url started")
        time.sleep(4)
        # 这里假装在爬取20个url
        for i in range(20):
            lock.acquire()
            if len(detail_url_list) >= 10:
                lock.release()
                time.sleep(1)
            else:
                detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
                lock.release()
        print("get detail url end")


# 1. 线程通信方式- 共享变量,全局变量

if __name__ == "__main__":
    lock = RLock()
    thread_detail_url = threading.Thread(target=get_detail_url, args=(lock,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(lock,))
        html_thread.start()
    # # thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    # thread_detail_url.start()
    # thread_detail_url1.start()
    #
    # thread1.join()
    # thread2.join()

    #当主线程退出的时候， 子线程kill掉
    print ("last time: {}".format(time.time()-start_time))
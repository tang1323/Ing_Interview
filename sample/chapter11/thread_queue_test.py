

"""通过queue的方式进行线程间同步"""
from queue import Queue


import time
import threading


def get_detail_html(queue):
    # 爬取文章详情页
    while True:
        # 往消息队列取，用消息队列的好处是，如果thread_detail_url消息队列里为空，
        # 它get会一直停在这里
        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            # 这里是往消息队列里put加数据
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


# 1. 线程通信方式- 共享变量
if __name__ == "__main__":
    # 用消息队列来做线程间的通信
    detail_url_queue = Queue(maxsize=1000)

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    # # thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    # thread_detail_url.start()
    # thread_detail_url1.start()
    #
    # thread1.join()
    # thread2.join()
    """
    爬虫都有运行完的时刻，我们用join()方法，它会一直blocks阻碍住 
    要想让我们的join()退出，必须要在某个地方给这个queue发一个task_done信号
    直到我们的queue接收到一个task_done信号才停住 
    所以task_done()和join()是成对出现的
    比如我们爬取1000条了，我们就停掉我们的爬虫
    这样我们的主线程才会退出 
    """
    detail_url_queue.task_done()
    # 这个join()就是用来阻塞住我们的queue，但是爬虫总有停止的时候
    # 这个join()要接收到我们的task_done信号才会退出，
    detail_url_queue.join()

    # 当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time()-start_time))
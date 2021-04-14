"""Semaphore 是用于控制进入数量的锁
进入控制是什么意思，比如场景：文件， 读、写， 写一般只是用于一个线程写，
读可以允许有多个
"""

# 另一个例子：做爬虫，控制爬虫的并发数
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    # 重载run
    def run(self):
        # 两秒爬取一个
        time.sleep(2)
        print("got html text success")
        # 这里释放锁，这里每次调用release()，sem = threading.Semaphore(3)就加1
        # 放在这里释放锁才是并发3次，因为这里才是爬取url知道的地方
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    # 重载run
    def run(self):
        for i in range(20):
            # 这里获取锁，这里每次调用acquire()，sem = threading.Semaphore(3)就减1
            self.sem.acquire()
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == "__main__":
    # sem控制3个并发
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()

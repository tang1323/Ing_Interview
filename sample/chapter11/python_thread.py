# 对于io操作来说，多线程和多进程性能差别不大
# 1.通过Thread类实例化
"""
这是多线程
方法实现多线程
类集成Thread实现多线程

"""
import time
import threading
from threading import Thread


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")

#
# if __name__ == "__main__":
#     # 这里的target只能写方法名，所以参数要写在args上，但是只有一个参数的话，那就要加上一个逗号
#     thread1 = threading.Thread(target=get_detail_html, args=("",))
#     thread2 = threading.Thread(target=get_detail_url, args=("", ))
#     """
#     假设一种情况。如果主线程让t1, t2在1秒钟内执行完任务，如果不执行完成
#     就代表t1, t2出现问题了，
#     那这两个线程就要跟着主线程退出关闭掉
#     thread1.setDaemon(True)  # 也就是说thread1设置为守护线程
#     """
#     # thread1.setDaemon(True)
#     # thread2.setDaemon(True)
#     start_time = time.time()
#
#     thread1.start()
#     thread2.start()
#
#     """
#     2.如何让主线程等到其他线程执行以后才继续执行
#     这里用  thread1.join()
#             thread2.join()
#             也就就是主线程阻塞住，等待这两个线程运行完再运行主线程
#     这样就先打印t1,t2这两个线程再执行计算时间
#     """
#     thread1.join()
#     thread2.join()
#
#     end_time = time.time()
#     # 当主线程退出的时候，子线程kill掉
#     print("last time:{}".format(end_time-start_time))
# ——--------------------------------------------------------------


# 2. 通过集成Thread来实现多线程
class GetDetailHtml(Thread):
    def __init__(self, name):
        # 这里如果只写__init__方法，它会提示让我们继承父类的方法
        # 继承父类方法也有好处，因为父类方法有很多初始化的工作
        # 我们要加上，这是一个好习惯
        super().__init__(name=name)

    # 若是用类来实现，那就得重载这个run方法，这是固定的
    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(Thread):
    def __init__(self, name):
        # 这里如果只写__init__方法，它会提示让我们继承父类的方法
        # 继承父类方法也有好处，因为父类方法有很多初始化的工作
        # 我们要加上，这是一个好习惯
        super().__init__(name=name)

    # 若是用类来实现，那就得重载这个run方法，这是固定的
    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()

    """
    2.如何让主线程等到其他线程执行以后才继续执行
    这里用  thread1.join()
         thread2.join()
         也就就是主线程阻塞住，等待这两个线程运行完再运行主线程
    这样就先打印t1,t2这两个线程再执行计算时间
    """
    thread1.join()
    thread2.join()

    # 当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time()-start_time))
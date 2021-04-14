"""这里是线程池的例子"""
# futures是一个非常底层的一个包， 这让我们编写多线程多进程更容易，而且它们的接口非常一致的
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future   # Future是非常非常重要的
from multiprocessing import Pool

""""
Future我们叫未来对象，是因为submit返回一个Future对象，
这个时候我们的任务还没有完成，但是将来某个时候完成所以叫未来对象
但是我们更加倾向叫task的返回容器，执行的结果或者状态都往这里面放

多线程多进程多协程在Future里面都是采用同一种设计理念，
"""


# 线程池， 为什么要线程池
# 线程池可以让  主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致
import time


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


# 这里在线程池里开了2个线程
# ThreadPoolExecutor翻译过来就是线程池，executor是一个实例化对象
executor = ThreadPoolExecutor(max_workers=2)
# ---------------------------------------------
# 这里面是一个一个的来做线程池，下面是批量做
# 通过submit函数提交执行的函数到线程池中, submit 是立即返回，是非阻塞的，是立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))
# ----------------------------------------------

# 要获取已经成功的task的返回，这里我们批量提交
urls = [3, 2, 4]
# 通过submit函数提交执行的函数到线程池中, submit 是立即返回，是非阻塞的，是立即返回
all_task = [executor.submit(get_html, (url)) for url in urls]

# wait()是指定我们某一个线程执行完成再继续往下执行
# return_when是能指明哪一个事件完成(线程)完再往下执行
# return_when=FIRST_COMPLETED是执行完第一个再往下执行
wait(all_task, return_when=FIRST_COMPLETED)
print("main")
# ---------------------------------------------------------

# as_completed()方法在as_completed里面
"""as_completed的工作就是找出己经完成的线程yield出去"""
"""我们更加偏向使用这个"""
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page".format(data))
# -----------------------------------------------------------------

# 通过executor的map获取已经完成的task的值，map()是返回urls的list是顺序，就算后面的线程先结束，但也按urls顺序返回
# map()里面已经帮我们做了yield future.result(),所以更加简单
# for data in executor.map(get_html, urls):
#     print("get {} page".format(data))


# --------------------------------------------------------------------


# 这是比较简单的写法
# #done方法用于判定某个任务是否完成
# print(task1.done())
# cancel()是在线程开始的之前取消才行，开始之后就取消不了，这个要接收executor的对象基础上才能执行
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
#
# #result方法可以获取task的执行结果
# print(task1.result())


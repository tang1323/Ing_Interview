
"""这是多进程使用的例子和进程池的例子"""
# import os
# # fork只能用于linux/unix中
# pid = os.fork()
"""
fork()是创建一个子进程，也就是复制一份父进程的数据
但是多进程和多线程不同，在多进程中的数据是完全隔离的

原本在下面这里if pid == 0:里面的语句是不会执行的，
但是在fork()下面的语句下面的所有代码复制一份给子进程
所以在if pid == 0:在子进程里pid是等于0的，里面的语句能在子进程里运行的
所以在fork()下面的所有数据都能运行的！！！！
注意：这一块的代码只能在Linux下运行

"""
# print("bobby")
# if pid == 0:
#   print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
# else:
#   print('我是父进程：{}.'.format(pid))
# ----------------------------------------------------------------------


# multiprocessing翻译过来是多处理的意思
import multiprocessing

# 多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n


# 使用类来实现多进程, 和多线程一样的
# class MyProgress(multiprocessing.Process):
#     def run(self):
#         pass


if __name__ == "__main__":
    # 这里和多线程区别差不多一样，下面这个是多线程，拿来比较一下
    # thread2 = threading.Thread(target=get_detail_url, args=("", ))
    # 下面是多进程的一个方法，但在进程中每一个进程是有一个pid的
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)     # 必须是在start()后面才有pid的，因为才启动多进程嘛
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")



# ------------------------------------------------------------
    # 使用进程池， 这里指的是multiprocessing里的线程池
    """
    使用多进程池最好是有几个cpu就使用几个，保持与cpu一样的数量
    cpu_count()就是获取我电脑上有几个cpu
    这是线程池的实例化，与多进程相比较一下
    executor = ThreadPoolExecutor(max_workers=2)
    """
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
# -----------------------下面是看实现多进程的例子---------------------------------
    # apply_async()就是异步提交的一个任务， args=(3,)的3是sleep3秒
    # result = pool.apply_async(get_html, args=(3,))
    #
    # # join()等待所有任务完成， 这样我们就能get()数据了
    # pool.close()    # 使用join()的时候，前面一人定要使用close()，这样pool才不会接收新的任务进来
    # pool.join()
    #
    # print(result.get())

# ------------------------这里是看多进程的状态的例子--------------------------------------
    # imap，这个imap是和concurrent_futures里面的map()是一样的
    # imap谁先完成某一个任务后，找出己经完成的线程yield出去，但是这里不管哪个先完成
    # 它都会按照[1,5,3]的顺序输出
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

# -------------------------这是看多进程状态的另一个例子-----------------------------

    # imap_unordered()是谁先完成就先打印谁的，和concurrent_futures里面的as_completed()一样
    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))





import time
from concurrent.futures import ThreadPoolExecutor, as_completed     # 这是多线程
from concurrent.futures import ProcessPoolExecutor      # 这是多进程
# 多进程编程
# 耗cpu的操作，用多进程编程， 对于io操作来说， 使用多线程编程，进程切换代价要高于线程


# 1. 对于耗费cpu的操作，多进程优于多线程
# def fib(n):
#     """用斐波那契数列来看多线程与多进程的计算能力"""
#     if n <= 2:
#         return 1
#     return fib(n-1)+fib(n-2)
#
#
# if __name__ == "__main__":
#     # 在这里ThreadPoolExecutor是关闭线程池的方法
#     # 在这里ProcessPoolExecutor是关闭线程池的方法
#     """
#     在concurrent_futures里是实例化一个executor = ThreadPoolExecutor(max_workers=2)
#     但在这里我们用with做
#     """
#     with ProcessPoolExecutor(3) as executor:
#         # 通过submit函数提交执行的函数到线程池中, submit 是立即返回，是非阻塞的，是立即返回
#         all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
#         start_time = time.time()
#         """as_completed的工作就是找出己经完成的线程yield出去"""
#         """我们更加偏向使用这个"""
#         for future in as_completed(all_task):
#             data = future.result()
#             print("exe result: {}".format(data))
#
#         print("last time is: {}".format(time.time()-start_time))
# ------------------------------------------------------


# 2. 对于io操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    with ThreadPoolExecutor(3) as executor:
        # 通过submit函数提交执行的函数到线程池中, submit 是立即返回，是非阻塞的，是立即返回
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))

        print("last time is: {}".format(time.time()-start_time))


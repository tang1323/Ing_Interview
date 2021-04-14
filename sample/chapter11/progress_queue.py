"""这是多进程通信的例子"""
"""
有多进程中有三种queue
from queue import Queue     这一种不能用与多进程通信
from multiprocessing import Queue       这个在下面也有例子了
from multiprocessing import Manager     这个要实例化才能用
Manager().Queue()
"""


import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe
#
"""
我们使用Queue来完成多进程的通信必须使用在multiprocessing里的Queue
方法对照多线程的用法
from multiprocessing import Queue     # 这里使用的是这个queue
"""
# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == "__main__":
#     queue = Queue(10)
#     my_producer = Process(target=producer, args=(queue,))
#     my_consumer = Process(target=consumer, args=(queue,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


# 共享全局变量通信
# 共享全局变量不能适用于多进程编程，可以适用于多线程
# 因为子进程会完全复制一份全局变量一样的父进程的数据
# 然后两边数据作修改是互不影响的
# def producer(a):
#     a += 100
#     time.sleep(2)
#
#
# def consumer(a):
#     time.sleep(2)
#     print(a)
#
#
# if __name__ == "__main__":
#     a = 1
#     my_producer = Process(target=producer, args=(a,))
#     my_consumer = Process(target=consumer, args=(a,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


# multiprocessing中的queue不能用于pool进程池
# pool中的进程间通信需要使用Manager中的queue
"""
from multiprocessing import Manager
Manager().Queue()       这个要实例化才能用
"""
# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == "__main__":
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))
#
#     pool.close()
#     pool.join()


# 通过pipe实现进程间通信,是简化版本的Queue
# pipe的性能高于queue，从某种意义上来说，pipe是queue的子集， 但为什么说高于queue呢
# 为什么说高于queue呢，因为Queue为了做进程的同步加了很多锁，反而降低了我们的性能
# 要是只能两个进程，就优先考虑pipe
# def producer(pipe):
#     # 这里发送数据
#     pipe.send("bobby")
#
#
# def consumer(pipe):
#     # 这里接收send()发送过来的数据，有点像socket编程
#     print(pipe.recv())
#
#
# if __name__ == "__main__":
#     # recevie_pipe是收到，send_pipe发送管道, 这里实例化这两个
#     recevie_pipe, send_pipe = Pipe()
#
#     # pipe只能适用于两个进程
#     my_producer = Process(target=producer, args=(send_pipe, ))
#     my_consumer = Process(target=consumer, args=(recevie_pipe,))
#
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# ----------------------------------------------------------
"""
但是在某种情况下，我们还是能够像线程一样在进程间维护一个公共的内存模块或者公共的变量
它实际在Manager()里边

"""


# 这个p_dict就是progress_dict
def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":
    # 在Manager()里边就有我们python的很数据类型的集合，点进dict()里看就知道了
    progress_dict = Manager().dict()
    from queue import PriorityQueue

    first_progress = Process(target=add_data, args=(progress_dict, "bobby1", 22))
    second_progress = Process(target=add_data, args=(progress_dict, "bobby2", 23))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()

    print(progress_dict)

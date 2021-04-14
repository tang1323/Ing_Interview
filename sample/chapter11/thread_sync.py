"""
线程同步问题
"""

from threading import Lock, RLock, Condition    # 可重入的锁

# 在同一个线程里面，可以连续调用多次acquire， 一定要注意acquire的次数要和release的次数相等
total = 0
# 这里一把锁，我们一般用可重入锁比较多
lock = RLock()


def add():
    # 1. dosomething1
    # 2. io操作
    # 1. dosomething3
    # 引入锁，下面的方法也是引用这个锁，所以这里两个方法在竞争这一个锁，这样就做到同步问题
    # 也可以在参数上引入
    global lock
    global total
    for i in range(1000000):
        # 获取锁，如果获取到锁，就可以运行里面代码，其他的代码就不能运行
        lock.acquire()
        lock.acquire()  # 这就是重入锁
        total += 1
        # 这是释放锁，这里一定要记得释放锁，释放完之后其他代码是运行不了的
        lock.release()
        lock.release()  # 要记得释放掉


def desc():
    global total
    # 引入锁，上面的方法也是引用这个锁，所以这里两个方法在竞争这一个锁，这样就做到同步问题
    # 也可以在参数上引入
    global lock
    for i in range(1000000):
        # 获取锁，如果获取到锁，就可以运行里面代码，其他的代码就不能运行
        lock.acquire()
        total -= 1
        # 这是释放锁，这里一定要记得释放锁，释放完之后其他代码是运行不了的
        lock.release()


if __name__ == "__main__":
    import threading
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(total)

# 用锁的问题如下
# 1. 在多线程下，用锁会影响性能，只有在协程下要求才不会那么的高，因为协程是单线程的
# 2. 锁会引起死锁


# 死锁的情况 A（a，b）
"""
A(a、b)A线程的两个资源a, b
acquire (a)要是A拿到一把锁给a运行了，它要等b的锁来
acquire (b)这里在等待b锁

B(a、b)B线程的两个资源a, b
acquire (b)要是B拿到一把锁给b运行了，它要等a的锁来
acquire (a)这里在等待a锁

从上面可以看出，谁都 在等待谁，造成一个循环
"""


import threading

"""条件变量， 用于复杂的线程间同步"""


# 这不符合我们的期望，它不会天猫说一句，小爱说一句，而是开猫说完，小爱才说
# 所以在最下面得用上我们的条件变量锁
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         # 加一把锁
#         self.lock.acquire()
#         print("{} : 在 ".format(self.name))
#         # 释放锁
#         self.lock.release()
#
#         # 加一把锁
#         self.lock.acquire()
#         print("{} : 好啊 ".format(self.name))
#         # 释放锁
#         self.lock.release()
#
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#
#         # 加一把锁
#         self.lock.acquire()
#         print("{} : 小爱同学 ".format(self.name))
#         # 释放锁
#         self.lock.release()
#
#         # 加一把锁
#         self.lock.acquire()
#         print("{} : 我们来对古诗吧 ".format(self.name))
#         # 释放锁
#         self.lock.release()
#
#
# if __name__ == "__main__":
#     lock = threading.Lock()
#     xiaoai = XiaoAi(lock)
#     tianmao = TianMao(lock)
#
#     tianmao.start()
#     xiaoai.start()
# ---------------------------------------------------------------


# 通过condition完成协同读诗，你一句，我一句
class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            """
            如果天猫先start()。这里的notify就把信号发出去了
            但是小爱的wait()并没有接收到，因为还没start()起来，
            所以小爱先启动
            我们要知道，wait()只有notify()才能唤醒
            也就是说，谁先wait()，就先启动谁
            """
            self.cond.wait()    # 这是在等待天猫的notify()过来
            print("{} : 在 ".format(self.name))
            self.cond.notify()  # 这是通知天猫的wait()

            self.cond.wait()
            print("{} : 好啊 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 君住长江尾 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 共饮长江水 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 此恨何时已 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 定不负相思意 ".format(self.name))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        # 用acquire()也是一样的
        # 与release()成对出现
        # self.cond.acquire()
        """当天猫调用了with，会在这里加了一把锁，那在小爱那边的with就进不来了"""
        with self.cond:
            print("{} : 小爱同学 ".format(self.name))
            """
            如果天猫先start()。这里的notify就把信号发出去了
            但是小爱的wait()并没有接收到，因为还没start()起来，
            所以小爱先启动
            我们要知道，wait()只有notify()才能唤醒
            """
            # 当天猫运行到这里的时候，进入小爱的with,会通知小爱的wait()，
            # 那wait()不光分配到一把锁，还会把cond的锁给释放掉
            # 而天猫就释放锁
            self.cond.notify()  # 这是通知小爱的wait()
            self.cond.wait()    # 这是等待小爱的notify()过来

            print("{} : 我们来对古诗吧 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我住长江头 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 日日思君不见君 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 此水几时休 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 只愿君心似我心 ".format(self.name))
            self.cond.notify()
            self.cond.wait()
        # 与acquire()成对出现
        # self.cond.release()


if __name__ == "__main__":
    from concurrent import futures
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # 启动顺序很重要
    # 在调用with cond之后才能调用wait或者notify方法
    # condition有两层锁，
    # 一把底层锁会在线程调用了wait方法的时候释放，
    # 上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒
    xiaoai.start()
    tianmao.start()

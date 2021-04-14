
# 我们把可以通过for...in...
# 这类语句迭代读取一条数据供我们使用的对象称之为可迭代对象（Iterable）。
"""
    可迭代对象的本质
我们分析对可迭代对象进行迭代使用的过程，
发现每迭代一次（即在for...in...中每循环一次）
都会返回对象中的下一条数据，一直向后读取数据直到迭代了所有数据后结束。
那么，在这个过程中就应该有一个“人”去记录每次访问到了第几条数据，
以便每次迭代都可以返回下一条数据。
我们把这个能帮助我们进行数据迭代的“人”称为迭代器(Iterator)。

"""

"""
可迭代对象通过__iter__方法向我们提供一个迭代器
我们在迭代一个可迭代对象的时候，
实际上就是先获取该对象提供的一个迭代器，
然后通过这个迭代器来依次获取对象中的每一个数据.
"""
# from collections import Iterable
#
#
# class MyList(object):
#
#     def __init__(self):
#         self.container = []
#
#     def add(self, item):
#         self.container.append(item)
#
#     def __iter__(self):
#         """返回一个迭代器"""
#         pass
#
#
# if __name__ == "__main__":
#     mylist = MyList()
#     mylist.add(1)
#     print(isinstance(mylist, Iterable))

# ------------------------------------------
# iter()函数与next()函数

"""
list、tuple等都是可迭代对象，
我们可以通过iter()函数获取这些可迭代对象的迭代器。
然后我们可以对获取到的迭代器不断使用next()函数来获取下一条数据。
iter()函数实际上就是调用了可迭代对象的__iter__方法。
"""

# li = [11, 22, 33, 44, 55]
# li_iter = iter(li)
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))

# ----------------------------------------------
"""
实际上，在使用next()函数的时候，
调用的就是迭代器对象的__next__方法（Python3中是对象的__next__方法，
Python2中是对象的next()方法
"""


class MyList(object):

    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        """返回一个迭代器"""
        return MyIterator(self)


class MyIterator(object):

    def __init__(self, mylist):
        self.mylist = mylist
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.container):
            item = self.mylist.container[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)

    for i in mylist:
        print(i)












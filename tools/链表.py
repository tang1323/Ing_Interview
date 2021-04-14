

# 单链表
# class Solution:
#
#     def reverseList(self, head):
#         pre = None
#         # cur指向头结点
#         cur = head
#         while cur:
#             # cur不为空的时候cur指向下一个
#             nextnode = cur.next
#             # cur往回指
#             cur.next = pre
#             # cur让pre前移，就是cur给了pre
#             pre = cur
#             # 下个数据给了cur
#             cur = nextnode
#         return pre


# 实现先进先出队列
from _collections import deque


class Queue:
    # 初始化这个队列
    def __init__(self):
        self.items = deque()

    # 添加值到进来，往右边追加元素
    def append(self, val):
        return self.items.append(val)

    # 先进先出，用popleft来左边取元素
    def pop(self):
        return self.items.popleft()

    def empty(self):
        return len(self.items) == 0


def test_queue():
    q = Queue()
    q.append(0)
    q.append(1)
    q.append(2)
    print(q.pop())
    print(q.pop())
    print(q.pop())


test_queue()


# 栈，先进后出

# from collections import deque
#
#
# class Stack(object):
#     # 初始化这个栈
#     def __init__(self):
#         self.deque = deque()
#
#     # 用push添加数据
#     def push(self, value):
#         return self.deque.append(value)
#
#     # 用pop取数据
#     def pop(self):
#         return self.deque.pop()
#
#
# def test_queue():
#     q = Stack()
#     q.push(0)
#     q.push(1)
#     q.push(2)
#     print(q.pop())
#     print(q.pop())
#     print(q.pop())


# test_queue()






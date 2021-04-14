

# def bubble_sort(lists):
#     # 获取数据长度
#     count = len(lists) - 1
#
#     # N个元素遍历N次
#     for index in range(count, 0, -1):
#
#         # 第i个和第i+1依次对比
#         for sub_index in range(index):
#
#             # 大的元素冒上去
#             if lists[sub_index] > lists[sub_index+1]:
#                 lists[sub_index], lists[sub_index+1] = lists[sub_index+1], lists[sub_index]
#     return lists
#
#
# alist = [0, 10, 88, 19, 9, 1]
# print(bubble_sort(alist))


def bb_sort(lists):
    count = len(lists)

    for index in range(count-1):

        for sub_list in range(count-1-index):

            if lists[sub_list] > lists[sub_list+1]:
                lists[sub_list], lists[sub_list+1] = lists[sub_list+1], lists[sub_list]

    return lists


alist = [0, 10, 1, 19, 88, 2]

print(bb_sort(alist))






# def bb_sort(alist):
#     count = len(alist)
#
#     for index in range(count-1):
#         for sub_list in range(count-1-index):
#             if alist[sub_list] > alist[sub_list+1]:
#                 alist[sub_list], alist[sub_list+1] = alist[sub_list+1], alist[sub_list]
#
#     return alist
#
#
# alist = [0, 10, 1, 19, 88, 2]
# print(bb_sort(alist))
















# 快速排序
# def quick_sort(lists, left, right):
#
#     # 递归过程中， 发现left和right一致时，停止递归，直接返回列表
#     if left >= right:
#         return lists
#
#     # 定义游标
#     low = left
#     high = right
#
#     # 取参考标志，最左边的元素
#     key = lists[low]
#     while low < high:
#
#         # 这是右边的值大过关键字，才执行，因为不用动，右边是接收大的值，游标high减1就行了
#         while low < high and lists[high] >= key:
#             # 如果右边的值是大于关键字，那就是在原处，只是要把游标向后减1 ，因为high是从右边的9开始的，这个要依次减
#             # 本来就是在右边比，但是关键字是右边的值相比还是右边的大，则不动，游标high减1就行
#             high -= 1
#
#         # 这个是右边的值小于关键字才给左边，因为左边本来就是接收小的值
#         print("这个是未交换的左值{0},这个是未交换右值{1}".format(lists[low], lists[high]))
#         print("未交换之前是这样的排序{0}".format(lists))
#         # 否则右边小的值赋值给左边，因为左边是接收小的值
#         # 这个就是把在右侧小于关键字的值，放到左边来
#         lists[low] = lists[high]
#         print("这个是己交换的左值{0},这个是己交换的右值{1}".format(lists[low], lists[high]))
#         print("这个是己交换之后的排序{0}".format(lists))
#
#
#
#         # 这是左边的值小过关键字，才执行，因为不用动，左边是接收小的值，游标low加1就行了
#         while low < high and lists[low] <= key:
#             # 如果左边的值是小于关键字，那就是在原处，只是要把游标向前加1 ，因为low是从左边的0开始的，这个要依次加
#             # 本来就是在左边比较的，但是关键字跟左边的值相比还是左边的值大，那么左边的值就不变，游标加1就行
#             low += 1
#
#
#         # 当左边的值大于关键字的时候，那么就给到右边
#         # print("未交换之前是这样的排序{0}".format(lists))
#         # print("这个是未交换的左值{0},这个是未交换右值{1}".format(lists[low], lists[high]))
#         # 这个就是把在左侧大于关键字的值，放到到右边来
#         # # 否则左边大的值赋值给右边，因为右边是接收大的值
#         lists[high] = lists[low]
#         # print("这个是己交换的左值{0},这个是己交换的右值{1}".format(lists[low], lists[high]))
#         # print("这个是己交换之后的排序{0}".format(lists))
#
#
#     # 最后给high位置赋值
#     lists[high] = key
#     # 修理左侧元素
#     quick_sort(lists, left, low - 1)
#     # 修理右侧元素
#     quick_sort(lists, low + 1, right)
#     return lists
#
#
# alist = [45, 53, 18, 49, 36, 76, 13, 97, 36, 32]
# print(quick_sort(alist, 0, 9))









def bu_sored(lists, left, right):
    if left >= right:
        return lists

    # 分配游标
    low = left
    high = right

    # 取出关键字
    key = lists[low]
    while low < high:

        # 如果右边的值还大于关键字，那就不动，还放在右边，游标-1就行
        while low < high and lists[high] >= key:
            high -= 1

        # 否则右边小的值赋值给左边，因为左边是接收小的值
        lists[low] = lists[high]

        # 如果左边的值还小于关键字，那就不动，还放在左边， 游标+1就行
        while low < high and lists[low] <= key:
            low += 1

        # 否则左边大的值赋值给右边，因为右边是接收大的值
        lists[high] = lists[low]

    lists[high] = key
    bu_sored(lists, left, low - 1)
    bu_sored(lists, low + 1, right)
    return lists


alist = [45, 53, 18, 49, 36, 76, 13, 97, 36, 32]
print(bu_sored(alist, 0, 9))










# def bb_sored(lists, left, right):
#     if left >= right:
#         return lists
#
#     low = left
#     high = right
#
#     key = lists[low]
#     while low < high:
#         while low < high and lists[high] >= key:
#             high -= 1
#
#         lists[low] = lists[high]
#
#         while low < high and lists[low] <= key:
#             low += 1
#
#         lists[high] = lists[low]
#
#     lists[high] = key
#     bb_sored(lists, left, low - 1)
#     bb_sored(lists, low + 1, right)
#
#     return lists
#
# alist = [45, 53, 18, 49, 36, 76, 13, 97, 36, 32]
# print(bb_sored(alist, 0, 9))








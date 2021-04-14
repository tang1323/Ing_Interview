







def bin_search(arr, start, end, hkey):
    if start > end:
        return -1

    mid = int((end+start)/2)
    if arr[mid] > hkey:
        return bin_search(arr, start, mid - 1, hkey)
    if arr[mid] < hkey:
        return bin_search(arr, mid + 1, end, hkey)
    return mid


alist = [0, 1, 10, 88, 19, 9, 2, 7, 9, 5]
alist = sorted(alist)
print(alist)
print(bin_search(alist, 0, 9, 19))




















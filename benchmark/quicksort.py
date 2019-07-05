

import random


def quicksort(arr, start=0, end=0):
    if start >= end:
        return
    pindex = partition(arr, start, end)
    quicksort(arr, start, pindex - 1)
    quicksort(arr, pindex + 1, end)


def partition(arr, start, end):
    pivot = arr[end]
    pindex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex += 1
    arr[end], arr[pindex] = arr[pindex], arr[end]
    return pindex


arr = list(range(21))
random.shuffle(arr)
print(arr)
quicksort(arr, 0, len(arr) - 1)
print(arr)

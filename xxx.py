from bisect import bisect_left, bisect_right 

arr = [1,2,4,5,7,8]
i = bisect_right(arr, 3)
j = bisect_left(arr, 6)
print(i, j)

arr[i:j] = [3, 6]
print(arr)
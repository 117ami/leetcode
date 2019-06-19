#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#
# https://leetcode.com/problems/duplicate-zeros/description/
#
# algorithms
# Easy (58.86%)
# Total Accepted:    3.8K
# Total Submissions: 6.4K
# Testcase Example:  '[1,0,2,3,0,4,5,0]'
#
# Given a fixed length array arr of integers, duplicate each occurrence of
# zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return
# anything from your function.
#
#
#
# Example 1:
#
#
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,0,0,2,3,0,0,4]
#
#
# Example 2:
#
#
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,2,3]
#
#
#
#
# Note:
#
#
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9
#
#


class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i = j = -1
        while True:
            j += 1
            i += 2 if arr[j] == 0 else 1
            if i >= len(arr) - 1:
                break

        if i >= len(arr):
            arr[i - 1] = 0
            i -= 2
            j -= 1

        # print(i, j, arr)
        while i > -1:
            if arr[j] == 0:
                arr[i], arr[i - 1], i = 0, 0, i - 2
            else:
                arr[i], i = arr[j], i - 1
            j -= 1

        # return arr


s = Solution()
arr = [1, 0, 2, 3, 0, 4, 5, 0]
print(s.duplicateZeros(arr))

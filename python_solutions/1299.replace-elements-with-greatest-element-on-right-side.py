from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
#
# algorithms
# Easy (75.37%)
# Total Accepted:    2.4K
# Total Submissions: 3.1K
# Testcase Example:  '[17,18,5,4,6,1]'
#
# Given an array arr, replace every element in that array with the greatest
# element among the elements to its right, and replace the last element with
# -1.
#
# After doing so, return the array.
#
#
# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5
#
#


class Solution:
    def replaceElements(self, arr):
        curmax = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            tmp = arr[i]
            arr[i] = curmax
            curmax = max(curmax, tmp)
        arr[-1] = -1
        return arr


sol = Solution()
arr = [17, 18, 5, 4, 6, 1]
print(sol.replaceElements(arr))

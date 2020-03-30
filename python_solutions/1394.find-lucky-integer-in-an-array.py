from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#
# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/
#
# algorithms
# Easy (74.24%)
# Total Accepted:    9.1K
# Total Submissions: 12.5K
# Testcase Example:  '[2,2,3,4]'
#
# Given an array of integers arr, a lucky integer is an integer which has a
# frequency in the array equal to its value.
#
# Return a lucky integer in the array. If there are multiple lucky integers
# return the largest of them. If there is no lucky integer return -1.
#
#
# Example 1:
#
#
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] ==
# 2.
#
#
# Example 2:
#
#
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
#
#
# Example 3:
#
#
# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.
#
#
# Example 4:
#
#
# Input: arr = [5]
# Output: -1
#
#
# Example 5:
#
#
# Input: arr = [7,7,7,7,7,7,7]
# Output: 7
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500
#
#


class Solution:
    def findLucky(self, ns):
        cnt = Counter(ns)
        return max([k for k, v in cnt.items() if k == v] or [-1])


ns = [2, 3, 4, 3, 2, 2]
sol = Solution()
print(sol.findLucky(ns))

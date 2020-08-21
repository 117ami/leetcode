from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007
#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#
# https://leetcode.com/problems/kth-missing-positive-number/description/
#
# algorithms
# Easy (49.89%)
# Total Accepted:    6.4K
# Total Submissions: 12.9K
# Testcase Example:  '[2,3,4,7,11]\n5'
#
# Given an array arr of positive integers sorted in a strictly increasing
# order, and an integer k.
#
# Find the k^th positive integer that is missing from this array.
#
#
# Example 1:
#
#
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The
# 5^th missing positive integer is 9.
#
#
# Example 2:
#
#
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2^nd missing
# positive integer is 6.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length
#
#


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cc = set(arr)
        i = 1
        while True:
            if i not in cc:
                k -= 1
            if k == 0:
                return i
            i += 1
        return i


sol = Solution()


arr = [2, 3, 4, 7, 11]
k = 5
# arr = [1, 2, 3, 4]
# k = 2
print(sol.findKthPositive(arr, k))

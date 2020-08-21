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
# @lc app=leetcode id=1524 lang=python3
#
# [1524] Number of Sub-arrays With Odd Sum
#
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/
#
# algorithms
# Medium (35.74%)
# Total Accepted:    7.3K
# Total Submissions: 20.1K
# Testcase Example:  '[1,3,5]\r'
#
# Given an array of integers arr. Return the number of sub-arrays with odd
# sum.
#
# As the answer may grow large, the answer must be computed modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: arr = [1,3,5]
# Output: 4
# Explanation: All sub-arrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.
#
#
# Example 2:
#
#
# Input: arr = [2,4,6]
# Output: 0
# Explanation: All sub-arrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.
#
#
# Example 3:
#
#
# Input: arr = [1,2,3,4,5,6,7]
# Output: 16
#
#
# Example 4:
#
#
# Input: arr = [100,100,99,99]
# Output: 4
#
#
# Example 5:
#
#
# Input: arr = [7]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 100
#
#


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even = odd = res = 0
        for a in arr:
            if a % 2 == 0:
                even += 1
            else:
                even, odd = odd, even
                odd += 1
            res += odd
        return res % MOD


sol = Solution()


arr = [1, 3, 5]
# arr = [2, 4, 6]
arr = [1, 2, 3, 4, 5, 6, 7]
# arr = [100, 100, 99, 99]
# arr = [7]
print(sol.numOfSubarrays(arr))

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
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1191 lang=python3
#
# [1191] K-Concatenation Maximum Sum
#
# https://leetcode.com/problems/k-concatenation-maximum-sum/description/
#
# algorithms
# Medium (25.86%)
# Total Accepted:    10.3K
# Total Submissions: 39.9K
# Testcase Example:  '[1,2]\n3'
#
# Given an integer array arr and an integer k, modify the array by repeating it
# k times.
#
# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2,
# 1, 2, 1, 2].
#
# Return the maximum sub-array sum in the modified array. Note that the length
# of the sub-array can be 0 and its sum in that case is 0.
#
# As the answer can be very large, return the answer modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: arr = [1,2], k = 3
# Output: 9
#
#
# Example 2:
#
#
# Input: arr = [1,-2,1], k = 5
# Output: 2
#
#
# Example 3:
#
#
# Input: arr = [-1,-2], k = 7
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^5
# 1 <= k <= 10^5
# -10^4 <= arr[i] <= 10^4
#
#
#


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def Kadane(arr):
            best_sum = cur_sum = 0
            for a in arr:
                cur_sum = max(cur_sum + a, a)
                best_sum = max(best_sum, cur_sum)
            return best_sum
        res = Kadane(arr * 2) + (k - 2) * \
            max(sum(arr), 0) if k > 1 else Kadane(arr)
        return res % (10**9 + 7)


sol = Solution()
print(sol.kConcatenationMaxSum([1,2],3))

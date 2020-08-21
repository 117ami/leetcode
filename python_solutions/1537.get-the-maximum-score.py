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
# @lc app=leetcode id=1537 lang=python3
#
# [1537] Get the Maximum Score
#
# https://leetcode.com/problems/get-the-maximum-score/description/
#
# algorithms
# Hard (35.72%)
# Total Accepted:    6.1K
# Total Submissions: 17K
# Testcase Example:  '[2,4,5,8,10]\n[4,6,8,9]'
#
# You are given two sorted arrays of distinct integers na and nb.
#
# A valid path is defined as follows:
#
#
# Choose array na or nb to traverse (from index-0).
# Traverse the current array from left to right.
# If you are reading any value that is present in na and nb you are
# allowed to change your path to the other array. (Only one repeated value is
# considered in the valid path).
#
#
# Score is defined as the sum of uniques values in a valid path.
#
# Return the maximum score you can obtain of all possible valid paths.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
#
#
# Input: na = [2,4,5,8,10], nb = [4,6,8,9]
# Output: 30
# Explanation: Valid paths:
# [2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from na)
# [4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nb)
# The maximum is obtained with the path in green [2,4,6,8,10].
#
#
# Example 2:
#
#
# Input: na = [1,3,5,7,9], nb = [3,5,100]
# Output: 109
# Explanation: Maximum sum is obtained with the path [1,3,5,100].
#
#
# Example 3:
#
#
# Input: na = [1,2,3,4,5], nb = [6,7,8,9,10]
# Output: 40
# Explanation: There are no common elements between na and nb.
# Maximum sum is obtained with the path [6,7,8,9,10].
#
#
# Example 4:
#
#
# Input: na = [1,4,5,8,9,11,19], nb = [2,3,4,11,12]
# Output: 61
#
#
#
# Constraints:
#
#
# 1 <= na.length <= 10^5
# 1 <= nb.length <= 10^5
# 1 <= na[i], nb[i] <= 10^7
# na and nb are strictly increasing.
#
#
#


class Solution:
    def maxSum(self, na: List[int], nb: List[int]) -> int:
        i = j = s1 = s2 = 0
        m, n = len(na), len(nb)
        
        while i < m or j < n:
            if i < m and (j == n or na[i] < nb[j]):
                s1 += na[i]
                i += 1

            elif j < n and (i == m or nb[j] < na[i]):
                s2 += nb[j]
                j += 1

            else:
                s1 = s2 = max(s1, s2) + na[i]
                i += 1
                j += 1

        return max(s1, s2) % MOD


sol = Solution()


na = [2, 4, 5, 8, 10]
nb = [4, 6, 8, 9]
na = [1, 3, 5, 7, 9]
nb = [3, 5, 100]
# na = [1, 2, 3, 4, 5]
# nb = [6, 7, 8, 9, 10]
# na = [1, 4, 5, 8, 9, 11, 19]
# nb = [2, 3, 4, 11, 12]
na, nb = [5, 9, 11, 15, 17, 25, 29], [6, 12, 15]
print(sol.maxSum(na, nb))

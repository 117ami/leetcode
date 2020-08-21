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
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (29.67%)
# Total Accepted:    478.6K
# Total Submissions: 1.6M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
#
# Example 1:
#
#
# Input: 2.00000, 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: 2.10000, 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
#
#
# Note:
#
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
#
#
#


class Solution:
    def myPow(self, x, n):
        if abs(x) < 1e-40:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        lower = self.myPow(x, n // 2)
        if n % 2 == 0:
            return lower * lower
        if n % 2 == 1:
            return lower * lower * x


sol = Solution()


# inputs = 2.00000, 10
# inputs = 2.10000, 3
# inputs = 2.00000, -2
# print(sol.myPow())

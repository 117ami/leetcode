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
# @lc app=leetcode id=1556 lang=python3
#
# [1556] Thousand Separator
#
# https://leetcode.com/problems/thousand-separator/description/
#
# algorithms
# Easy (62.02%)
# Total Accepted:    7.1K
# Total Submissions: 11.5K
# Testcase Example:  '987'
#
# Given an integer n, add a dot (".") as the thousands separator and return it
# in string format.
#
#
# Example 1:
#
#
# Input: n = 987
# Output: "987"
#
#
# Example 2:
#
#
# Input: n = 1234
# Output: "1.234"
#
#
# Example 3:
#
#
# Input: n = 123456789
# Output: "123.456.789"
#
#
# Example 4:
#
#
# Input: n = 0
# Output: "0"
#
#
#
# Constraints:
#
#
# 0 <= n < 2^31
#
#
#
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)[::-1]
        return '.'.join(map(lambda i: s[i:i + 3], range(0, len(s), 3)))[::-1]


sol = Solution()

n = 987
n = 1234
# n = 123456789
# n = 0
print(sol.thousandSeparator(n))

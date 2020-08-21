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
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (45.85%)
# Total Accepted:    297.2K
# Total Submissions: 637.4K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

ps = [0]

class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        
        while len(ps) <= n:
            m = len(ps)
            cur = float('inf')
            for i in range(1, m+1):
                if i * i > m:
                    break
                cur = min(cur, ps[m - i * i] + 1)
            ps.append(cur)
        # print(ps)
        return ps[n]


sol = Solution()
print(sol.numSquares(18))

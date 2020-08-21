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
# @lc app=leetcode id=1447 lang=python3
#
# [1447] Simplified Fractions
#
# https://leetcode.com/problems/simplified-fractions/description/
#
# algorithms
# Medium (57.67%)
# Total Accepted:    6.3K
# Total Submissions: 10.8K
# Testcase Example:  '2\r'
#
# Given an integer n, return a list of all simplified fractions between 0 and 1
# (exclusive) such that the denominator is less-than-or-equal-to n. The
# fractions can be in any order.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: ["1/2"]
# Explanation: "1/2" is the only unique fraction with a denominator
# less-than-or-equal-to 2.
#
# Example 2:
#
#
# Input: n = 3
# Output: ["1/2","1/3","2/3"]
#
#
# Example 3:
#
#
# Input: n = 4
# Output: ["1/2","1/3","1/4","2/3","3/4"]
# Explanation: "2/4" is not a simplified fraction because it can be simplified
# to "1/2".
#
# Example 4:
#
#
# Input: n = 1
# Output: []
#
#
#
# Constraints:
#
#
# 1 <= n <= 100
#
#


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        rset = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    rset.append(f"{j}/{i}")
        return rset


sol = Solution()
print(sol.simplifiedFractions(4))

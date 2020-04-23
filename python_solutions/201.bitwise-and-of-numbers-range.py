from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (37.24%)
# Total Accepted:    111.1K
# Total Submissions: 295.8K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
# 
# Example 1:
# 
# 
# Input: [5,7]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: [0,1]
# Output: 0
#
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0: return 0
        return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1 if n > m else m 
        

sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))




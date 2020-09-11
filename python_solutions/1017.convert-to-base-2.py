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
# @lc app=leetcode id=1017 lang=python3
#
# [1017] Convert to Base -2
#
# https://leetcode.com/problems/convert-to-base-2/description/
#
# algorithms
# Medium (58.94%)
# Total Accepted:    11.8K
# Total Submissions: 20K
# Testcase Example:  '2'
#
# Given a number N, return a string consisting of "0"s and "1"s that represents
# its value in base -2 (negative two).
#
# The returned string must have no leading zeroes, unless the string is
# "0".
#
#
#
#
# Example 1:
#
#
# Input: 2
# Output: "110"
# Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
#
#
#
# Example 2:
#
#
# Input: 3
# Output: "111"
# Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
#
#
#
# Example 3:
#
#
# Input: 4
# Output: "100"
# Explantion: (-2) ^ 2 = 4
#
#
#
#
# Note:
#
#
# 0 <= N <= 10^9
#
#
#
#
#
class Solution:
    def baseNeg2(self, N: int) -> str:
        neg = [1 << i for i in range(1, 32, 2)]
        for m in neg:
            if N & m: N += m * 2
        return bin(N)[2:]


sol = Solution()
print(sol.baseNeg2(2))

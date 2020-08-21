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
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
#
# algorithms
# Easy (53.35%)
# Total Accepted:    6K
# Total Submissions: 11.3K
# Testcase Example:  '3\n7'
#
# Given two non-negative integers low and high. Return the count of odd numbers
# between low and high (inclusive).
#
#
# Example 1:
#
#
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
#
# Example 2:
#
#
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
#
#
# Constraints:
#
#
# 0 <= low <= high <= 10^9
#
#


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


sol = Solution()


low = 3
high = 7
# low = 8, high = 10
print(sol.countOdds(low, high))

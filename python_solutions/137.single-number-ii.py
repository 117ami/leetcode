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
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (49.81%)
# Total Accepted:    225.5K
# Total Submissions: 444.8K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#
#


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
            print(n, ones, twos)
        return ones


sol = Solution()
nums = [0, 1, 0, 1, 0, 1, 99]
nums = [2, 3, 2, 3, 2, 3, 7]
print(sol.singleNumber(nums))

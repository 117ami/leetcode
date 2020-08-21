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
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (61.15%)
# Total Accepted:    146.2K
# Total Submissions: 235.9K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
#
# Example:
#
#
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
#
# Note:
#
#
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
#
#


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(lambda a, b: a ^ b, nums)
        rightmost = (xor & (xor - 1)) ^ xor
        a = b = 0
        for n in nums:
            if n & rightmost:
                a = a ^ n
            else:
                b = b ^ n

        return [a, b]


sol = Solution()
inputs = [1, 2, 1, 3, 2, 5]
print(sol.singleNumber(inputs))

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
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (44.96%)
# Total Accepted:    211K
# Total Submissions: 468.4K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
# '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# Example:
#
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
#
#
# Constraints:
#
#
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 0 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= i <= j < nums.length
#
#
#
class NumArray:
    def __init__(self, nums: List[int]):
        self.ptr = nums
        for i in range(1, len(nums)):
            self.ptr[i] += self.ptr[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.ptr[j] if i == 0 else self.ptr[j] - self.ptr[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


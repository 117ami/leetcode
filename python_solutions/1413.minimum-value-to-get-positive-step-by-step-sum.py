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
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/
#
# algorithms
# Easy (64.46%)
# Total Accepted:    5.8K
# Total Submissions: 9.1K
# Testcase Example:  '[-3,2,-3,4,2]\r'
#
# Given an array of integers nums, you start with an initial positive value
# startValue.
#
# In each iteration, you calculate the step by step sum of startValue plus
# elements in nums (from left to right).
#
# Return the minimum positive value of startValue such that the step by step
# sum is never less than 1.
#
#
# Example 1:
#
#
# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step
# by step sum is less than 1.
# ⁠               step by step sum
# startValue = 4 | startValue = 5 | nums
# (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
# (1 +2 ) = 3  | (2 +2 ) = 4    |   2
# (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
# (0 +4 ) = 4  | (1 +4 ) = 5    |   4
# (4 +2 ) = 6  | (5 +2 ) = 7    |   2
#
#
# Example 2:
#
#
# Input: nums = [1,2]
# Output: 1
# Explanation: Minimum start value should be positive.
#
#
# Example 3:
#
#
# Input: nums = [1,-2,-3]
# Output: 5
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
#
#


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        i32_sum = 0
        i32_min = float('inf')
        for n in nums:
            i32_sum += n
            i32_min = min(i32_min, i32_sum)
        return max(0, i32_min * -1) + 1


sol = Solution()
nums = [-3, 2, -3, 4, 2]
nums = [1, -2, -3]
print(sol.minStartValue(nums))

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
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (37.13%)
# Total Accepted:    244.7K
# Total Submissions: 658.5K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        _sum = j = 0 
        res = 1 << 32
        for i in range(len(nums)):
            if nums[i] >= s: return 1
            _sum += nums[i]
            while _sum >= s:
                res = min(res, i - j + 1)
                _sum -= nums[j]
                j += 1
        return res if res < 1 << 32 else 0

sol = Solution()
s, nums = 7, [2,3,1,2,4,3]
print(sol.minSubArrayLen(s, nums))


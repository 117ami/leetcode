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
# @lc app=leetcode id=1509 lang=python3
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/
#
# algorithms
# Medium (50.75%)
# Total Accepted:    6.1K
# Total Submissions: 11.9K
# Testcase Example:  '[5,3,2,4]'
#
# Given an array nums, you are allowed to choose one element of nums and change
# it by any value in one move.
#
# Return the minimum difference between the largest and smallest value of nums
# after perfoming at most 3 moves.
#
#
# Example 1:
#
#
# Input: nums = [5,3,2,4]
# Output: 0
# Explanation: Change the array [5,3,2,4] to [2,2,2,2].
# The difference between the maximum and minimum is 2-2 = 0.
#
# Example 2:
#
#
# Input: nums = [1,5,0,10,14]
# Output: 1
# Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1].
# The difference between the maximum and minimum is 1-0 = 1.
#
#
# Example 3:
#
#
# Input: nums = [6,6,0,1,1,4,6]
# Output: 2
#
#
# Example 4:
#
#
# Input: nums = [1,5,6,14,15]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        heapq.heapify(nums)
        nums = heapq.nsmallest(4, nums) + heapq.nlargest(4, nums)[::-1]
        res = float('inf')
        for i in range(4):
            res = min(res, nums[i - 4] - nums[i])
        return res


sol = Solution()

nums = [5, 3, 2, 4]
nums = [20, 54, 81, 82, 95]
# nums = [1,5,0,10,14]
# nums = [6,6,0,1,1,4,6]
# nums = [1,5,6,14,15]
print(sol.minDifference(nums))

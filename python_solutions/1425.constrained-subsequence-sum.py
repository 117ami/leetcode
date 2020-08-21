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
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subsequence Sum
#
# https://leetcode.com/problems/constrained-subsequence-sum/description/
#
# algorithms
# Hard (43.60%)
# Total Accepted:    6.9K
# Total Submissions: 15.8K
# Testcase Example:  '[10,2,-10,5,20]\n2'
#
# Given an integer array nums and an integer k, return the maximum sum of a
# non-empty subsequence of that array such that for every two consecutive
# integers in the subsequence, nums[i] and nums[j], where i < j, the condition
# j - i <= k is satisfied.
#
# A subsequence of an array is obtained by deleting some number of elements
# (can be zero) from the array, leaving the remaining elements in their
# original order.
#
#
# Example 1:
#
#
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
#
#
# Example 2:
#
#
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest
# number.
#
#
# Example 3:
#
#
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
#
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        '''d is a decreasing deque, caching the previous k maximum sum 
        '''
        d = deque()
        ans = float('-inf')
        for i in range(len(nums)):
            nums[i] += d[0] if d else 0
            ans = max(ans, nums[i])
            # both >= and > are fine 
            while d and nums[i] >= d[-1]:
                d.pop()
            if nums[i] > 0:
                d.append(nums[i])
            while d and i >= k and d[0] == nums[i - k]:
                d.popleft()
        return ans


sol = Solution()


# nums = [10,2,-10,5,20],  = 2
# nums = [-1,-2,-3], k = 1÷
nums = [10, -2, -10, -5, 20]
k = 2
print(sol.constrainedSubsetSum(nums, k))

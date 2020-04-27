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
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subset Sum
#
# https://leetcode.com/problems/constrained-subset-sum/description/
#
# algorithms
# Hard (30.17%)
# Total Accepted:    3.2K
# Total Submissions: 8K
# Testcase Example:  '[10,2,-10,5,20]\n2'
#
# Given an integer array nums and an integer k, return the maximum sum of a
# non-empty subset of that array such that for every two consecutive integers
# in the subset, nums[i] and nums[j], where i < j, the condition j - i <= k is
# satisfied.
#
# A subset of an array is obtained by deleting some number of elements (can be
# zero) from the array, leaving the remaining elements in their original
# order.
#
#
# Example 1:
#
#
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subset is [10, 2, 5, 20].
#
#
# Example 2:
#
#
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subset must be non-empty, so we choose the largest number.
#
#
# Example 3:
#
#
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subset is [10, -2, -5, 20].
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
        deq = deque()
        res = nums[0]
        for i in range(len(nums)):
            nums[i] += deq[0] if len(deq) else 0
            res = max(res, nums[i])
            while len(deq) and nums[i] >= deq[-1]:
                deq.pop()
            if nums[i] > 0:
                deq.append(nums[i])
            if i >= k and len(deq) and deq[0] == nums[i - k]:
                deq.popleft()
        return res


sol = Solution()
nums = [10, 2, -10, 5, 20]
k = 2
print(sol.constrainedSubsetSum(nums, k))

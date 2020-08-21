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
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (24.48%)
# Total Accepted:    124.7K
# Total Submissions: 509.5K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to a multiple of k, that is, sums up to n*k where n is also an
# integer.
#
#
#
# Example 1:
#
#
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
#
#
# Example 2:
#
#
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
#
#
#
# Constraints:
#
#
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
#
#
#


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cc = {0: -1}
        carry = 0
        for i, n in enumerate(nums):
            carry += n
            if k != 0:
                carry %= k
            if carry in cc:
                if i - cc.get(carry, 10001) > 1:
                    return True
            else:
                cc[carry] = i

        return False


sol = Solution()
nums = [23, 2, 6, 4, 7]
k = 0
nums = [1, 0]
k = 2
print(sol.checkSubarraySum(nums, k))

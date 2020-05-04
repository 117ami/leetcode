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
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/
#
# algorithms
# Medium (68.17%)
# Total Accepted:    9.2K
# Total Submissions: 13.4K
# Testcase Example:  '[1,0,0,0,1,0,0,1]\r\n2\r'
#
# Given an array nums of 0s and 1s and an integer k, return True if all 1's are
# at least k places away from each other, otherwise return False.
#
#
# Example 1:
#
#
#
#
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
#
#
# Example 2:
#
#
#
#
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.
#
# Example 3:
#
#
# Input: nums = [1,1,1,1,1], k = 0
# Output: true
#
#
# Example 4:
#
#
# Input: nums = [0,1,0,1], k = 1
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= k <= nums.length
# nums[i] is 0 or 1
#
#


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        preidx = -k-1
        for i, n in enumerate(nums):
            if n == 1 and i - preidx <= k:
                return False
            if n == 1:
                preidx = i
        return True


sol = Solution()

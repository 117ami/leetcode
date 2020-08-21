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
# @lc app=leetcode id=1546 lang=python3
#
# [1546] Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
#
# https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/description/
#
# algorithms
# Medium (33.66%)
# Total Accepted:    5.1K
# Total Submissions: 13.1K
# Testcase Example:  '[1,1,1,1,1]\n2'
#
# Given an array nums and an integer target.
#
# Return the maximum number of non-empty non-overlapping subarrays such that
# the sum of values in each subarray is equal to target.
#
#
# Example 1:
#
#
# Input: nums = [1,1,1,1,1], target = 2
# Output: 2
# Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum
# equals to target(2).
#
#
# Example 2:
#
#
# Input: nums = [-1,3,5,1,4,2,-9], target = 6
# Output: 2
# Explanation: There are 3 subarrays with sum equal to 6.
# ([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
#
# Example 3:
#
#
# Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
# Output: 3
#
#
# Example 4:
#
#
# Input: nums = [0,0,0], target = 0
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 0 <= target <= 10^6
#
#
#


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        presum, preidx, res = 0, -1, 0
        cc = {0: -1}
        for i, n in enumerate(nums):
            presum += n
            # print(cc, preidx)
            if presum - target in cc and cc[presum - target] >= preidx:
                # print(presum, preidx)
                res += 1
                preidx = i
            cc[presum] = i
        return res


sol = Solution()


nums = [1, 1, 1, 1, 1]
target = 2
# nums = [-1, 3, 5, 1, 4, 2, -9]
# target = 6
# nums = [-2, 6, 6, 3, 5, 4, 1, 2, 8]
# target = 10
# nums = [0, 0, 0]
# target = 0
print(sol.maxNonOverlapping(nums, target))

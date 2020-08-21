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
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#
# https://leetcode.com/problems/number-of-good-pairs/description/
#
# algorithms
# Easy (91.81%)
# Total Accepted:    11.8K
# Total Submissions: 13K
# Testcase Example:  '[1,2,3,1,1,3]'
#
# Given an array of integers nums.
#
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#
# Return the number of good pairs.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
#
# Example 2:
#
#
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#
#


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        cc = defaultdict(int)
        for n in nums:
            ans += cc[n]
            cc[n] += 1
        return ans


sol = Solution()


nums = [1, 2, 3, 1, 1, 3]
nums = [1, 1, 1, 1]
# nums = [1,2,3]
print(sol.numIdenticalPairs(nums))

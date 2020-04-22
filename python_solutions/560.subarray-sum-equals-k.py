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
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.54%)
# Total Accepted:    236.3K
# Total Submissions: 540.6K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
# Input:nums = [1,1,1], k = 2
# Output: 2
#
#
#
# Note:
#
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
#
#
#
#


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = i32sum = 0
        cc = defaultdict(int)
        cc[0] = 1
        for n in nums:
            i32sum += n
            res += cc[i32sum - k]
            cc[i32sum] += 1
        return res


sol = Solution()
nums = [1,1,1]
k = 2
print(sol.subarraySum(nums, k))

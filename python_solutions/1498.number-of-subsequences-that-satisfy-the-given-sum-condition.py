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
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
#
# algorithms
# Medium (27.12%)
# Total Accepted:    4.4K
# Total Submissions: 12.1K
# Testcase Example:  '[3,5,6,7]\n9'
#
# Given an array of integers nums and an integer target.
#
# Return the number of non-empty subsequences of nums such that the sum of the
# minimum and maximum element on it is less or equal than target.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
#
#
# Example 2:
#
#
# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can
# have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
#
# Example 3:
#
#
# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them don't satisfy
# the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).
#
#
# Example 4:
#
#
# Input: nums = [5,2,4,1,7,6,8], target = 16
# Output: 127
# Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= target <= 10^6
#
#
#

sh = [0] * (10**5 + 5)
sh[0] = 1

for i in range(1, 10**5 + 5):
    sh[i] = (sh[i - 1] << 1) % MOD


class Solution:
    def numSubseq(self, ns: List[int], t: int) -> int:
        ns.sort()
        l, r = 0, len(ns) - 1
        ans = 0
        while l <= r:
            if ns[l] + ns[r] > t:
                r -= 1
            else:
                ans += sh[r - l]
                l += 1
        return ans % MOD


sol = Solution()
nums = [3, 5, 6, 7]
target = 9
# nums = [3,3,6,8]; target = 10
# nums = [2,3,3,4,6,7]; target = 12
# nums = [5,2,4,1,7,6,8]; target = 16
nums, target=[1], 1
print(sol.numSubseq(nums, target))

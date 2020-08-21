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
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (48.68%)
# Total Accepted:    39.5K
# Total Submissions: 81.1K
# Testcase Example:  '[3,4,2]'
#
# Given an array nums of integers, you can perform operations on the array.
#
# In each operation, you pick any nums[i] and delete it to earn nums[i] points.
# After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
#
# You start with 0 points. Return the maximum number of points you can earn by
# applying such operations.
#
# Example 1:
#
#
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation:
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
#
#
#
#
# Example 2:
#
#
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation:
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
#
#
#
#
# Note:
#
#
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].
#
#
#
#
#
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cc = Counter(nums)
        nums = sorted(list(set(nums)))
        res = [0]
        for i, n in enumerate(nums):
            if i > 0 and n - 1 == nums[i - 1]:
                res.append(max(res[-1], res[-2] + n * cc[n]))
            else:
                res.append(res[-1] + n * cc[n])
        return max(res)


sol = Solution()
nums = [3, 4, 2]
# nums = [2, 2, 3, 3, 3, 4]
print(sol.deleteAndEarn(nums))

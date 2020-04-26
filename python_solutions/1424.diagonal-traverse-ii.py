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
# @lc app=leetcode id=1424 lang=python3
#
# [1424] Diagonal Traverse II
#
# https://leetcode.com/problems/diagonal-traverse-ii/description/
#
# algorithms
# Medium (25.11%)
# Total Accepted:    4.4K
# Total Submissions: 13.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a list of lists of integers, nums, return all elements of nums in
# diagonal order as shown in the below images.
#
# Example 1:
#
#
#
#
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
#
#
# Example 2:
#
#
#
#
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
#
#
# Example 3:
#
#
# Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
# Output: [1,4,2,5,3,8,6,9,7,10,11]
#
#
# Example 4:
#
#
# Input: nums = [[1,2,3,4,5,6]]
# Output: [1,2,3,4,5,6]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i].length <= 10^5
# 1 <= nums[i][j] <= 10^9
# There at most 10^5 elements in nums.
#
#
#


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        cc = defaultdict(list)
        max_len = 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                cc[i + j].append(nums[i][j])
                max_len = max(max_len, i + j)

        return [n for k in range(max_len + 1) for n in cc[k][::-1]]


sol = Solution()
nums = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
print(sol.findDiagonalOrder(nums))

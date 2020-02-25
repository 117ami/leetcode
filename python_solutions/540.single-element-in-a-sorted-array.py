from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (57.66%)
# Total Accepted:    76.7K
# Total Submissions: 133K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# 
# 
# Note: Your solution should run in O(log n) time and O(1) space.
# 
#
class Solution:
    def singleNonDuplicate(self, nums):
        # return reduce(lambda a, b: a ^ b, nums)
        low, high, mid = 0, len(nums) - 1, 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid 
        return nums[low]


sol = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))



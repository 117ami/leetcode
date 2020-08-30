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
# @lc app=leetcode id=1567 lang=python3
#
# [1567] Maximum Length of Subarray With Positive Product
#
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/description/
#
# algorithms
# Medium (27.12%)
# Total Accepted:    4.4K
# Total Submissions: 14.9K
# Testcase Example:  '[1,-2,-3,4]'
#
# Given an array of integers nums, find the maximum length of a subarray where
# the product of all its elements is positive.
# 
# A subarray of an array is a consecutive sequence of zero or more values taken
# out of that array.
# 
# Return the maximum length of a subarray with positive product.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which
# has a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the
# product 0 which is not positive.
# 
# Example 3:
# 
# 
# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or
# [-2,-3].
# 
# 
# Example 4:
# 
# 
# Input: nums = [-1,2]
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: nums = [1,2,3,5,-6,4,0,10]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def solve(i, j):
            neg_count = sum(1 if n < 0 else 0 for n in nums[i:j+1])
            if neg_count % 2 == 0: 
                return j - i + 1 
            x = next(itertools.dropwhile(lambda k: nums[k] > 0, range(i, j + 1)), j)
            y = next(itertools.dropwhile(lambda k: nums[k] > 0, range(j, i - 1, -1)), i)
            # print(neg_count, i, j, x, y)
            return max(y - i, j - x)

        i = j = 0
        res = 0 
        nums.append(0)
        while j < len(nums):
            # print(j)
            while nums[j] != 0 and j < len(nums): j += 1
            res = max(res, solve(i, j - 1))
            print(res, i, j)
            i = j + 1
            j += 1
        return res 

        

sol = Solution()


nums = [1,-2,-3,4]
nums = [0,1,-2,-3,-4]
nums = [-1,-2,-3,0,1]
nums = [-1,2]
nums = [1,2,3,5,-6,4,0,10]
print(sol.getMaxLen(nums))
# x = next(itertools.dropwhile(lambda i: nums[i] > 0, range(len(nums))))
# y = next(itertools.dropwhile(lambda i: nums[i] > 0, range(len(nums)-1, -1, -1)))
# print(x, y)

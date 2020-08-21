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
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#
# https://leetcode.com/problems/shuffle-the-array/description/
#
# algorithms
# Easy (92.15%)
# Total Accepted:    9.8K
# Total Submissions: 10.6K
# Testcase Example:  '[2,5,1,3,4,7]\n3'
#
# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn].
# 
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is
# [2,3,5,4,1,7].
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3
# 
#
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return itertools.chain(*zip(nums[:n], nums[n:]))

sol = Solution()
print(list(sol.shuffle([2,5,1,3,4,7], 3)))



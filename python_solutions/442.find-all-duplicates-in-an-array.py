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
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (66.07%)
# Total Accepted:    184.5K
# Total Submissions: 276K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]
#
#


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ''' For number n, flip the number at position n-1 to negative. 
        If the number at position n-1 is already negative, n is the number that occurs twice.
        '''
        res = []
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                res.append(abs(n))
            nums[idx] = - nums[idx]
        return res


sol = Solution()


inputs = [4, 3, 2, 7, 8, 2, 3, 1]
print(sol.findDuplicates(inputs))

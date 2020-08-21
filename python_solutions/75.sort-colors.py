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
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (45.62%)
# Total Accepted:    465.3K
# Total Submissions: 1M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this
# problem.
#
# Example:
#
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Follow up:
#
#
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
#
#
#


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, write, blue = 0, 0, len(nums) - 1
        while write <= blue:
            if nums[write] == 0:
                nums[red], nums[write] = nums[write], nums[red]
                write += 1
                red += 1
            elif nums[write] == 1:
                write += 1
            else:
                nums[blue], nums[write] = nums[write], nums[blue]
                blue -= 1


sol = Solution()

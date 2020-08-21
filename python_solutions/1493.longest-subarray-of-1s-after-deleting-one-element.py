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
#@lc app = leetcode id = 1493 lang = python3
#
#[1493] Longest Subarray of 1's After Deleting One Element
#
#https: // leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
#
#algorithms
#Medium(55.50 %)
#Total Accepted : 5.7K
#Total Submissions : 10.1K
#Testcase Example : '[1,1,0,1]'
#
#Given a binary array nums, you should delete one element from it.
#
#Return the size of the longest non - empty subarray containing only 1's in the
#resulting array.
#
#Return 0 if there is no such subarray.
#
#
#Example 1:
#
#
#Input : nums = [1, 1, 0, 1]
#Output : 3
#Explanation : After deleting the number in position 2, [1, 1, 1] contains 3
#numbers with value of 1's.
#
#Example 2:
#
#
#Input : nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
#Output : 5
#Explanation : After deleting the number in position 4, [0, 1, 1, 1, 1, 1, 0, 1]
#longest subarray with value of 1's is[1, 1, 1, 1, 1].
#
#Example 3:
#
#
#Input : nums = [1, 1, 1]
#Output : 2
#Explanation : You must delete one element.
#
#Example 4:
#
#
#Input : nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
#Output : 4
#
#
#Example 5:
#
#
#Input : nums = [0, 0, 0]
#Output : 0
#
#
#
#Constraints:
#
#
# 1 <= nums.length <= 10 ^ 5
#nums[i] is either 0 or 1.
#
#
#


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        k = 1
        for j, n in enumerate(nums):
            if n == 0:
                k -= 1
            if k < 0:
                k += nums[i] == 0
                i += 1
        return j - i


sol = Solution()
nums = [1, 1, 0, 1]
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
nums = [1, 1, 1]
nums = [1,1,0,0,1,1,1,0,1]
#nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
#nums = [0, 0, 0]
print(sol.longestSubarray(nums))

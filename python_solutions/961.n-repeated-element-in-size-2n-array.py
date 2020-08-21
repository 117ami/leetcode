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
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/
#
# algorithms
# Easy (73.70%)
# Total Accepted:    118K
# Total Submissions: 160.2K
# Testcase Example:  '[1,2,3,3]'
#
# In a array A of size 2N, there are N+1 unique elements, and exactly one of
# these elements is repeated N times.
# 
# Return the element repeated N times.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,3]
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: [2,1,2,5,3,2]
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: [5,1,5,2,5,3,5,4]
# Output: 5
# 
# 
# 
# 
# Note:
# 
# 
# 4 <= A.length <= 10000
# 0 <= A[i] < 10000
# A.length is even
# 
# 
# 
# 
# 
#
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(2, len(A)):
            if A[i] == A[i-1] or A[i] == A[i-2]:
                return A[i]
        return A[0]
        

sol = Solution()


inputs =   [1,2,3,3]
inputs =   [2,1,2,5,3,2]
inputs =   [5,1,5,2,5,3,5,4]
# print(sol.repeatedNTimes())

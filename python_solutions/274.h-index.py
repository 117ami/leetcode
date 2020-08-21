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
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (35.43%)
# Total Accepted:    151.9K
# Total Submissions: 425.3K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 3, 0, 6, 1, 5 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
# 
#
class Solution:
    def hIndex(self, cs: List[int]) -> int:
        cs.sort()
        n = len(cs)
        if n == 0: return 0
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) >> 1
            if cs[mid] == n - mid:
                return cs[mid]
            elif cs[mid] > n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - (r + 1)
        

sol = Solution()
cs = [0, 1, 3, 5, 6]
cs = [3,0,6,1,5]
print(sol.hIndex(cs))


from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#
# https://leetcode.com/problems/rank-transform-of-an-array/description/
#
# algorithms
# Easy (60.06%)
# Total Accepted:    4.5K
# Total Submissions: 7.5K
# Testcase Example:  '[40,10,20,30]'
#
# Given an array of integers arr, replace each element with its rank.
# 
# The rank represents how large the element is. The rank has the following
# rules:
# 
# 
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their
# rank must be the same.
# Rank should be as small as possible.
# 
# 
# 
# Example 1:
# 
# 
# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second
# smallest. 30 is the third smallest.
# 
# Example 2:
# 
# 
# Input: arr = [100,100,100]
# Output: [1,1,1]
# Explanation: Same elements share the same rank.
# 
# 
# Example 3:
# 
# 
# Input: arr = [37,12,28,9,100,56,80,5,12]
# Output: [5,3,4,2,8,6,7,1,3]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= arr.length <= 10^5
# -10^9 <= arr[i] <= 10^9
# 
#
class Solution:
    def arrayRankTransform(self, arr):
        # sarr = sorted(list(set(arr)))
        # d = {n:i+1 for i, n in enumerate(sarr)}
        # print(sorted({*arr}))
        # # return list(map(lambda x:d[x], arr))
        return [*map({n:rank for rank, n in enumerate(sorted({*arr}), 1)}.get, arr)]

        

sol = Solution()
arr = [37,12,28,9,100,56,80,5,12]
arr = [1,1,1]
print(sol.arrayRankTransform(arr))


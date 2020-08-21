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
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#
# https://leetcode.com/problems/count-good-triplets/description/
#
# algorithms
# Easy (77.89%)
# Total Accepted:    7.4K
# Total Submissions: 9.5K
# Testcase Example:  '[3,0,1,1,9,7]\n7\n2\n3'
#
# Given an array of integers arr, and three integers a, b and c. You need to
# find the number of good triplets.
# 
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are
# true:
# 
# 
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# 
# 
# Where |x| denotes the absolute value of x.
# 
# Return the number of good triplets.
# 
# 
# Example 1:
# 
# 
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1),
# (0,1,1)].
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= arr.length <= 100
# 0 <= arr[i] <= 1000
# 0 <= a, b, c <= 1000
# 
#
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt=0
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        cnt += 1
        return cnt
        

sol = Solution()


arr = [3,0,1,1,9,7]; a = 7; b = 2; c = 3
# arr = [1,1,2,2,3], a = 0, b = 0, c = 1
print(sol.countGoodTriplets(arr,a,b,c))

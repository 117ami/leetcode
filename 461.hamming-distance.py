from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (71.14%)
# Total Accepted:    283.7K
# Total Submissions: 398.8K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 2^31.
# 
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are
# different.
# 
# 
#
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        

sol = Solution()



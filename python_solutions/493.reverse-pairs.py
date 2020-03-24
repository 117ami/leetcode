from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right, insort
from functools import reduce, lru_cache
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
# https://leetcode.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (24.43%)
# Total Accepted:    33.4K
# Total Submissions: 136.8K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an array nums, we call (i, j) an important reverse pair if i < j and
# nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
#
#
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
#
#
# Note:
#
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
#
#
#


class Solution:
    def reversePairs(self, ns):
        aux = []
        res = 0
        for n in ns:
            res += len(aux) - bisect_right(aux, 2 * n)
            j = bisect_right(aux, n)
            aux[j:j] = [n]
            # res += len(aux) - idx
            # insort(aux, n)
        return res


sol = Solution()
ns = [2, 4, 3, 5, 1]
# ns = [1, 3, 2, 3, 1]
print(sol.reversePairs(ns))

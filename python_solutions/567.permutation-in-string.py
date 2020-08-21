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
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (40.75%)
# Total Accepted:    88.7K
# Total Submissions: 217.3K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
#
#
#
# Example 1:
#
#
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
# Example 2:
#
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
#
#
#
# Note:
#
#
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
#
#
#


class Solution:
    def checkInclusion(self, s, t):
        ls, lt = len(s), len(t)
        if ls > lt: return False
        hs = sum(map(hash, s))
        ht = sum(map(hash, t[:ls]))
        if hs == ht: return True

        for i in range(lt - ls):
            ht += hash(t[ls + i]) - hash(t[i])
            # print(ht, hs)
            if ht == hs:
                return True
        return False


sol = Solution()
s1, s2 = "ab", "eidbaoaoo"
print(sol.checkInclusion(s1, s2))

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
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (34.09%)
# Total Accepted:    628.8K
# Total Submissions: 1.8M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#
class KMP():
    def get_lhp(self, t: str) -> List[int]:
        '''Compute the length of LHP for each t[:i], i \in [1..len(t)],
        where a prefix-suffix of t is a substring, u, of t s.t., t.startswith(u) and t.endswith(u).
        And proper means, len(u) < len(t), i.e., u != t
        '''
        j, lhp = 0, [0] * len(t)
        for i in range(1, len(t)):
            while j > 0 and t[i] != t[j]:
                j = lhp[j-1]
                
            if t[i] == t[j]:
                j += 1
                lhp[i] = j
        return lhp

    def pattern_search(self, text: str, pat: str) -> List[int]:
        """KMP (Knuth Morris Pratt) Pattern Searching
        Return a list of indexes i, such that t occurs in s starting from i.
        """
        j = 0
        lhp, res = self.get_lhp(pat), []
        for i in range(len(text)):
            while j > 0 and text[i] != pat[j]:
                j = lhp[j-1]

            if text[i] == pat[j]:
                j += 1 

            if j == len(pat):
                res.append(i + 1 - len(pat))
                j = lhp[j - 1]
        return res

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)        

sol = Solution()
print(sol.strStr("a", "0"))


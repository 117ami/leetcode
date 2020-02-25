from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#
# https://leetcode.com/problems/repeated-string-match/description/
#
# algorithms
# Easy (32.03%)
# Total Accepted:    83.7K
# Total Submissions: 261.2K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# Given two strings A and B, find the minimum number of times A has to be
# repeated such that B is a substring of it. If no such solution, return -1.
# 
# For example, with A = "abcd" and B = "cdabcdab".
# 
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a
# substring of it; and B is not a substring of A repeated two times
# ("abcdabcd").
# 
# Note:
# The length of A and B will be between 1 and 10000.
# 
#
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if set(B) - set(A): return -1 
        
        x = A[::]
        i = 1
        while len(x) <= 2 * len(B) or i < 5:
            if B in x: return i 
            x += A
            i += 1 
        return -1 

sol = Solution()
A, B = "abcd", "cdabcdab"
A, B = "abcbc", "cabcbca"
print(sol.repeatedStringMatch(A, B))



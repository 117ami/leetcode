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
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (60.82%)
# Total Accepted:    200.9K
# Total Submissions: 330.5K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
#
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
#
# Example 1:
#
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#
#
# Example 2:
#
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
#
# Note:
#
#
# The input string length won't exceed 1000.
#
#
#
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(i, j):
            return next(
                filter(lambda k: i < (k - j) or s[k] != s[i - (k - j)],
                       range(j, len(s))), len(s)) - j
        return sum(map(lambda i: check(i, i) + check(i, i + 1), range(len(s))))
        


sol = Solution()
print(sol.countSubstrings("aaa"))

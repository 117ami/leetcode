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
# @lc app=leetcode id=1392 lang=python3
#
# [1392] Longest Happy Prefix
#
# https://leetcode.com/problems/longest-happy-prefix/description/
#
# algorithms
# Hard (39.14%)
# Total Accepted:    7.4K
# Total Submissions: 18.8K
# Testcase Example:  '"level"'
#
# A string is called a happy prefix if is a non-empty prefix which is also a
# suffix (excluding itself).
# 
# Given a string s. Return the longest happy prefix of s .
# 
# Return an empty string if no such prefix exists.
# 
# 
# Example 1:
# 
# 
# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"),
# and suffix ("l", "el", "vel", "evel"). The largest prefix which is also
# suffix is given by "l".
# 
# 
# Example 2:
# 
# 
# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can
# overlap in the original string.
# 
# 
# Example 3:
# 
# 
# Input: s = "leetcodeleet"
# Output: "leet"
# 
# 
# Example 4:
# 
# 
# Input: s = "a"
# Output: ""
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
# 
# 
#
class Solution:
    def longestPrefix(self, t: str) -> str:
        j, lps = 0, [0] * len(t)

        for i in range(1, len(t)):
            while j > 0 and t[i] != t[j]: j = lps[j - 1]
            if t[i] == t[j]: j, lps[i] = j + 1, j + 1

        return t[:lps[-1]]
        

sol = Solution()
s = "leetcodeleet"
# s = "ababab"
print(sol.longestPrefix(s))

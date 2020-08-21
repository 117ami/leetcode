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
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (41.63%)
# Total Accepted:    209.4K
# Total Submissions: 502.6K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#

# method 2 using itertools.accumulate
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp = len(s), len(p)
        if ls < lp:
            return []
        hp = sum(map(hash, p))
        hs = [0] + list(itertools.accumulate(map(hash, s)))
        res = [i for i in range(ls - lp + 1) if hs[i + lp] - hs[i] == hp]
        return res

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp = len(s), len(p)
        if ls < lp:
            return
        # if (ls := len(s)) < (lp := len(p)): return
        hp = sum(map(hash, p))
        hs = sum(map(hash, s[:lp]))
        res = [0] if hp == hs else []

        for i in range(ls - lp):
            hs += hash(s[lp + i]) - hash(s[i])
            if hp == hs:
                res.append(i + 1)
        return res


sol = Solution()
s, p = "abab", "ab"
s, p = "cbaebabacd", "abc"
p_hash = list(map(hash, p))
print(p_hash)
print(sol.findAnagrams(s, p))
print(hash('a'))

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
# @lc app=leetcode id=1371 lang=python3
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
#
# algorithms
# Medium (57.88%)
# Total Accepted:    7.2K
# Total Submissions: 12.4K
# Testcase Example:  '"eleetminicoworoep"'
#
# Given the string s, return the size of the longest substring containing each
# vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must
# appear an even number of times.
#
#
# Example 1:
#
#
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each
# of the vowels: e, i and o and zero of the vowels: a and u.
#
#
# Example 2:
#
#
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
#
#
# Example 3:
#
#
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because
# all vowels: a, e, i, o and u appear zero times.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 x 10^5
# s contains only lowercase English letters.
#
#


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bit = dict(zip('aeiou', range(5)))
        mask, res = 0, 0
        cc = [-1] + [len(s)] * 32
        for i, c in enumerate(s):
            if c in bit:
                mask ^= 1 << bit[c]
            res = max(res, i - cc[mask])
            cc[mask] = min(cc[mask], i)
        return res


sol = Solution()


s = "eleetminicoworoep"
s = "leetcodeisgreat"
s = "bcbcbc"
s="yopumzgd"
print(sol.findTheLongestSubstring(s))

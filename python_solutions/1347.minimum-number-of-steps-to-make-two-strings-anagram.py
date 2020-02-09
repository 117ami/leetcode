from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
#
# algorithms
# Medium (76.58%)
# Total Accepted:    5.8K
# Total Submissions: 7.6K
# Testcase Example:  '"bab"\n"aba"'
#
# Given two equal-size strings s and t. In one step you can choose any
# character of t and replace it with another character.
#
# Return the minimum number of steps to make t an anagram of s.
#
# An Anagram of a string is a string that contains the same characters with a
# different (or the same) ordering.
#
#
# Example 1:
#
#
# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of
# s.
#
#
# Example 2:
#
#
# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters
# to make t anagram of s.
#
#
# Example 3:
#
#
# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams.
#
#
# Example 4:
#
#
# Input: s = "xxyyzz", t = "xxyyzz"
# Output: 0
#
#
# Example 5:
#
#
# Input: s = "friend", t = "family"
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 50000
# s.length == t.length
# s and t contain lower-case English letters only.
#
#
#


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        return sum(max(0, c2[k] - c1.get(k, 0)) for k in c2)
        # for k, v in c1.items():
        #     if k in c2:
        #         c2[k] = max(0, c2[k] - v)
        # return sum(c2.values())


sol = Solution()
s, t = 'bab', 'aba'
s, t = "leetcode", "practice"
s, t = "anagram", "mangaar"
s, t = "friend", "family"
print(sol.minSteps(s, t))

from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#
# https://leetcode.com/problems/find-and-replace-in-string/description/
#
# algorithms
# Medium (48.50%)
# Total Accepted:    28.1K
# Total Submissions: 57.9K
# Testcase Example:  '"abcd"\n[0, 2]\n["a", "cd"]\n["eee", "ffff"]'
#
# To some string S, we will perform some replacement operations that replace
# groups of letters with new ones (not necessarily the same size).
#
# Each replacement operation has 3 parameters: a starting index i, a source
# word x and a target word y.  The rule is that if x starts at position i in
# the original string S, then we will replace that occurrence of x with y.  If
# not, we do nothing.
#
# For example, if we have S = "abcd" and we have some replacement operation i =
# 2, x = "cd", y = "ffff", then because "cd" starts at position 2 in the
# original string S, we will replace it with "ffff".
#
# Using another example on S = "abcd", if we have both the replacement
# operation i = 0, x = "ab", y = "eee", as well as another replacement
# operation i = 2, x = "ec", y = "ffff", this second operation does nothing
# because in the original string S[2] = 'c', which doesn't match x[0] = 'e'.
#
# All these operations occur simultaneously.  It's guaranteed that there won't
# be any overlap in replacement: for example, S = "abc", indexes = [0, 1],
# sources = ["ab","bc"] is not a valid test case.
#
# Example 1:
#
#
# Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets =
# ["eee","ffff"]
# Output: "eeebffff"
# Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
# "cd" starts at index 2 in S, so it's replaced by "ffff".
#
#
# Example 2:
#
#
# Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets =
# ["eee","ffff"]
# Output: "eeecd"
# Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
# "ec" doesn't starts at index 2 in the original S, so we do nothing.
#
#
# Notes:
#
#
# 0 <= indexes.length = sources.length = targets.length <= 100
# 0 < indexes[i] < S.length <= 1000
# All characters in given inputs are lowercase letters.
#
#
#
#
#


class Solution:
    def findReplaceString(self, s, idx, ss, t):
        hh = {n: i for i, n in enumerate(idx)}
        i, st = 0, ""
        while i < len(s):
            if i in hh and s[i:i + len(ss[hh[i]])] == ss[hh[i]]:
                st, i = st + t[hh[i]], i + len(ss[hh[i]])
            else:
                st, i = st + s[i], i + 1
        return st


# sol = Solution()
# s, idx, ss, t = "abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]
# # s, idx, ss, t = "abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]
# print(sol.findReplaceString(s, idx, ss, t))

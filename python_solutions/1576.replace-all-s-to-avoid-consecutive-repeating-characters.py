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
# @lc app=leetcode id=1576 lang=python3
#
# [1576] Replace All ?'s to Avoid Consecutive Repeating Characters
#
# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/
#
# algorithms
# Easy (45.88%)
# Total Accepted:    6.7K
# Total Submissions: 14.6K
# Testcase Example:  '"?zs"'
#
# Given a string s containing only lower case English letters and the '?'
# character, convert all the '?' characters into lower case letters such that
# the final string does not contain any consecutive repeating characters. You
# cannot modify the non '?' characters.
#
# It is guaranteed that there are no consecutive repeating characters in the
# given string except for '?'.
#
# Return the final string after all the conversions (possibly zero) have been
# made. If there is more than one solution, return any of them. It can be shown
# that an answer is always possible with the given constraints.
#
#
# Example 1:
#
#
# Input: s = "?zs"
# Output: "azs"
# Explanation: There are 25 solutions for this problem. From "azs" to "yzs",
# all are valid. Only "z" is an invalid modification as the string will consist
# of consecutive repeating characters in "zzs".
#
# Example 2:
#
#
# Input: s = "ubv?w"
# Output: "ubvaw"
# Explanation: There are 24 solutions for this problem. Only "v" and "w" are
# invalid modifications as the strings will consist of consecutive repeating
# characters in "ubvvw" and "ubvww".
#
#
# Example 3:
#
#
# Input: s = "j?qg??b"
# Output: "jaqgacb"
#
#
# Example 4:
#
#
# Input: s = "??yw?ipkj?"
# Output: "acywaipkja"
#
#
#
# Constraints:
#
#
#
# 1 <= s.length <= 100
#
#
# s contains only lower case English letters and '?'.
#
#
#
#
import random


class Solution:
    def modifyString(self, s: str) -> str:
        cs = list(s)
        left = 'z'
        for i, c in enumerate(cs):
            if c == '?':
                cur = left
                while cur == left or (i < len(cs) - 1 and cur == cs[i + 1]):
                    cur = chr(random.randint(1, 26) + 97)
                cs[i] = cur
            left = cs[i]
        return ''.join(cs)


sol = Solution()

s = "?zs"
s = "ubv?w"
s = "j?qg??b"
s = "??yw?ipkj?"
print(sol.modifyString(s))

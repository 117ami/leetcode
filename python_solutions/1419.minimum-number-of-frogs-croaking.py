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
# @lc app=leetcode id=1419 lang=python3
#
# [1419] Minimum Number of Frogs Croaking
#
# https://leetcode.com/problems/minimum-number-of-frogs-croaking/description/
#
# algorithms
# Medium (46.29%)
# Total Accepted:    11.9K
# Total Submissions: 25.8K
# Testcase Example:  '"croakcroak"'
#
# Given the string croakOfFrogs, which represents a combination of the string
# "croak" from different frogs, that is, multiple frogs can croak at the same
# time, so multiple “croak” are mixed. Return the minimum number of different
# frogs to finish all the croak in the given string.
#
# A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’
# sequentially. The frogs have to print all five letters to finish a croak. If
# the given string is not a combination of valid "croak" return -1.
#
#
# Example 1:
#
#
# Input: croakOfFrogs = "croakcroak"
# Output: 1
# Explanation: One frog yelling "croak" twice.
#
#
# Example 2:
#
#
# Input: croakOfFrogs = "crcoakroak"
# Output: 2
# Explanation: The minimum number of frogs is two.
# The first frog could yell "crcoakroak".
# The second frog could yell later "crcoakroak".
#
#
# Example 3:
#
#
# Input: croakOfFrogs = "croakcrook"
# Output: -1
# Explanation: The given string is an invalid combination of "croak" from
# different frogs.
#
#
# Example 4:
#
#
# Input: croakOfFrogs = "croakcroa"
# Output: -1
#
#
#
# Constraints:
#
#
# 1 <= croakOfFrogs.length <= 10^5
# All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
#
#
#
cc = dict(zip('croak', range(5)))


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = 0
        frogs = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
                frogs = max(frogs, c - k)
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            elif ch == 'k':
                k += 1

            if not c >= r >= o >= a >= k:
                return -1

        return frogs if c == r == o == a == k else -1


sol = Solution()
croakOfFrogs = "croakcroak"
# croakOfFrogs = "crcoakroak"
# croakOfFrogs = "croakcrook"
# croakOfFrogs = "croakcroa"
print(sol.minNumberOfFrogs(croakOfFrogs))

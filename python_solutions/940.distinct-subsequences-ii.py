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
# @lc app=leetcode id=940 lang=python3
#
# [940] Distinct Subsequences II
#
# https://leetcode.com/problems/distinct-subsequences-ii/description/
#
# algorithms
# Hard (41.38%)
# Total Accepted:    9.7K
# Total Submissions: 23.5K
# Testcase Example:  '"abc"'
#
# Given a string S, count the number of distinct, non-empty subsequences of S
# .
#
# Since the result may be large, return the answer modulo 10^9 + 7.
#
#
#
# Example 1:
#
#
# Input: "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc",
# and "abc".
#
#
#
# Example 2:
#
#
# Input: "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and
# "aba".
#
#
#
# Example 3:
#
#
# Input: "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
#
#
#
#
#
#
#
#
# Note:
#
#
# S contains only lowercase letters.
# 1 <= S.length <= 2000
#
#
#
#
#
#
#
#
#
#


class Solution:
    def distinctSubseqII(self, S: str) -> int:
        _endswith = [0] * 26
        for c in S:
            _endswith[ord(c) - 97] = sum(_endswith) + 1
        return sum(_endswith) % (10**9 + 7)


sol = Solution()
print(sol.distinctSubseqII('abc'))

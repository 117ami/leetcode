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
# @lc app=leetcode id=1573 lang=python3
#
# [1573] Number of Ways to Split a String
#
# https://leetcode.com/problems/number-of-ways-to-split-a-string/description/
#
# algorithms
# Medium (27.87%)
# Total Accepted:    3.9K
# Total Submissions: 14K
# Testcase Example:  '"10101"'
#
# Given a binary string s (a string consisting only of '0's and '1's), we can
# split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).
#
# Return the number of ways s can be split such that the number of characters
# '1' is the same in s1, s2, and s3.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: s = "10101"
# Output: 4
# Explanation: There are four ways to split s in 3 parts where each part
# contain the same number of letters '1'.
# "1|010|1"
# "1|01|01"
# "10|10|1"
# "10|1|01"
#
#
# Example 2:
#
#
# Input: s = "1001"
# Output: 0
#
#
# Example 3:
#
#
# Input: s = "0000"
# Output: 3
# Explanation: There are three ways to split s in 3 parts.
# "0|0|00"
# "0|00|0"
# "00|0|0"
#
#
# Example 4:
#
#
# Input: s = "100100010100110"
# Output: 12
#
#
#
# Constraints:
#
#
# s[i] == '0' or s[i] == '1'
# 3 <= s.length <= 10^5
#
#
#
class Solution:
    def numWays(self, s: str) -> int:
        cnt = s.count('1')
        if cnt % 3 > 0: return 0
        if cnt == 0: return (len(s) - 1) * (len(s) - 2) // 2 % MOD
        
        a, b, i, k = 0, 0, 0, 0
        while k < cnt // 3:
            k += 1 if s[i] == '1' else 0
            i += 1
        while s[i] != '1':
            a += 1
            i += 1

        while k < cnt * 2 // 3:
            k += 1 if s[i] == '1' else 0
            i += 1
        while s[i] != '1':
            b += 1
            i += 1
        return (a + 1) * (b + 1) % MOD


sol = Solution()

s = "10101"
s = "1001"
s = "0000"
# s = "100100010100110"
print(sol.numWays(s))

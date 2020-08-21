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
# @lc app=leetcode id=1513 lang=python3
#
# [1513] Number of Substrings With Only 1s
#
# https://leetcode.com/problems/number-of-substrings-with-only-1s/description/
#
# algorithms
# Medium (40.12%)
# Total Accepted:    12K
# Total Submissions: 30K
# Testcase Example:  '"0110111"'
#
# Given a binary string s (a string consisting only of '0' and '1's).
#
# Return the number of substrings with all characters 1's.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.
#
# Example 2:
#
#
# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.
#
#
# Example 3:
#
#
# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.
#
#
# Example 4:
#
#
# Input: s = "000"
# Output: 0
#
#
#
# Constraints:
#
#
# s[i] == '0' or s[i] == '1'
# 1 <= s.length <= 10^5
#
#


class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        for c in s.split('0'):
            n = len(c)
            ans += (n * (n + 1) // 2) % MOD
        return ans


sol = Solution()


s = "0110111"
print(sol.numSub(s))

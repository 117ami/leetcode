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
# @lc app=leetcode id=1540 lang=python3
#
# [1540] Can Convert String in K Moves
#
# https://leetcode.com/problems/can-convert-string-in-k-moves/description/
#
# algorithms
# Medium (25.07%)
# Total Accepted:    4.4K
# Total Submissions: 16.7K
# Testcase Example:  '"input"\n"ouput"\n9'
#
# Given two strings s and t, your goal is to convert s into t in k moves or
# less.
#
# During the i^th (1 <= i <= k) move you can:
#
#
# Choose any index j (1-indexed) from s, such that 1 <= j <= s.length and j has
# not been chosen in any previous move, and shift the character at that index i
# times.
# Do nothing.
#
#
# Shifting a character means replacing it by the next letter in the alphabet
# (wrapping around so that 'z' becomes 'a'). Shifting a character by i means
# applying the shift operations i times.
#
# Remember that any index j can be picked at most once.
#
# Return true if it's possible to convert s into t in no more than k moves,
# otherwise return false.
#
#
# Example 1:
#
#
# Input: s = "input", t = "ouput", k = 9
# Output: true
# Explanation: In the 6th move, we shift 'i' 6 times to get 'o'. And in the 7th
# move we shift 'n' to get 'u'.
#
#
# Example 2:
#
#
# Input: s = "abc", t = "bcd", k = 10
# Output: false
# Explanation: We need to shift each character in s one time to convert it into
# t. We can shift 'a' to 'b' during the 1st move. However, there is no way to
# shift the other characters in the remaining moves to obtain t from s.
#
#
# Example 3:
#
#
# Input: s = "aab", t = "bbb", k = 27
# Output: true
# Explanation: In the 1st move, we shift the first 'a' 1 time to get 'b'. In
# the 27th move, we shift the second 'a' 27 times to get 'b'.
#
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 10^5
# 0 <= k <= 10^9
# s, t contain only lowercase English letters.
#
#


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        bit = dict(zip(string.ascii_lowercase, range(26)))
        m, n = len(s), len(t)
        if m != n:
            return False
        diffs = sorted((bit[t[i]] + 26 - bit[s[i]]) % 26 for i in range(m))
        move = 0
        for i, d in enumerate(diffs):
            if d == 0:
                continue
            if i > 0 and d == diffs[i - 1]:
                move += 26
            else:
                move = d
            if move > k:
                return False
        return True


sol = Solution()


s, t, k = "input", "ouput", 9
# s, t, k = "abc", "bcd", 10
s, t, k = "aab", "bbb", 27
# s, t, k = 'a'*100000, 'z'*100000, 2599999
# print((26 * 99999))
print(sol.canConvertString(s, t, k))

from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=761 lang=python3
#
# [761] Special Binary String
#
# https://leetcode.com/problems/special-binary-string/description/
#
# algorithms
# Hard (54.28%)
# Total Accepted:    7.1K
# Total Submissions: 13.1K
# Testcase Example:  '"11011000"'
#
#
# Special binary strings are binary strings with the following two properties:
#
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
#
# Given a special string S, a move consists of choosing two consecutive,
# non-empty, special substrings of S, and swapping them.  (Two strings are
# consecutive if the last character of the first string is exactly one index
# before the first character of the second string.)
#
# At the end of any number of moves, what is the lexicographically largest
# resulting string possible?
#
#
# Example 1:
#
# Input: S = "11011000"
# Output: "11100100"
# Explanation:
# The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
# This is the lexicographically largest string possible after some number of
# swaps.
#
#
#
# Note:
# S has length at most 50.
# S is guaranteed to be a special binary string as defined above.
#
#


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        res = []
        i = cnt = 0
        for j, c in enumerate(S):
            cnt += 1 if c == '1' else -1
            if cnt == 0:
                res.append(
                    ''.join(['1', self.makeLargestSpecial(S[i + 1:j]), '0']))
                i = j + 1
        return ''.join(sorted(res)[::-1])


sol = Solution()
S = "11011000"
print(sol.makeLargestSpecial(S))

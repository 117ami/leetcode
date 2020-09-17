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
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#
# https://leetcode.com/problems/shifting-letters/description/
#
# algorithms
# Medium (44.68%)
# Total Accepted:    25.1K
# Total Submissions: 56.2K
# Testcase Example:  '"abc"\n[3,5,9]'
#
# We have a string S of lowercase letters, and an integer array shifts.
#
# Call the shift of a letter, the next letter in the alphabet, (wrapping around
# so that 'z' becomes 'a').
#
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
#
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x
# times.
#
# Return the final string after all such shifts to S are applied.
#
# Example 1:
#
#
# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation:
# We start with "abc".
# After shifting the first 1 letters of S by 3, we have "dbc".
# After shifting the first 2 letters of S by 5, we have "igc".
# After shifting the first 3 letters of S by 9, we have "rpl", the answer.
#
#
# Note:
#
#
# 1 <= S.length = shifts.length <= 20000
# 0 <= shifts[i] <= 10 ^ 9
#
#
#
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        n, cnt = len(shifts), 0
        res = [''] * n
        for i in range(n - 1, -1, -1):
            cnt = (cnt + shifts[i]) % 26
            res[i] = chr((cnt + ord(S[i]) - 97) % 26 + 97)
        return ''.join(res)


sol = Solution()
S, shifts = "abc", [3, 5, 9]
print(sol.shiftingLetters(S, shifts))

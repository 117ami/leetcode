from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (41.59%)
# Total Accepted:    137.5K
# Total Submissions: 330.4K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# 
# -1 : My number is lower
# ⁠1 : My number is higher
# ⁠0 : Congrats! You got it!
# 
# 
# Example :
# 
# 
# 
# Input: n = 10, pick = 6
# Output: 6
# 
# 
# 
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) >> 1
            if guess(mid) == 1: lo = mid + 1
            else: hi = mid 
        return lo


sol = Solution()



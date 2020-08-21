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
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#
# https://leetcode.com/problems/domino-and-tromino-tiling/description/
#
# algorithms
# Medium (38.83%)
# Total Accepted:    14.3K
# Total Submissions: 36.7K
# Testcase Example:  '3'
#
# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape.
# These shapes may be rotated.
#
#
# XX  <- domino
#
# XX  <- "L" tromino
# X
#
#
# Given N, how many ways are there to tile a 2 x N board? Return your answer
# modulo 10^9 + 7.
#
# (In a tiling, every square must be covered by a tile. Two tilings are
# different if and only if there are two 4-directionally adjacent cells on the
# board such that exactly one of the tilings has both squares occupied by a
# tile.)
#
#
#
# Example:
# Input: 3
# Output: 5
# Explanation:
# The five different ways are listed below, different letters indicates
# different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY
#
# Note:
#
#
# N  will be in range [1, 1000].
#
#
#
#
#
cc = {0: 0, 1: 1, 2: 2, 3: 5}
MOD = 10 ** 9 + 7


class Solution:
    def numTilings(self, N: int) -> int:
        a, b, c, m = 1, 0, 0, 1000000007
        for _ in range(N):
            a, b, c = (a + b + c) % m, a, (2 * b + c) % m
        return a


sol = Solution()
print(sol.numTilings(50))

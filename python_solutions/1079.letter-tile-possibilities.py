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
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#
# https://leetcode.com/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (74.63%)
# Total Accepted:    21.9K
# Total Submissions: 29.3K
# Testcase Example:  '"AAB"'
#
# You have a set of tiles, where each tile has one letter tiles[i] printed on
# it.  Return the number of possible non-empty sequences of letters you can
# make.
#
#
#
# Example 1:
#
#
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
#
#
#
# Example 2:
#
#
# Input: "AAABBC"
# Output: 188
#
#
#
#
#
# Note:
#
#
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
#
#


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = [0] * 26
        for c in tiles:
            counts[ord(c) - 65] += 1
        self.res = 0

        def rec():
            for i in range(26):
                if counts[i]:
                    counts[i] -= 1
                    self.res += 1
                    rec()
                    counts[i] += 1
        rec()
        return self.res


sol = Solution()
print(sol.numTilePossibilities("AAABBC"))

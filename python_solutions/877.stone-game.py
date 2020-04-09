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
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#
# https://leetcode.com/problems/stone-game/description/
#
# algorithms
# Medium (63.34%)
# Total Accepted:    47.3K
# Total Submissions: 74.7K
# Testcase Example:  '[5,3,4,5]'
#
# Alex and Lee play a game with piles of stones.  There are an even number of
# piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].
#
# The objective of the game is to end with the most stones.  The total number
# of stones is odd, so there are no ties.
#
# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes
# the entire pile of stones from either the beginning or the end of the row.
# This continues until there are no more piles left, at which point the person
# with the most stones wins.
#
# Assuming Alex and Lee play optimally, return True if and only if Alex wins
# the game.
#
#
#
# Example 1:
#
#
# Input: [5,3,4,5]
# Output: true
# Explanation:
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10
# points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win
# with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we
# return true.
#
#
#
#
# Note:
#
#
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
#
#


class Solution:
    # Method 1 2D DP
    # def stoneGame(self, piles: List[int]) -> bool:
    #     n = len(piles)
    #     dp = [[0] * n for _ in range(n)]
    #     for i in range(n):
    #         dp[i][i] = piles[i]

    #     for d in range(1, n):
    #         for i in range(n - d):
    #             dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])

    #     return dp[0][-1] > 0

    # Method 2 1D dp
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        cur = piles[:]
        for length in range(1, n):
            pre = cur[:]
            for i in range(n - length):
                j = i + length
                cur[j] = max(piles[i] - pre[j], piles[j] - pre[j - 1])
        return cur[-1] > 0


sol = Solution()
piles = [5, 3, 4, 5]
print(sol.stoneGame(piles))

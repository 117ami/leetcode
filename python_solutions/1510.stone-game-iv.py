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
# @lc app=leetcode id=1510 lang=python3
#
# [1510] Stone Game IV
#
# https://leetcode.com/problems/stone-game-iv/description/
#
# algorithms
# Hard (48.73%)
# Total Accepted:    5.3K
# Total Submissions: 10.7K
# Testcase Example:  '1\r'
#
# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there are n stones in a pile.  On each player's turn, that player
# makes a move consisting of removing any non-zero square number of stones in
# the pile.
#
# Also, if a player cannot make a move, he/she loses the game.
#
# Given a positive integer n. Return True if and only if Alice wins the game
# otherwise return False, assuming both players play optimally.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: true
# Explanation: Alice can remove 1 stone winning the game because Bob doesn't
# have any moves.
#
# Example 2:
#
#
# Input: n = 2
# Output: false
# Explanation: Alice can only remove 1 stone, after that Bob removes the last
# one winning the game (2 -> 1 -> 0).
#
# Example 3:
#
#
# Input: n = 4
# Output: true
# Explanation: n is already a perfect square, Alice can win with one move,
# removing 4 stones (4 -> 0).
#
#
# Example 4:
#
#
# Input: n = 7
# Output: false
# Explanation: Alice can't win the game if Bob plays optimally.
# If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should
# remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 ->
# 0).
# If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only
# can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 ->
# 0).
#
# Example 5:
#
#
# Input: n = 17
# Output: false
# Explanation: Alice can't win the game if Bob plays optimally.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
#
#
#


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # DP method. 
        # dp = [False] * (n + 1)
        # for i in range(1, n + 1):
        #     dp[i] = any(not dp[i - k * k] for k in range(1, int(i**0.5) + 1))
        # return dp[n]


        # Recursive method.
        @lru_cache(None)
        def rec(n):
            if n < 2: return n == 1
            return any(not rec(n-i*i) for i in range(int(n**0.5), 0, -1))
        return rec(n)

sol = Solution()
print(sol.winnerSquareGame(3))
for n in range(1, 18):
    print(n, sol.winnerSquareGame(n))

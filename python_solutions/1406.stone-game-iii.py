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
# @lc app=leetcode id=1406 lang=python3
#
# [1406] Stone Game III
#
# https://leetcode.com/problems/stone-game-iii/description/
#
# algorithms
# Hard (52.01%)
# Total Accepted:    3.9K
# Total Submissions: 7.3K
# Testcase Example:  '[1,2,3,7]'
#
# Alice and Bob continue their games with piles of stones. There are several
# stones arranged in a row, and each stone has an associated value which is an
# integer given in the array stoneValue.
#
# Alice and Bob take turns, with Alice starting first. On each player's turn,
# that player can take 1, 2 or 3 stones from the first remaining stones in the
# row.
#
# The score of each player is the sum of values of the stones taken. The score
# of each player is 0 initially.
#
# The objective of the game is to end with the highest score, and the winner is
# the player with the highest score and there could be a tie. The game
# continues until all the stones have been taken.
#
# Assume Alice and Bob play optimally.
#
# Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end
# the game with the same score.
#
#
# Example 1:
#
#
# Input: values = [1,2,3,7]
# Output: "Bob"
# Explanation: Alice will always lose. Her best move will be to take three
# piles and the score become 6. Now the score of Bob is 7 and Bob wins.
#
#
# Example 2:
#
#
# Input: values = [1,2,3,-9]
# Output: "Alice"
# Explanation: Alice must choose all the three piles at the first move to win
# and leave Bob with negative score.
# If Alice chooses one pile her score will be 1 and the next move Bob's score
# becomes 5. The next move Alice will take the pile with value = -9 and lose.
# If Alice chooses two piles her score will be 3 and the next move Bob's score
# becomes 3. The next move Alice will take the pile with value = -9 and also
# lose.
# Remember that both play optimally so here Alice will choose the scenario that
# makes her win.
#
#
# Example 3:
#
#
# Input: values = [1,2,3,6]
# Output: "Tie"
# Explanation: Alice cannot win this game. She can end the game in a draw if
# she decided to choose all the first three piles, otherwise she will lose.
#
#
# Example 4:
#
#
# Input: values = [1,2,3,-1,-2,-3,7]
# Output: "Alice"
#
#
# Example 5:
#
#
# Input: values = [-1,-2,-3]
# Output: "Tie"
#
#
#
# Constraints:
#
#
# 1 <= values.length <= 50000
# -1000 <= values[i] <= 1000
#
#


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        s = 0
        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            s += stoneValue[i]
            dp[i] = s - min(dp[i + 1:i + 4])
        
        if dp[0] * 2 == s:
            return "Tie"
        return "Alice" if dp[0] * 2 > s else "Bob"

sol = Solution()
# values = [1, 2, 3, -9]
# values = [-1,-2,-3]
# print(sol.stoneGameIII(values))

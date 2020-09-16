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
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (35.85%)
# Total Accepted:    462.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example 1:
#
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cc = [0] + [amount + 1] * amount
        for c in coins:
            for j in range(c, amount + 1):
                cc[j] = min(cc[j], 1 + cc[j - c])
        return -1 if cc[amount] == amount + 1 else cc[amount]


sol = Solution()

coins, amount = [1, 2, 5], 11
# coins, amount = [2], 3
print(sol.coinChange(coins, amount))

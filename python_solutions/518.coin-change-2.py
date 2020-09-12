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
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
# https://leetcode.com/problems/coin-change-2/description/
#
# algorithms
# Medium (50.43%)
# Total Accepted:    146.3K
# Total Submissions: 289.8K
# Testcase Example:  '5\n[1,2,5]'
#
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that
# amount. You may assume that you have infinite number of each kind of
# coin.
#
#
#
#
#
#
# Example 1:
#
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
# Example 2:
#
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
#
# Example 3:
#
#
# Input: amount = 10, coins = [10]
# Output: 1
#
#
#
#
# Note:
#
# You can assume that
#
#
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
#
#
#
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        f = [1] + [0] * amount
        n = len(coins)
        for i in range(n):
            for j in range(coins[i], amount + 1):
                f[j] += f[j - coins[i]] if j >= coins[i] else 0
        return f[-1]


sol = Solution()

amount, coins = 5, [1, 2, 5]
# amount, coins = 3, [2]
# amount, coins = 10, [10]
print(sol.change(amount, coins))

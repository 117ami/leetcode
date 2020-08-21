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
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (46.42%)
# Total Accepted:    143.3K
# Total Submissions: 307.6K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
#
#
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
#
#
# Example:
#
#
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#
#

# Explanation https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        s0 = [0] * n
        s1 = [0] * n
        s2 = [0] * n
        s1[0] = -prices[0]
        s2[0] = float('-inf')
        for i in range(1, n):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]
        return max(s0[-1], s2[-1])


sol = Solution()


inputs = [1, 2, 3, 0, 2]
print(sol.maxProfit(inputs))

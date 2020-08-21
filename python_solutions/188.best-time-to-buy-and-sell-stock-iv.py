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
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (27.74%)
# Total Accepted:    124.3K
# Total Submissions: 447.8K
# Testcase Example:  '2\n[2,4,1]'
#
# Say you have an array for which the i-th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k
# transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
#
# Example 1:
#
#
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
#
#
# Example 2:
#
#
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4.
# Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 =
# 3.
#
#
#


class Solution:
    def maxProfit(self, k: int, ps: List[int]) -> int:
        n = len(ps)
        if k >= n // 2:
            return self._qucick_solve(ps)

        '''dp[i][j] the maximum prefit gained at time j with at most
        i transcations
        '''
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            _max = -ps[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], ps[j] + _max)
                _max = max(_max, dp[i - 1][j - 1] - ps[j])

        return dp[-1][-1]

    def _qucick_solve(self, ps):
        '''As long as there is price gap, we gain a profit
        '''
        return sum(ps[i] - ps[i - 1]
                   for i in range(1, len(ps)) if ps[i] > ps[i - 1])


sol = Solution()
ps, k = [3, 2, 6, 5, 0, 3], 2
print(sol.maxProfit(k, ps))

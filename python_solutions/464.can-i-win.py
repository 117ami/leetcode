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
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (28.83%)
# Total Accepted:    52.4K
# Total Submissions: 181.6K
# Testcase Example:  '10\n11'
#
# In the "100 game" two players take turns adding, to a running total, any
# integer from 1 to 10. The player who first causes the running total to reach
# or exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of
# numbers from 1 to 15 without replacement until they reach a total >= 100.
#
# Given two integers maxChoosableInteger and desiredTotal, return true if the
# first player to move can force a win, otherwise return false. Assume both
# players play optimally.
#
#
# Example 1:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 11
# Output: false
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
#
#
# Example 2:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 0
# Output: true
#
#
# Example 3:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 1
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= maxChoosableInteger <= 20
# 0 <= desiredTotal <= 300
#
#
#
class Solution:
    def canIWin(self, m: int, t: int) -> bool:
        @lru_cache(None)
        def dfs(used: int, val: int) -> bool:
            for i in range(m, 0, -1):
                if (1 << i) & used == 0:
                    if val + i >= t:
                        return True
                    elif not dfs(used | (1 << i), val + i):
                        return True
            return False

        total = (1 + m) * m // 2

        if total <= t:
            return total == t and m & 0x1

        return dfs(1, 0)


sol = Solution()

m, t = 10, 11
m, t = 4, 6
print(sol.canIWin(m, t))

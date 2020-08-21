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
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#
# https://leetcode.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (27.07%)
# Total Accepted:    20.2K
# Total Submissions: 74.8K
# Testcase Example:  '1\n2'
#
# You are given K eggs, and you have access to a building with N floors from 1
# to N.
#
# Each egg is identical in function, and if an egg breaks, you cannot drop it
# again.
#
# You know that there exists a floor F with 0 <= F <= N such that any egg
# dropped at a floor higher than F will break, and any egg dropped at or below
# floor F will not break.
#
# Each move, you may take an egg (if you have an unbroken one) and drop it from
# any floor X (with 1 <= X <= N).
#
# Your goal is to know with certainty what the value of F is.
#
# What is the minimum number of moves that you need to know with certainty what
# F is, regardless of the initial value of F?
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: K = 1, N = 2
# Output: 2
# Explanation:
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty
# that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with
# certainty.
#
#
#
# Example 2:
#
#
# Input: K = 2, N = 6
# Output: 3
#
#
#
# Example 3:
#
#
# Input: K = 3, N = 14
# Output: 4
#
#
#
#
# Note:
#
#
# 1 <= K <= 100
# 1 <= N <= 10000
#
#
#
#
#
#
class Solution:
    def superEggDrop(self, egg: int, floor: int) -> int:
        # dp = [[0] * (egg + 1) for _ in range(floor + 1)]
        # for m in range(1, floor + 1):
        #     for i in range(1, egg + 1):
        #         dp[m][i] = dp[m - 1][i - 1] + dp[m - 1][i] + 1
        #     if dp[m][egg] >= floor: return m
        dp = [0] * (egg + 1)
        cnt = 0
        while dp[-1] < floor:
            cnt += 1
            pre = dp.copy()
            for i in range(1, egg + 1):
                dp[i] = pre[i - 1] + pre[i] + 1
            print(dp)
        return cnt


sol = Solution()
egg, floor = 1, 2
print(sol.superEggDrop(egg, floor))

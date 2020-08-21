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
# @lc app=leetcode id=1473 lang=python3
#
# [1473] Paint House III
#
# https://leetcode.com/problems/paint-house-iii/description/
#
# algorithms
# Hard (48.10%)
# Total Accepted:    6.3K
# Total Submissions: 13.2K
# Testcase Example:  '[0,0,0,0,0]\n[[1,10],[10,1],[10,1],[1,10],[5,1]]\n5\n2\n3'
#
# There is a row of m houses in a small city, each house must be painted with
# one of the n colors (labeled from 1 to n), some houses that has been painted
# last summer should not be painted again.
#
# A neighborhood is a maximal group of continuous houses that are painted with
# the same color. (For example: houses = [1,2,2,3,3,2,1,1] contains 5
# neighborhoods  [{1}, {2,2}, {3,3}, {2}, {1,1}]).
#
# Given an array houses, an m * n matrix cost and an integer target
# where:
#
#
# houses[i]: is the color of the house i, 0 if the house is not painted
# yet.
# cost[i][j]: is the cost of paint the house i with the color j+1.
#
#
# Return the minimum cost of painting all the remaining houses in such a way
# that there are exactly target neighborhoods, if not possible return -1.
#
#
# Example 1:
#
#
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =
# 5, n = 2, target = 3
# Output: 9
# Explanation: Paint houses of this way [1,2,2,1,1]
# This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
# Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
#
#
# Example 2:
#
#
# Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =
# 5, n = 2, target = 3
# Output: 11
# Explanation: Some houses are already painted, Paint the houses of this way
# [2,2,1,2,2]
# This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
# Cost of paint the first and last house (10 + 1) = 11.
#
#
# Example 3:
#
#
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m =
# 5, n = 2, target = 5
# Output: 5
#
#
# Example 4:
#
#
# Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n
# = 3, target = 3
# Output: -1
# Explanation: Houses are already painted with a total of 4 neighborhoods
# [{3},{1},{2},{3}] different of target = 3.
#
#
#
# Constraints:
#
#
# m == houses.length == cost.length
# n == cost[i].length
# 1 <= m <= 100
# 1 <= n <= 20
# 1 <= target <= m
# 0 <= houses[i] <= n
# 1 <= cost[i][j] <= 10^4
#
#
#
class Solution:
    def minCost(self,
                houses: List[int],
                cost: List[List[int]],
                m: int,
                n: int,
                target: int) -> int:
        # maps (i, t, p) -> the minimum cost to paint houses i <= h < m with t
        # neighborhoods, where house i - 1 is color p
        dp = {}

        # You can use this functools line instead of dp to make it faster, but I cache
        # manually because I don't want to abstract the caching away from the reader.
        # @functools.lru_cache(None)
        def dfs(i, t, p):
            key = (i, t, p)
            """When i == len(houses), there are three cases to consider:
            1. t > 0, we've colored the m houses with fewer than target neighborhoods, mission failed.
            2. t < 0, the opposite of - we've colored the houses with too many neighborhoods, mission failed
            3. t == 0, we succeeded in coloring the houses with the appropriate number of neighborhoods.
            """
            if i == len(houses):
                return 0 if t == 0 else math.inf
                # base case - we're trying to color 0 houses. Only i == len(houses) is necessary
                # to check here, but it prunes a bit of the search space to make things faster.
                # return 0 if t == 0 and i == len(houses) else float('inf')
            if t < 0 or m - i < t:
                return math.inf

            if key not in dp:
                if houses[i] == 0:
                    dp[key] = min(dfs(i + 1, t - (nc != p), nc) +
                                  cost[i][nc - 1] for nc in range(1, n + 1))
                else:
                    dp[key] = dfs(i + 1, t - (houses[i] != p), houses[i])

            return dp[key]

        ret = dfs(0, target, -1)
        # if ret is infinity, then we failed every case because there were too many neighborhoods
        # to start. If we could paint over houses that were previously painted, we could remedy that,
        # but the problem doesn't allow that.
        return ret if ret < math.inf else -1


sol = Solution()

houses, cost, m, n, target = [0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1],
                                               [1, 10], [5, 1]], 5, 2, 3

# houses = [0, 2, 1, 2, 0]
# cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
# m = 5
# n = 2
# target = 3

# houses = [0, 0, 0, 0, 0]
# cost = [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]]
# m = 5
# n = 2
# target = 5

# houses = [3, 1, 2, 3]
# cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
# m = 4
# n = 3
# target = 3
print(sol.minCost(houses, cost, m, n, target))

print(math.inf == float('inf'))

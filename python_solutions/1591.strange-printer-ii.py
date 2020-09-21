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
# @lc app=leetcode id=1591 lang=python3
#
# [1591] Strange Printer II
#
# https://leetcode.com/problems/strange-printer-ii/description/
#
# algorithms
# Hard (47.98%)
# Total Accepted:    1.3K
# Total Submissions: 2.5K
# Testcase Example:  '[[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]'
#
# There is a strange printer with the following two special requirements:
#
#
# On each turn, the printer will print a solid rectangular pattern of a single
# color on the grid. This will cover up the existing colors in the
# rectangle.
# Once the printer has used a color for the above operation, the same color
# cannot be used again.
#
#
# You are given a m x n matrix targetGrid, where targetGrid[row][col] is the
# color in the position (row, col) of the grid.
#
# Return true if it is possible to print the matrix targetGrid, otherwise,
# return false.
#
#
# Example 1:
#
#
#
#
# Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
# Output: true
#
#
# Example 2:
#
#
#
#
# Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
# Output: true
#
#
# Example 3:
#
#
# Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
# Output: false
# Explanation: It is impossible to form targetGrid because it is not allowed to
# print the same color in different turns.
#
# Example 4:
#
#
# Input: targetGrid = [[1,1,1],[3,1,3]]
# Output: false
#
#
#
# Constraints:
#
#
# m == targetGrid.length
# n == targetGrid[i].length
# 1 <= m, n <= 60
# 1 <= targetGrid[row][col] <= 60
#
#
#
class Solution:
    def isPrintable(self, g: List[List[int]]) -> bool:
        m, n = len(g), len(g[0])
        memo = [0] * 61

        def dfs(color):
            if memo[color] == -1: return False
            if memo[color] == 1: return True
            l = u = 0x3f3f3f3f
            r = d = -1
            for i in range(m):
                for j in range(n):
                    if g[i][j] == color:
                        l, r, u, d = min(l, i), max(r, i), min(u, j), max(d, j)

            if l == 0x3f3f3f3f: return True
            memo[color] = -1

            for i in range(l, r + 1):
                for j in range(u, d + 1):
                    if g[i][j] != color and not dfs(g[i][j]):
                        return False
            memo[color] = 1
            return True

        for i in range(61):
            if not dfs(i): return False
        return True


sol = Solution()
targetGrid = [[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]
targetGrid = [[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]]
# targetGrid = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
# targetGrid = [[1, 1, 1], [3, 1, 3]]
# print(sol.isPrintable(targetGrid))
# print(list(set(itertools.chain(*targetGrid))))

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
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#
# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/
#
# algorithms
# Medium (41.62%)
# Total Accepted:    6.1K
# Total Submissions: 14.6K
# Testcase Example:  '[[0,0,1],[1,1,0],[1,0,0]]'
#
# Given an n x n binary grid, in one step you can choose two adjacent rows of
# the grid and swap them.
#
# A grid is said to be valid if all the cells above the main diagonal are
# zeros.
#
# Return the minimum number of steps needed to make the grid valid, or -1 if
# the grid cannot be valid.
#
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and
# ends at cell (n, n).
#
#
# Example 1:
#
#
# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
#
#
# Example 2:
#
#
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
#
#
# Example 3:
#
#
# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0
#
#
#
# Constraints:
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 200
# grid[i][j] is 0 or 1
#
#
#


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = [n - 1 - next(filter(lambda j: grid[i][j],
                               range(n - 1, -1, -1)), -1) for i in range(n)]
        res = 0
        for i in range(n):
            required = n - i - 1
            k = next(filter(lambda j: row[j] >= required, range(i, n)), n)
            if k == n:
                return -1
            res += k - i
            row[i + 1:k + 1] = row[i:k]
        return res


sol = Solution()


grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
# grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# grid = [[1,0,0],[1,1,0],[1,1,1]]
print(sol.minSwaps(grid))
row = [0, 0, 0, 1, 0, 0]
s = ''.join(str(i) for i in row)
print(s.rindex('1'))

from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1368 lang=python3
#
# [1368] Minimum Cost to Make at Least One Valid Path in a Grid
#
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/
#
# algorithms
# Hard (51.59%)
# Total Accepted:    4.2K
# Total Submissions: 8.2K
# Testcase Example:  '[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]'
#
# Given a m x n grid. Each cell of the grid has a sign pointing to the next
# cell you should visit if you are currently in this cell. The sign of
# grid[i][j] can be:
#
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to
# grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to
# grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i +
# 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i -
# 1][j])
#
#
# Notice that there could be some invalid signs on the cells of the grid which
# points outside the grid.
#
# You will initially start at the upper left cell (0,0). A valid path in the
# grid is a path which starts from the upper left cell (0,0) and ends at the
# bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid
# path doesn't have to be the shortest.
#
# You can modify the sign on a cell with cost = 1. You can modify the sign on a
# cell one time only.
#
# Return the minimum cost to make the grid have at least one valid path.
#
#
# Example 1:
#
#
# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3)
# change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) -->
# (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2,
# 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.
#
#
# Example 2:
#
#
# Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
# Output: 0
# Explanation: You can follow the path from (0, 0) to (2, 2).
#
#
# Example 3:
#
#
# Input: grid = [[1,2],[4,3]]
# Output: 1
#
#
# Example 4:
#
#
# Input: grid = [[2,2,2],[2,2,2]]
# Output: 3
#
#
# Example 5:
#
#
# Input: grid = [[4]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
#
#
#


class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[false] * n for _ in range(m)]
        queue = deque([(m - 1, n - 1, 0)])
        dirs = [-1, 0, 1, 0, -1]
        signs = [3, 2, 4, 1]

        while queue:
            i, j, cur = queue.popleft()

            if visited[i][j]:
                continue
            visited[i][j] = true

            if i == j == 0:
                return cur

            for _i in [0, 3, 1, 2]:
                ni, nj = i + dirs[_i], j + dirs[_i + 1]
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                # print(ni, nj, _i)
                if grid[ni][nj] == signs[_i]:
                    queue.appendleft((ni, nj, cur))
                else:
                    queue.append((ni, nj, cur + 1))

            
        return -1


sol = Solution()
grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
# grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
# grid = [[1, 2], [4, 3]]
# grid = [[2, 2, 2], [2, 2, 2]]
# grid = [[4]]
# grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
print(sol.minCost(grid))

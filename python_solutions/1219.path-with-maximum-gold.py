#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#
# https://leetcode.com/problems/path-with-maximum-gold/description/
#
# algorithms
# Medium (61.31%)
# Total Accepted:    9K
# Total Submissions: 14.6K
# Testcase Example:  '[[0,6,0],[5,8,7],[0,9,0]]'
#
# In a gold mine grid of size m * n, each cell in this mine has an integer
# representing the amount of gold in that cell, 0 if it is empty.
#
# Return the maximum amount of gold you can collect under the conditions:
#
#
# Every time you are located in a cell you will collect all the gold in that
# cell.
# From your position you can walk one step to the left, right, up or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has
# some gold.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
# ⁠[5,8,7],
# ⁠[0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
#
#
# Example 2:
#
#
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
# ⁠[2,0,6],
# ⁠[3,4,5],
# ⁠[0,3,0],
# ⁠[9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
#
#
#
# Constraints:
#
#
# 1 <= grid.length, grid[i].length <= 15
# 0 <= grid[i][j] <= 100
# There are at most 25 cells containing gold.
#
#


class Solution:
    def getMaximumGold(self, grid):
        res = 0
        max_path = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in max_path and grid[i][j] > 0:
                    val, path = self.dfs(grid, i, j)
                    if val > res:
                        res = val
                        max_path = path
        return res

    def dfs(self, grid, i, j):
        gold, path = 0, set()
        if i < 0 or j < 0 or i >= len(grid) or j >= len(
                grid[0]) or grid[i][j] == 0:
            return gold, path

        v = grid[i][j]
        grid[i][j] = 0
        for ia, ib in ([i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]):
            n_gold, n_path = self.dfs(grid, ia, ib)
            if n_gold > gold:
                gold = n_gold
                path = n_path

        grid[i][j] = v
        return v + gold, path | {(i, j)}


s = Solution()
grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
# grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]

print(s.getMaximumGold(grid))

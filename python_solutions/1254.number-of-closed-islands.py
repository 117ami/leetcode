#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#
# https://leetcode.com/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (59.94%)
# Total Accepted:    5K
# Total Submissions: 8.3K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
# 4-directionally connected group of 0s and a closed island is an island
# totally (all left, top, right, bottom) surrounded by 1s.
#
# Return the number of closed islands.
#
#
# Example 1:
#
#
#
#
# Input: grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation:
# Islands in gray are closed because they are completely surrounded by water
# (group of 1s).
#
# Example 2:
#
#
#
#
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
#
#
# Example 3:
#
#
# Input: grid = [[1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# ⁠              [1,1,1,1,1,1,1]]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
#
#


class Solution:
    def closedIsland(self, grid):
        for i in range(len(grid)):
            self.infect(grid, i, 0)
            self.infect(grid, i, len(grid[0]) - 1)

        for j in range(len(grid[0])):
            self.infect(grid, 0, j)
            self.infect(grid, len(grid) - 1, j)

        res = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    res += 1
                    self.infect(grid, i, j)
        return res

    def infect(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(
                grid[0]) or grid[i][j] == 1:
            return
        grid[i][j] = 1
        self.infect(grid, i + 1, j)
        self.infect(grid, i, j + 1)
        self.infect(grid, i - 1, j)
        self.infect(grid, i, j - 1)


s = Solution()
grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
    1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]
grid = [
    [
        0, 0, 1, 1, 0, 1, 0, 0, 1, 0], [
            1, 1, 0, 1, 1, 0, 1, 1, 1, 0], [
                1, 0, 1, 1, 1, 0, 0, 1, 1, 0], [
                    0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [
                        0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [
                            0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [
                                1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [
                                    1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [
                                        1, 1, 1, 0, 0, 1, 0, 1, 0, 1], [
                                            1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
print(s.closedIsland(grid))

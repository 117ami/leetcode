from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
true = True
false = False
#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#
# https://leetcode.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (57.26%)
# Total Accepted:    14.6K
# Total Submissions: 25.5K
# Testcase Example:  '[[2]]'
#
# On a N * N grid, we place some 1 * 1 * 1 cubes.
#
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid
# cell (i, j).
#
# Return the total surface area of the resulting shapes.
#
#
#
#
#
#
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
# Input: [[2]]
# Output: 10
#
#
#
# Example 2:
#
#
# Input: [[1,2],[3,4]]
# Output: 34
#
#
#
# Example 3:
#
#
# Input: [[1,0],[0,2]]
# Output: 16
#
#
#
# Example 4:
#
#
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
#
#
#
# Example 5:
#
#
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
#
#
#
#
# Note:
#
#
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
#
#
#
#
#
#
#
#


class Solution:
    def surfaceArea(self, grid):
        l = len(grid)
        area = 0
        for i in range(l):
            for j in range(l - 1):
                area += 4 * grid[i][j] + 2 if grid[i][j] > 0 else 0
                area -= min(grid[i][j], grid[i][j + 1]) * 2
                area -= min(grid[j][i], grid[j + 1][i]) * 2
            area += 4 * grid[i][l - 1] + 2 if grid[i][l-1] > 0 else 0
        # for j in range(l):
        #     for i in range(l-1):
        #         area -= min(grid[i][j], grid[i+1][j])*2
        return area


s = Solution()
grid = [[2]]
# grid =[[1,2],[3,4]]
# grid =[[1,1,1],[1,0,1],[1,1,1]]
grid = [[1,0], [0,2]]
print(s.surfaceArea(grid))

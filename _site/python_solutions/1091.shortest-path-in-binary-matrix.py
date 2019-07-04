#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (32.11%)
# Total Accepted:    2.4K
# Total Submissions: 7.2K
# Testcase Example:  '[[0,1],[1,0]]'
#
# In an N by N square grid, each cell is either empty (0) or blocked (1).
#
# A clear path from top-left to bottom-right has length k if and only if it is
# composed of cells C_1, C_2, ..., C_k such that:
#
#
# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are
# different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] ==
# 0).
#
#
# Return the length of the shortest such clear path from top-left to
# bottom-right.  If such a path does not exist, return -1.
#
#
#
# Example 1:
#
#
# Input: [[0,1],[1,0]]
# Output: 2
#
#
#
# Example 2:
#
#
# Input: [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
#
#
#
#
# Note:
#
#
# 1 <= grid.length == grid[0].length <= 100
# grid[r][c] is 0 or 1
#
#
#
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, g):
        m = len(g)
        if g[0][0] == 1 or g[m - 1][m - 1] == 1:
            return -1
        if m == 1:
            return 1
        q = deque([[0, 0]])
        g[0][0] = 1
     
        while q:
            i, j = q.popleft()
            # print(i, j)
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if a != 0 or b != 0:
                        x, y = i + a, j + b
                        if x < 0 or x >= m or y < 0 or y >= m or g[x][y] != 0:
                            continue
                        g[x][y] = g[i][j] + 1
                        q.append([x, y])

                        if x == m - 1 and y == m - 1:
                            return g[x][y]
        return -1


s = Solution()
g = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(s.shortestPathBinaryMatrix(g))

from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=1139 lang=python3
#
# [1139] Largest 1-Bordered Square
#
# https://leetcode.com/problems/largest-1-bordered-square/description/
#
# algorithms
# Medium (45.49%)
# Total Accepted:    6.3K
# Total Submissions: 13.8K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D grid of 0s and 1s, return the number of elements in the largest
# square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't
# exist in the grid.
#
#
# Example 1:
#
#
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 9
#
#
# Example 2:
#
#
# Input: grid = [[1,1,0,0]]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] is 0 or 1
#
#


class Solution:
    def largest1BorderedSquare(self, gd):
        m, n, maxlen = len(gd), len(gd[0]), 0
        ver = [[0]*n for _ in range(m)]
        hor = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if gd[i][j] == 1:
                    ver[i][j] = 1 if j == 0 else ver[i][j-1] + 1 
                    hor[i][j] = 1 if i == 0 else hor[i-1][j] + 1
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                minv = min(ver[i][j], hor[i][j])
                while minv > maxlen:
                    if ver[i-minv+1][j] >= minv and hor[i][j-minv+1] >= minv:
                        maxlen = minv 
                        break 
                    minv -= 1
        return maxlen * maxlen 





sol = Solution()
gd = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# gd = [[1,1,0,0]]
gd = [[0, 1], [1, 1]]
print(sol.largest1BorderedSquare(gd))

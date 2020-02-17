from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
#
# algorithms
# Easy (83.52%)
# Total Accepted:    7.2K
# Total Submissions: 8.7K
# Testcase Example:  '[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]'
#
# Given a m * n matrix grid which is sorted in non-increasing order both
# row-wise and column-wise. 
# 
# Return the number of negative numbers in grid.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[3,2],[1,0]]
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# 
# 
# Example 4:
# 
# 
# Input: grid = [[-1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
# 
#
class Solution:
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        res = 0
        for row in grid:
            for i, v in enumerate(row):
                if v < 0:
                    res += n - i
                    break 

        return res 
        

sol = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(sol.countNegatives(grid))


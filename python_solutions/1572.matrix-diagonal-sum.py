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
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#
# https://leetcode.com/problems/matrix-diagonal-sum/description/
#
# algorithms
# Easy (77.53%)
# Total Accepted:    6.4K
# Total Submissions: 8.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the
# elements on the secondary diagonal that are not part of the primary
# diagonal.
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],
# [4,5,6],
# [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
#
#
# Example 2:
#
#
# Input: mat = [[1,1,1,1],
# [1,1,1,1],
# [1,1,1,1],
# [1,1,1,1]]
# Output: 8
#
#
# Example 3:
#
#
# Input: mat = [[5]]
# Output: 5
#
#
#
# Constraints:
#
#
# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100
#
#
#
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res, n = 0, len(mat)
        for i in range(n):
            res += mat[i][i] + mat[i][n - 1 - i]
        if n & 1: res -= mat[(n - 1) // 2][(n - 1) // 2]
        return res


sol = Solution()

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sol.diagonalSum(mat))

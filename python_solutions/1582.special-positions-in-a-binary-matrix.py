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
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/
#
# algorithms
# Easy (59.56%)
# Total Accepted:    5.9K
# Total Submissions: 9.9K
# Testcase Example:  '[[1,0,0],[0,0,1],[1,0,0]]'
#
# Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the
# number of special positions in mat.
# 
# A position (i,j) is called special if mat[i][j] == 1 and all other elements
# in row i and column j are 0 (rows and columns are 0-indexed).
# 
# 
# Example 1:
# 
# 
# Input: mat = [[1,0,0],
# [0,0,1],
# [1,0,0]]
# Output: 1
# Explanation: (1,2) is a special position because mat[1][2] == 1 and all other
# elements in row 1 and column 2 are 0.
# 
# 
# Example 2:
# 
# 
# Input: mat = [[1,0,0],
# [0,1,0],
# [0,0,1]]
# Output: 3
# Explanation: (0,0), (1,1) and (2,2) are special positions. 
# 
# 
# Example 3:
# 
# 
# Input: mat = [[0,0,0,1],
# [1,0,0,0],
# [0,1,1,0],
# [0,0,0,0]]
# Output: 2
# 
# 
# Example 4:
# 
# 
# Input: mat = [[0,0,0,0,0],
# [1,0,0,0,0],
# [0,1,0,0,0],
# [0,0,1,0,0],
# [0,0,0,1,1]]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] is 0 or 1.
# 
# 
#
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        pass 
        

sol = Solution()


mat = [[1,0,0],               [0,0,1],               [1,0,0]]
mat = [[1,0,0],               [0,1,0],               [0,0,1]]
mat = [[0,0,0,1],               [1,0,0,0],               [0,1,1,0],               [0,0,0,0]]
mat = [[0,0,0,0,0],               [1,0,0,0,0],               [0,1,0,0,0],               [0,0,1,0,0],               [0,0,0,1,1]]
print(sol.numSpecial(mat))

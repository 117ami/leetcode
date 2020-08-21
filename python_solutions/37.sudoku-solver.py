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
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (42.21%)
# Total Accepted:    178.2K
# Total Submissions: 421.4K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
#
#
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
#
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
#
#
#


class Solution:
    def __init__(self):
        self.row = [[0] * 10 for _ in range(9)]
        self.col = [[0] * 10 for _ in range(9)]
        self.cub = [[[0] * 10 for _ in range(3)] for _ in range(3)]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for r, c in itertools.product(range(9), range(9)):
            if board[r][c] != ".":
                n = int(board[r][c])
                self.row[r][n] = 1
                self.col[c][n] = 1
                self.cub[r // 3][c // 3][n] = 1
        self.dfs(board, 0, 0)

    def dfs(self, board, i, j)->bool:
        if i == 9:
            return True
        if j == 9:
            return self.dfs(board, i + 1, 0)
        if board[i][j] != '.':
            return self.dfs(board, i, j + 1)

        for x in range(1, 10):
            c = str(x)
            if self.feasible(i, j, x):
                board[i][j] = c
                self.row[i][x] = self.col[j][x] = self.cub[i // 3][j // 3][x] = 1
                if self.dfs(board, i, j + 1):
                    return True
                self.row[i][x] = self.col[j][x] = self.cub[i // 3][j // 3][x] = 0
                board[i][j] = '.'
        return False

    def feasible(self, i, j, x):
        if self.row[i][x] == 1:
            return False
        if self.col[j][x] == 1:
            return False
        if self.cub[i // 3][j // 3][x] == 1:
            return False
        return True


sol = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."], 
    ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
    [".", "9", "8", ".", ".", ".", ".", "6", "."], 
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
    [".", "6", ".", ".", ".", ".", "2", "8", "."], 
    [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(sol.solveSudoku(board))

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
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (26.44%)
# Total Accepted:    211K
# Total Submissions: 792.6K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
#
#


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [-1, 0, 1, 0, -1]
        if not board:
            return
        m, n = len(board), len(board[0])

        def dfs(i, j, sa, sb):
            '''replace symbol sa with symbol b'''
            if 0 <= i < m and 0 <= j < n and board[i][j] == sa:
                board[i][j] = sb
                for k in range(4):
                    dfs(i + dirs[k], j + dirs[k + 1], sa, sb)

        for i, j in itertools.product(range(m), [0, n - 1]):
            dfs(i, j, 'O', '#')
        for i, j in itertools.product([0, m - 1], range(n)):
            dfs(i, j, 'O', '#')

        board[:] = [['XO'[c == '#'] for c in row] for row in board]

        return board


sol = Solution()
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
# board = [['O', 'O', 'O']]
print(sol.solve(board))

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
# @lc app=leetcode id=794 lang=python3
#
# [794] Valid Tic-Tac-Toe State
#
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/
#
# algorithms
# Medium (32.62%)
# Total Accepted:    26.3K
# Total Submissions: 80.7K
# Testcase Example:  '["O  ","   ","   "]'
#
# A Tic-Tac-Toe board is given as a string array board. Return True if and only
# if it is possible to reach this board position during the course of a valid
# tic-tac-toe game.
#
# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".
# The " " character represents an empty square.
#
# Here are the rules of Tic-Tac-Toe:
#
#
# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always
# places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled
# ones.
# The game ends when there are 3 of the same (non-empty) character filling any
# row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
#
#
#
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
#
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
#
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
#
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
#
#
# Note:
#
#
# board is a length-3 array of strings, where each string board[i] has length
# 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.
#
#
#
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        cnt_a = sum(map(lambda b: b.count('X'), board))
        cnt_b = sum(map(lambda b: b.count('O'), board))
        if cnt_a < cnt_b or cnt_a - cnt_b > 1: return False
        win_a = any(board[i] == 'XXX' for i in range(3)) or all(
            board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)) or \
                any(all(board[j][i] == 'X' for j in range(3)) for i in range(3))

        win_b = any(board[i] == 'OOO' for i in range(3)) or all(
            board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)) or \
                any(all(board[j][i] == 'O' for j in range(3)) for i in range(3))

        if (win_a and win_b) or (win_a and cnt_a
                                 == cnt_b) or (win_b and cnt_a - 1 == cnt_b):
            return False
        return True


sol = Solution()
board = ["O  ", "   ", "   "]
board = ["XOX", " X ", "   "]
board = ["XXX", "   ", "OOO"]
board = ["XOX", "O O", "XOX"]
board = ["XO ", "XO ", "XO "]
print(sol.validTicTacToe(board))

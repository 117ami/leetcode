#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (41.58%)
# Total Accepted:    91.3K
# Total Submissions: 219.5K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
#
#
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
#
#
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
#
# Example:
#
#
# Input:
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output:
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
#
#
# Follow up:
#
#
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
#
#
#


class Solution(object):
    def count_neibors(self, board, i, j):
        res = 0
        for m in range(i - 1, i + 2):
            for n in range(j - 1, j + 2):
                if m == i and n == j:
                    continue
                if m >= 0 and m < len(board) and n >= 0 and n < len(board[0]):
                    a = str(board[m][n]).split('.')[0]
                    if int(a) == 1:
                        res += 1
        return res

    def gameOfLife(self, board):
        # print(self.count_neibors(board, 1, 0))
        for i in range(len(board)):
            for j in range(len(board[0])):
                cter = self.count_neibors(board, i, j)
                board[i][j] = '.'.join([str(board[i][j]), str(cter)])

        for i in range(len(board)):
            for j in range(len(board[0])):
                a, b = [int(k) for k in board[i][j].split('.')]
                if a == 0 and b == 3 or a == 1 and (b == 2 or b == 3):
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        # print(board)


board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
Solution().gameOfLife(board)

#
# @lc app=leetcode id=289 lang=ruby
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
# @param {Integer[][]} board
# @return {Void} Do not return anything, modify board in-place instead.

def game_of_life(board)
  lives = lambda do |i, j|
    res = 0
    [i - 1, i, i + 1].product([j - 1, j, j + 1]).each do |m, n|
      next if m < 0 || n < 0 || m >= board.size || n >= board[0].size || m == i && n == j

      res += 1 if board[m][n].to_s.split('.').first.to_i == 1
    end
    res
  end

  0.upto(board.size - 1).each do |i|
    0.upto(board[0].size - 1).each do |j|
      board[i][j] = [board[i][j], lives.call(i, j)].join('.')
    end
  end

    0.upto(board.size - 1).each do |i|
    0.upto(board[0].size - 1).each do |j|
    	a, b = board[i][j].split(".").map(&:to_i)
    	board[i][j] = (a == 0 && b == 3 || a == 1 && (b == 2 || b == 3)) ? 1 : 0	
    end
  end
end

board =
  [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
  ]

p game_of_life(board)

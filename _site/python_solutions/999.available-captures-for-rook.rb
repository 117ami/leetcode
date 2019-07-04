#
# @lc app=leetcode id=999 lang=ruby
#
# [999] Available Captures for Rook
#
# https://leetcode.com/problems/available-captures-for-rook/description/
#
# algorithms
# Easy (68.35%)
# Total Accepted:    8.4K
# Total Submissions: 12.3K
# Testcase Example:  '[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]'
#
# On an 8 x 8 chessboard, there is one white rook.  There also may be empty
# squares, white bishops, and black pawns.  These are given as characters 'R',
# '.', 'B', and 'p' respectively. Uppercase characters represent white pieces,
# and lowercase characters represent black pieces.
#
# The rook moves as in the rules of Chess: it chooses one of four cardinal
# directions (north, east, west, and south), then moves in that direction until
# it chooses to stop, reaches the edge of the board, or captures an opposite
# colored pawn by moving to the same square it occupies.  Also, rooks cannot
# move into the same square as other friendly bishops.
#
# Return the number of pawns the rook can capture in one move.
#
#
#
# Example 1:
#
#
#
#
# Input:
# [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation:
# In this example the rook is able to capture all the pawns.
#
#
# Example 2:
#
#
#
#
# Input:
# [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation:
# Bishops are blocking the rook to capture any pawn.
#
#
# Example 3:
#
#
#
#
# Input:
# [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation:
# The rook can capture the pawns at positions b5, d6 and f5.
#
#
#
#
# Note:
#
#
# board.length == board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'
#
#
#
# @param {Character[][]} board
# @return {Integer}
def num_rook_captures(board)
  ans = i = j = 0
  i += 1 until board[i].include?('R')
  j += 1 until board[i][j] == 'R'

  [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |m, n|
    x = i + m
    y = j + n
    while x < 8 && x >= 0 &&  y < 8 && y >= 0
      ans += 1 if board[x][y] == 'p'
      break if board[x][y] != '.'

      x += m
      y += n
    end
  end
  ans
end

board = [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['p', 'p', '.', 'R', '.', 'p', 'B', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'B', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]
board = [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['.', '.', '.', 'R', '.', '.', '.', 'p'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]
p num_rook_captures(board)

# An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.
#
# What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return -1.
#
# Examples:
# Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# Output: 2
# Explanation:
# One potential sequence of moves is shown below, from left to right:
#
# 0110     1010     1010
# 0110 --> 1010 --> 0101
# 1001     0101     1010
# 1001     0101     0101
#
# The first move swaps the first and second column.
# The second move swaps the second and third row.
#
# Input: board = [[0, 1], [1, 0]]
# Output: 0
# Explanation:
# Also note that the board with 0 in the top left corner,
# 01
# 10
#
# is also a valid chessboard.
#
# Input: board = [[1, 0], [1, 0]]
# Output: -1
# Explanation:
# No matter what sequence of moves you make, you cannot end with a valid chessboard.
# Note:
#
# board will have the same number of rows and columns, a number in the range [2, 30].
# board[i][j] will be only 0s or 1s.

# @param {Integer[][]} board
# @return {Integer}
def moves_to_chessboard(board)
  sz = board.size
  return -1 if invalid?(board) || invalid?(board.transpose)
  m1 = minimum_step(board[0].dup)
  m2 = minimum_step(board.transpose[0].dup)
  m1 + m2
end

def minimum_step(line)
  # return the ideal shape of a line, i.e., 0 1 0 1 0 or 1 0 1 0
  a, b = line.group_by { |v| v }.values.sort_by(&:size)
  ideals = if line.size.odd?
             [b.zip(a).flatten.compact]
           else
             [a.zip(b).flatten, b.zip(a).flatten]
           end

  min = 1 << 32
  ideals.each do |x|
    r = 0
    x.each_with_index { |v, i| r += 1 if v != line[i] }
    min = [min, r].min
  end
  min / 2
end

def invalid?(b)
  rows = Hash.new(0)
  b.each do |row|
    rows[row.join] += 1
    v0, v1 = row.group_by { |v| v }.values.map(&:size)
    return true if v1.nil? || (v0 - v1).abs > 1
  end
  # There are only two possible ways of rows and columns
  return true unless rows.size == 2
  false
end

board = [[1, 0, 1, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1]]
p moves_to_chessboard(board)

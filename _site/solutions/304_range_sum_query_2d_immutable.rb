# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 <= row2 and col1 <= col2.
#
#  https://leetcode.com/problems/range-sum-query-2d-immutable/description/
require './aux.rb'

class NumMatrix
  def initialize(matrix)
    @m = Array.new(matrix.size) { Array.new(matrix[0].size, 0) }
    return @m if matrix.empty?
    @m[0][0] = matrix[0][0]
    0.upto(matrix.size - 1).each do |i|
      0.upto(matrix[0].size - 1).each do |j|
        next if i.zero? && j.zero?
        @m[i][j] = @m[i][j - 1] + matrix[i][j]
      end
    end
  end

  def sum_region(row1, col1, row2, col2)
    res = 0
    row1.upto(row2).each do |i|
      b = @m[i][col2]
      a = col1.zero? ? 0 : @m[i][col1 - 1]
      res += b - a
    end
    res
  end
end

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

matrix = [[-1]]
# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix.new(matrix)
param_1 = obj.sum_region(0, 0, 0, 0)
p param_1

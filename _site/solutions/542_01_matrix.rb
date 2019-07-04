#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:
# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#  https://leetcode.com/problems/01-matrix/description/
require './aux.rb'

# @param {Integer[][]} matrix
# @return {Integer[][]}
def update_matrix(matrix)
  return matrix if matrix.empty?
  res = matrix.map { |row| row.map { |n| n * 10_000 } }
  4.times do
    0.upto(res.size - 1).each do |i|
      1.upto(res[0].size - 1).each do |j|
        res[i][j] = [res[i][j], res[i][j - 1] + 1].min
      end
    end
    res = res.transpose.map(&:reverse!)
  end
  res
end

matrix = [
  [0, 0, 1],
  [1, 1, 0],
  [1, 0, 1]
]
matrix = [[0, 1, 0, 1, 1],
          [1, 1, 0, 0, 1],
          [0, 0, 0, 1, 0],
          [1, 0, 1, 1, 1],
          [1, 0, 0, 0, 1]]
p update_matrix(matrix)

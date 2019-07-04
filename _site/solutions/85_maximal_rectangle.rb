# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
# Example:
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6
#
#  https://leetcode.com/problems/maximal-rectangle/description/
require './aux.rb'

# @param {Character[][]} matrix
# @return {Integer}
def maximal_rectangle(matrix)
  return 0 if matrix.empty?
  cache = Array.new(matrix.size) { Array.new(matrix.size, []) }
  res = 0
  (matrix.size - 1).downto(0).each do |i|
    (matrix[0].size - 1).downto(0).each do |j|
      if matrix[i][j] == '0'
        cache[i][j] = [0, 0]
      elsif i == matrix.size - 1
        cache[i][j] = j == matrix[0].size - 1 ? [1, 1] : [1 + cache[i][j + 1].first, 1]
        res = [res, cache[i][j].first].max
      elsif j == matrix[0].size - 1
        cache[i][j] = i == matrix.size - 1 ? [1, 1] : [1, 1 + cache[i + 1][j].last]
        res = [res, cache[i][j].last].max
      else
        cache[i][j] = [cache[i][j + 1].first + 1, cache[i + 1][j].last + 1]
        rowlen = cache[i][j].first
        i.upto(i + cache[i][j].last - 1).each do |ni|
          rowlen = [rowlen, cache[ni][j].first].min
          res = [(ni - i + 1) * rowlen, res].max
        end
      end
    end
  end
  res
end

matrix = [
  %w[1 0 1 0 0],
  %w[1 0 1 1 1],
  %w[1 1 1 1 1],
  %w[1 0 1 1 0]
]

p maximal_rectangle(matrix)

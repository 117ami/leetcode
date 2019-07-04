# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:
# Given the following 5x5 matrix:
#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
# Return:
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
#
#  https://leetcode.com/problems/pacific-atlantic-water-flow/description/
require './aux.rb'
# altantic[[i, j].join('-')]  = true
# infect.call(matrix[i][j], i-1, j)
# elsif
# altantic[[i, j].join('-')]  = true
# infect.call(matrix[i][j], i, j-1)
# elsif

# @param {Integer[][]} matrix
# @return {Integer[][]}
def pacific_atlantic(matrix)
	res = []
	return res if matrix.empty?
	altantic = {}
	pacific = {}

	infect = lambda do |v, i, j|
		return if altantic.key?([i, j].join('-')) || i < 0 || i > matrix.size - 1 || j < 0 || j > matrix[0].size - 1
		if i == matrix.size - 1 || j == matrix[0].size - 1 || v <= matrix[i][j]
			altantic[[i, j].join('-')] = true
			[[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]].each { |a, b| infect.call(matrix[i][j], a, b) }
		end
	end

	flow = lambda do |v, i, j|
		return if pacific.key?([i, j].join('-')) || i < 0 || i > matrix.size - 1 || j < 0 || j > matrix[0].size - 1
		if i.zero? || j.zero? || v <= matrix[i][j]
			pacific[[i, j].join('-')] = true
			res << [i, j] if altantic.key?([i, j].join('-'))
			[[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]].each { |a, b| flow.call(matrix[i][j], a, b) }
		end
	end

	infect.call(matrix.last.last, matrix.size - 1, matrix[0].size - 1)
	flow.call(matrix[0][0], 0, 0)
	res
end

matrix = [
	[1, 2, 2, 3, 5],
	[3, 2, 3, 4, 4],
	[2, 4, 5, 3, 1],
	[6, 7, 1, 4, 5],
	[5, 1, 1, 2, 4]
]

p pacific_atlantic(matrix)

#
# @lc app=leetcode id=73 lang=ruby
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (38.30%)
# Total Accepted:    176.9K
# Total Submissions: 461.9K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
#
# Example 1:
#
#
# Input:
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output:
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
#
#
# Example 2:
#
#
# Input:
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output:
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
#
#
# Follow up:
#
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
#
#
#
# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def set_zeroes(matrix)
  panish = lambda do |i, j|
    (0..matrix.size - 1).each { |ni| matrix[ni][j] = [matrix[ni][j].to_s.split('.').first, '0'].join('.') }
    (0..matrix[0].size - 1).each { |nj| matrix[i][nj] = [matrix[i][nj].to_s.split('.').first, '0'].join('.') }
  end

  (0..matrix.size - 1).each do |i|
    (0..matrix[0].size - 1).each do |j|
      panish.call(i, j) if matrix[i][j].to_s.split('.').first.to_i.zero?
    end
  end

  (0..matrix.size - 1).each do |i|
    (0..matrix[0].size - 1).each do |j|
      matrix[i][j] = 0 if matrix[i][j].to_s.split('.').last.to_i.zero?
    end
  end
  # matrix
end

matrix = [
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5]
]

p set_zeroes(matrix)

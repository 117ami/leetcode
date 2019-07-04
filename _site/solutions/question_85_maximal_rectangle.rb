=begin
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
=end

# @param {Character[][]} matrix
# @return {Integer}
require 'matrix'

def maximal_rectangle(matrix)
  Matrix.rows(matrix).each_with_index do |v, i, j|
    pp [v, i, j]
  end
  p "he"
  maxarea(matrix, 0, 2)
end

def maxarea(matrix, m, n)
  return 0 if matrix[m][n] == '0'
  imax = jmax = r = 1 << 32
  jmax = matrix[0].size - 1
  m.upto(matrix.size - 1) do |i|
    (n..jmax).each do |j|
      if matrix[i][j] == '0'
        imax = [i - 1, imax].min
        jmax = [j - 1, jmax].min
      end
    end
  end
  p [m, n, imax, jmax]
end

matrix = [
  %w[1 0 1 0 0],
  %w[1 0 1 1 1],
  %w[1 1 1 1 1],
  %w[1 0 0 1 0],
]

maximal_rectangle(matrix)

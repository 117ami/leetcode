# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#
# Input: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:
#
# Input: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
#

# @param {Integer[][]} matrix
# @return {Integer}
def longest_increasing_path(matrix)
  return 0 if matrix.empty?
  res = 1
  sz = matrix.size
  cn = matrix[0].size
  aux = array_array(sz, cn, 0)
  helper = lambda do |i, j|
    return aux[i][j] if aux[i][j] != 0
    aux[i][j] = 1
    [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]].each do |ni, nj|
      next if ni < 0 || ni >= sz || nj < 0 || nj >= cn || matrix[ni][nj] <= matrix[i][j]
      aux[i][j] = [aux[i][j], helper.call(ni, nj) + 1].max
    end
    res = aux[i][j] if res < aux[i][j]
    aux[i][j]
  end
  0.upto(sz - 1).each do |i|
    0.upto(cn - 1).each do |j|
      helper.call(i, j)
    end
  end
  # p aux
  res
end

def array_array(rn, cn, iv = 1)
  Array.new(rn) { Array.new(cn, iv) }
end

nums =
  [
    [7, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
  ]

p longest_increasing_path(nums)

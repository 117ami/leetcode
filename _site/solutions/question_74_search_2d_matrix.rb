# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
  return false if matrix.empty? || matrix[0].empty? ||
                  target < matrix[0][0] || target > matrix[-1][-1]
  i = matrix.transpose[0].bsearch_index { |v| v > target }
  i = i.nil? ? matrix.size - 1 : i - 1
  matrix[i].include?(target)
end

m = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

p search_matrix(m, 10)

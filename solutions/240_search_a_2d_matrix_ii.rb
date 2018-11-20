# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#   Integers in each row are sorted in ascending from left to right.
#   Integers in each column are sorted in ascending from top to bottom.
# Example:
# Consider the following matrix:
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Giventarget=5, returntrue.
# Giventarget=20, returnfalse.
#
#  https://leetcode.com/problems/search-a-2d-matrix-ii/description/

# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
  return false if matrix.empty? || matrix[0].empty?
  i = 0
  j = matrix[0].size - 1
  while i < matrix.size && j >= 0
    return true if matrix[i][j] == target
    if matrix[i][j] > target
      j -= 1
    else
      i += 1
      end
  end
  false
end

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target = 24

p search_matrix(matrix, target)

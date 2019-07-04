# Given an m * n matrix M initialized with all 0's and several update operations.
#
# Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
#
# You need to count and return the number of maximum integers in the matrix after performing all the operations.

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} ops
# @return {Integer}
def max_count(m, n, ops)
  return m * n if ops.empty? # no guarantee that ops will be non-empty
  ops.map(&:first).min * ops.map(&:last).min
end

ops = [[2, 3], [3, 2], [3, 4], [4, 1]]
p max_count(2, 2, ops)

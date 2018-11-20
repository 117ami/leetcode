
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

# @param {Integer[][]} matrix
# @return {Integer[]}
def spiral_order(matrix)
  matrix[0] ? matrix.shift + spiral_order(matrix.transpose.reverse) : []
end

m = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
p spiral_order(m)

sz = 2
bd = 15
init = [[16, 15]]
init = init.transpose
p init

init = [[13, 14], [16, 15]]
init = init.rotate
p init

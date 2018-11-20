
# @param {Integer[][]} matrix
# @return {Boolean}
def is_toeplitz_matrix(matrix)
  row = matrix.size
  return true if row == 1
  col = matrix[0].size
  return true if col == 1

  ct = 0
  matrix.reverse!
  while matrix
    matrix.shift while matrix[0].empty?
    return true if matrix.size == 1

    i = 0
    e = matrix[i][0]
    while i <= ct and i < col and i < matrix.size
      p matrix
      f = matrix[i].shift
      return false unless e == f
      i += 1
    end
    ct += 1
  end
  true 
end

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix = [[3,54],[42,3],[34,42],[34,34]]
p is_toeplitz_matrix(matrix)


# learning tap


# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# click to show follow up.
#
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def set_zeroes(matrix)
  m = matrix.size
  n = matrix[0].size
  a = 3.14159
  m.times do |i|
    rset = false
    n.times do |j|
      next unless matrix[i][j].to_i.zero?
      unless rset
        rset = true
        n.times { |k| matrix[i][k] = a unless matrix[i][k].zero? }
      end
      m.times { |k| matrix[k][j] = a unless matrix[k][j].zero? }
    end
  end

  0.upto(m - 1) do |i|
    0.upto(n - 1) do |j|
      matrix[i][j] = 0 if matrix[i][j] == a
    end
  end

  p matrix
end

m = [
  [1, 0, 0, 3],
  [2, 1, 3, 2],
  [2, 0, 5, 4],
  [7, 8, 2, 9]
]
set_zeroes(m)

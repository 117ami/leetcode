# We have a two dimensional matrixA where each value is 0 or 1.
# A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
# After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
# Return the highest possiblescore.
#
# Example 1:
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
# Note:
#   1 <= A.length <= 20
#   1 <= A[0].length <= 20
#   A[i][j]is 0 or 1.
#
#  https://leetcode.com/problems/score-after-flipping-matrix/description/

# @param {Integer[][]} a
# @return {Integer}
def matrix_score(a)
  res = 0
  zeros = Hash.new(0)
  ones =  Hash.new(0)
  0.upto(a.size - 1).each do |i|
    a[i] = revert(a[i]) if a[i].first.zero?
  end

  0.upto(a[0].size - 1).each do |j|
    m = n = 0
    0.upto(a.size - 1).each do |i|
      m += 1 if a[i][j] == 1
      n += 1 if a[i][j] == 0
    end
    res += 2**(a[0].size - 1 - j) * [m, n].max
  end
  res
end

def revert(row)
  row.map { |i| 1 - i }
end

a = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
p matrix_score(a)

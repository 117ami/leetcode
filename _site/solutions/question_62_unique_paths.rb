
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Above is a 3 x 7 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.

# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)
  return 0 if (m * n).zero?
  return 1 if m == 1 || n == 1

  r = Array.new(m) { Array.new(n, 0) }
  (0..n - 1).each { |i| r[m - 1][i] = 1 }
  (0..m - 1).each { |i| r[i][n - 1] = 1 }

  (0..m - 2).reverse_each do |i|
    (0..n - 2).reverse_each do |j|
      r[i][j] = r[i][j + 1] + r[i + 1][j]
    end
  end
  r[0][0]
end

# Another simplier way of doing it is: C_{m + n - 2} ^ {m - 1}
def unique_paths_2(m, n)
  f = lambda do |k| # factorial
    k = k.zero? ? 1 : (1..k).reduce(:*)
  end
  f.call(m + n - 2) / (f.call(m - 1) * f.call(n - 1))
end

p unique_paths(3, 2)
p unique_paths_2(3, 2)

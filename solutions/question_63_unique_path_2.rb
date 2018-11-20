
# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.

# @param {Integer[][]} obstacle_grid
# @return {Integer}
def unique_paths_with_obstacles(obstacle_grid)
  r = obstacle_grid
  m = r.size
  n = r[0].size || 0
  return 0 if m.zero? || r[m - 1][n - 1] == 1

  ri = r[m - 1].rindex(1)
  if ri.nil?
    r[m - 1] = Array.new(n, 1)
  else
    (0..n - 1).each { |j| r[m - 1][j] = j <= ri ? 0 : 1 }
  end

  (0..m - 2).reverse_each do |i|
    if r[i][n - 1] == 1
      (0..i).each { |j| r[j][n - 1] = 0 }
      break
    end
    r[i][n - 1] = 1
  end

  (0..m - 2).reverse_each do |i|
    (0..n - 2).reverse_each do |j|
      r[i][j] = if r[i][j] == 1
                  0
                else
                  r[i][j + 1] + r[i + 1][j]
                end
    end
  end
  r[0][0]
end

og = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
p unique_paths_with_obstacles(og)

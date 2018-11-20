# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

def dfs(grid, i, j)
  return 0 if i < 0 || i > grid.size - 1 || j < 0 || j > grid[0].size - 1
  return 0 if grid[i][j].zero?
  grid[i][j] = 0
  1 + dfs(grid, i - 1, j) + dfs(grid, i, j + 1) + dfs(grid, i + 1, j) + dfs(grid, i, j - 1)
end

def max_area_of_island(grid)
  ret = 0
  (0..grid.size - 1).each do |i|
    (0..grid[0].size - 1).each do |j|
      next if grid[i][j].zero?
      ret = [ret, dfs(grid, i, j)].max
    end
  end
  ret
end

# @param {Integer[][]} grid
# @return {Integer}
def max_area_of_island2(grid)
  ret = 0
  rowsize = grid.size - 1
  colsize = grid[0].size - 1
  (0..rowsize).each do |i|
    (0..colsize).each do |j|
      next if grid[i][j].zero?
      todo = [[i, j]]
      area = 0
      until todo.empty?
        a, b = todo.shift
        next if a < 0 || a > rowsize || b < 0 || b > colsize
        next if grid[a][b].zero?
        area += 1
        todo << [a - 1, b] << [a + 1, b] << [a, b - 1] << [a, b + 1]
        grid[a][b] = 0
      end
      ret = [ret, area].max
    end
  end
  ret
end

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
# grid =  [[0,0,0,0,0,0,0,0]]
# p max_area_of_island(grid)
p max_area_of_island(grid)

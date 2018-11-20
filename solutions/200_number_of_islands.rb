# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

# @param {Character[][]} grid
# @return {Integer}
def clear_off(grid, a, b)
  return if a >= grid.size || b >= grid[0].size ||
            a < 0 || b < 0 ||
            grid[a][b] == '0'
  grid[a][b] = '0'
  clear_off(grid, a + 1, b)
  clear_off(grid, a, b + 1)
  clear_off(grid, a - 1, b)
  clear_off(grid, a, b - 1)
end

def num_islands(grid)
  counter = 0
  (0..grid.size - 1).each do |i|
    (0..grid[0].size - 1).each do |j|
      next if grid[i][j] == '0'
      counter += 1
      clear_off(grid, i, j)
    end
  end
  counter
end

grid = [
  [0, 1, 0, 1, 0],
  [1, 1, 0, 1, 0],
  [0, 1, 0, 0, 1],
  [1, 0, 1, 0, 1]
].map { |lis| lis.map(&:to_s) }

# clear_off(grid, 0, 1)
p ['before', grid]
p num_islands(grid)
p ['after', grid]

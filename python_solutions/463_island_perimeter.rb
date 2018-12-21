# @param {Integer[][]} grid
# @return {Integer}
def island_perimeter(grid)
  res = 0
  0.upto(grid.size - 1).each do |i|
    0.upto(grid[0].size - 1).each do |j|
      next if grid[i][j].zero?

      res += 4
      res -= 2 if i < grid.size - 1 && grid[i + 1][j] == 1
      res -= 2 if j < grid[0].size - 1 && grid[i][j + 1] == 1
    end
  end
  res
end

grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]

p island_perimeter(grid)

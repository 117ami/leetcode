# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
# Example:
#
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image bel
# @param {Integer[][]} grid
# @return {Integer}
def island_perimeter(grid)
  c = 0
  (0..grid.size - 1).each do |row|
    (0..grid[0].size - 1).each do |col|
      next if grid[row][col].zero?
      c += 4
      c -= 2 if row > 0 && grid[row - 1][col] == 1 
      c -= 2 if col > 0 && grid[row][col - 1] == 1
    end
  end
  c
end

grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]

p island_perimeter(grid)

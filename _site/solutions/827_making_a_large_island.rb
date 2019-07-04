# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
# After, what is the size of the largest island?(An island is a 4-directionally connected group of 1s).
# Example 1:
# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:
# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 1.
# Example 3:
# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 1.
#
# Notes:
#   1 <= grid.length = grid[0].length <= 50.
#   0 <= grid[i][j] <= 1.
#

# @param {Integer[][]} grid
# @return {Integer}

# use color to mark colored island
def largest_island(grid)
  colored_island = Array.new(grid.size + 2) { Array.new(grid.size + 2, -1) }
  nex_color_index = 0
  max_color_area = { -1 => 0 }
  cache = {}

  gp_island = lambda do |i, j|
    return if cache.key?([i, j].join('-')) ||
              i < 0 || j < 0 || i >= grid.size || j >= grid.size ||
              grid[i][j].zero?
    cache[[i, j].join('-')] = nil
    gp_island.call(i + 1, j)
    gp_island.call(i - 1, j)
    gp_island.call(i, j - 1)
    gp_island.call(i, j + 1)
  end

  area = lambda do |i, j|
    return if colored_island[i + 1][j + 1] != -1 # already computed the max area
    gp_island.call(i, j)
    cache.each_key do |k|
      a, b = k.split('-').map(&:to_i)
      colored_island[a + 1][b + 1] = nex_color_index
    end
    if cache.size > 0
      max_color_area[nex_color_index] = cache.size
      nex_color_index += 1
      cache = {}
    end
  end

  res = 0

  0.upto(grid.size - 1) do |i|
    0.upto(grid.size - 1) do |j|
      neibors = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1], [i, j]]
      neibors.each { |a, b| area.call(a, b) }
      n = neibors.map { |a, b| colored_island[a + 1][b + 1] }.uniq.map { |a| max_color_area[a] }.reduce(:+)
      n += 1 if grid[i][j].zero?
      res = [n, res].max
    end
  end

  p colored_island
  p max_color_area
  res
end

grid = [
  [1, 0, 1, 0],
  [0, 1, 1, 0],
  [0, 1, 0, 1],
  [0, 0, 0, 1]
]

grid = [[1, 0], [0, 1]]

grid = [[1]]

p largest_island(grid)


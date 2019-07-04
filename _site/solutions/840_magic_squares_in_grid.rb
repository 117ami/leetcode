# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
#
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).
#
#
#
# Example 1:
#
# Input: [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276
#
# while this one is not:
# 384
# 519
# 762
#
# In total, there is only one magic square inside the given grid.
#
# Note:
#
#     1 <= grid.length <= 10
#     1 <= grid[0].length <= 10
#     0 <= grid[i][j] <= 15
#

# @param {Integer[][]} grid
# @return {Integer}
def num_magic_squares_inside(grid)
  return 0 if grid.size < 3 || grid[0].size < 3
  ret = 0
  is_magic = lambda do |i, j|
    arr = grid[i][j..j + 2]
    arr.concat(grid[i + 1][j..j + 2]).concat(grid[i + 2][j..j + 2])
    return false unless arr.sort == Array(1..9)
    s = grid[i][j..j + 2].reduce(:+)
    (i + 1..i + 2).each { |k| return false unless s == grid[k][j..j + 2].reduce(:+) }
    (j..j + 2).each { |k| return false unless s == grid[i][k] + grid[i + 1][k] + grid[i + 2][k] }
    return false unless s == grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
    return false unless s == grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]
    true
  end

  (0..grid.size - 3).each do |i|
    (0..grid[0].size - 3).each do |j|
      ret += 1 if is_magic.call(i, j)
    end
  end
  ret
end

grid = [[4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2]]
p num_magic_squares_inside(grid)

#
# @lc app=leetcode id=994 lang=ruby
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.25%)
# Total Accepted:    7.6K
# Total Submissions: 16.5K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
#
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
#
#
#
#
# Example 1:
#
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
#
# Example 2:
#
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
#
# Example 3:
#
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
#
#
#
#
# Note:
#
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
#
#
#
#
#
# @param {Integer[][]} grid
# @return {Integer}
def oranges_rotting(grid)
  trans = lambda do |i, j, v|
    return if i < 0 || j < 0 || i >= grid.size || j >= grid[0].size || grid[i][j].zero? || grid[i][j] == 2 || (grid[i][j] < 0 && grid[i][j].abs <= v.abs)

    grid[i][j] = v
    [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]].each do |ni, nj|
      trans.call(ni, nj, v - 1)
    end
  end

  0.upto(grid.size - 1).each do |i|
    0.upto(grid[0].size - 1).each do |j|
      next unless grid[i][j] == 2

      [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]].each do |ni, nj|
        trans.call(ni, nj, -1)
      end
    end
  end

  ans = 0
  0.upto(grid.size - 1).each do |i|
    0.upto(grid[0].size - 1).each do |j|
      return -1 if grid[i][j] == 1
      next if grid[i][j] >= 0
      ans = [ans, grid[i][j].abs].max
    end
  end
  ans 
end

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
p oranges_rotting(grid)

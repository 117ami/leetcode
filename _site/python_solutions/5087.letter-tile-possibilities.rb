#
# @lc app=leetcode id=5087 lang=ruby
#
# [5087] Letter Tile Possibilities
#
# https://leetcode.com/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (76.77%)
# Total Accepted:    2K
# Total Submissions: 2.6K
# Testcase Example:  '"AAB"'
#
# You have a set of tiles, where each tile has one letter tiles[i] printed on
# it.  Return the number of possible non-empty sequences of letters you can
# make.
#
#
#
# Example 1:
#
#
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
#
#
#
# Example 2:
#
#
# Input: "AAABBC"
# Output: 188
#
#
#
#
#
# Note:
#
#
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
#
#
#
# @param {String} tiles
# @return {Integer}

# t is either a string or an array
def counter(t)
  cter = Hash.new(0)
  arr = t.is_a?(String) ? t.chars : t
  arr.each do |c|
    cter[c] += 1
  end
  cter
end

def num_tile_possibilities(tiles)
  c = counter(tiles)
  res = 0
  dfs = lambda do |cter|
    sum = 0
    'A'.upto('Z').each do |ic|
      next unless cter[ic] > 0

      sum += 1
      cter[ic] -= 1
      sum += dfs.call(cter)
      cter[ic] += 1
    end
    sum
  end
  dfs.call(c)
end

tiles = 'AAABBC'
p num_tile_possibilities(tiles)

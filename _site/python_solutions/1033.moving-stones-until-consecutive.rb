#
# @lc app=leetcode id=1033 lang=ruby
#
# [1033] Moving Stones Until Consecutive
#
# https://leetcode.com/problems/moving-stones-until-consecutive/description/
#
# algorithms
# Easy (28.39%)
# Total Accepted:    2.5K
# Total Submissions: 8.9K
# Testcase Example:  '1\n2\n5'
#
# Three stones are on a number line at positions a, b, and c.
#
# Each turn, let's say the stones are currently at positions x, y, z with x < y
# < z.  You pick up the stone at either position x or position z, and move that
# stone to an integer position k, with x < k < z and k != y.
#
# The game ends when you cannot make any more moves, ie. the stones are in
# consecutive positions.
#
# When the game ends, what is the minimum and maximum number of moves that you
# could have made?  Return the answer as an length 2 array: answer =
# [minimum_moves, maximum_moves]
#
#
#
# Example 1:
#
#
# Input: a = 1, b = 2, c = 5
# Output: [1, 2]
# Explanation: Move stone from 5 to 4 then to 3, or we can move it directly to
# 3.
#
#
#
# Example 2:
#
#
# Input: a = 4, b = 3, c = 2
# Output: [0, 0]
# Explanation: We cannot make any moves.
#
#
#
#
#
# Note:
#
#
# 1 <= a <= 100
# 1 <= b <= 100
# 1 <= c <= 100
# a != b, b != c, c != a
#
#
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer[]}
def num_moves_stones(a, b, c)
  a, b, c = [a, b, c].sort
  res = [2, 0]
  res[0] = 1 if c - b <= 2 || b - a <= 2
  res[0] = 0 if a + 1 == b && b + 1 == c
  res[1] += b - a - 1
  res[1] += c - b - 1
  res
end

p num_moves_stones(3, 5, 1)

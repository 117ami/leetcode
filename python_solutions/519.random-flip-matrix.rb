#
# @lc app=leetcode id=519 lang=ruby
#
# [519] Random Flip Matrix
#
# https://leetcode.com/problems/random-flip-matrix/description/
#
# algorithms
# Medium (32.26%)
# Total Accepted:    2.5K
# Total Submissions: 7.8K
# Testcase Example:  '["Solution", "flip", "flip", "flip", "flip"]\n[[2, 2], [], [], [], []]'
#
# You are given the number of rows n_rows and number of columns n_cols of a 2D
# binary matrix where all values are initially 0. Write a function flip which
# chooses a 0 value uniformly at random, changes it to 1, and then returns the
# position [row.id, col.id] of that value. Also, write a function reset which
# sets all values back to 0. Try to minimize the number of calls to system's
# Math.random() and optimize the time and space complexity.
#
# Note:
#
#
# 1 <= n_rows, n_cols <= 10000
# 0 <= row.id < n_rows and 0 <= col.id < n_cols
# flip will not be called when the matrix has no 0 values left.
# the total number of calls to flip and reset will not exceed 1000.
#
#
# Example 1:
#
#
# Input:
# ["Solution","flip","flip","flip","flip"]
# [[2,3],[],[],[],[]]
# Output: [null,[0,1],[1,2],[1,0],[1,1]]
#
#
#
# Example 2:
#
#
# Input:
# ["Solution","flip","flip","reset","flip"]
# [[1,2],[],[],[],[]]
# Output: [null,[0,0],[0,1],null,[0,0]]
#
#
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has two arguments, n_rows and n_cols. flip and reset
# have no arguments. Arguments are always wrapped with a list, even if there
# aren't any.
#
#
class Solution
  #     :type n_rows: Integer
  #     :type n_cols: Integer
  def initialize(n_rows, n_cols)
    @ids = {}
    @n_rows = n_rows
    @n_cols = n_cols
    @total = n_rows * n_cols
  end

  #     :rtype: Integer[]
  def flip
    r = rand(@total)
    @total -= 1
    idx = @ids[r] || r 
    @ids[r], @ids[@total] = @ids[@total] || @total, idx
    [idx / @n_cols, idx % @n_cols]
  end

  #     :rtype: Void
  def reset
    @ids = {}
    @total = @n_rows * @n_cols
  end
end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()

# n_rows = 3
# rows = (0..n_rows).to_a.product((0..n_rows).to_a)
# res =  rows.sample
# p res
# rows.delete(res)
# p rows
p rand(3)
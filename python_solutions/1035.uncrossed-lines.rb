#
# @lc app=leetcode id=1035 lang=ruby
#
# [1035] Uncrossed Lines
#
# https://leetcode.com/problems/uncrossed-lines/description/
#
# algorithms
# Medium (43.52%)
# Total Accepted:    1.5K
# Total Submissions: 3.5K
# Testcase Example:  '[1,4,2]\n[1,2,4]'
#
# We write the integers of A and B (in the order they are given) on two
# separate horizontal lines.
#
# Now, we may draw a straight line connecting two numbers A[i] and B[j] as long
# as A[i] == B[j], and the line we draw does not intersect any other connecting
# (non-horizontal) line.
#
# Return the maximum number of connecting lines we can draw in this way.
#
#
#
# Example 1:
#
#
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will
# intersect the line from A[2]=2 to B[1]=2.
#
#
#
# Example 2:
#
#
# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3
#
#
#
# Example 3:
#
#
# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2
#
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 500
# 1 <= B.length <= 500
# 1 <= A[i], B[i] <= 2000
#
#
# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer}
def max_uncrossed_lines(a, b)
  res = Array.new(a.size + 1) { Array.new(b.size + 1, 0) }
  0.upto(a.size - 1).each do |i|
    0.upto(b.size - 1).each do |j|
      res[i + 1][j + 1] = if a[i] == b[j]
                            [res[i][j + 1], res[i + 1][j], 1 + res[i][j]].max
                          else
                            [res[i][j + 1], res[i + 1][j]].max
                          end
    end
  end
  # p res
  res.last.last
end

a = [1, 3, 7, 1, 7, 5]
b = [1, 9, 2, 5, 1]

# a = [2, 5, 1, 2, 5]
# b = [10, 5, 2, 1, 5, 2]

a = [1,3,7,1,7,5]
b = [1,9,2,5,1]
p max_uncrossed_lines(a, b)

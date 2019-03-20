#
# @lc app=leetcode id=1007 lang=ruby
#
# [1007] Minimum Domino Rotations For Equal Row
#
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/
#
# algorithms
# Medium (47.56%)
# Total Accepted:    4.8K
# Total Submissions: 10.2K
# Testcase Example:  '[2,1,2,4,2,2]\n[5,2,6,2,3,2]'
#
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of
# the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on
# each half of the tile.)
#
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
#
# Return the minimum number of rotations so that all the values in A are the
# same, or all the values in B are the same.
#
# If it cannot be done, return -1.
#
#
#
# Example 1:
#
#
#
#
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by A and B: before we do
# any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the
# top row equal to 2, as indicated by the second figure.
#
#
# Example 2:
#
#
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of
# values equal.
#
#
#
#
# Note:
#
#
# 1 <= A[i], B[i] <= 6
# 2 <= A.length == B.length <= 20000
#
#
#
# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer}
def min_domino_rotations(a, b)
  fa = fb = true
  return -1 if a.size != b.size
  return 0 if a.size <= 1

  0.upto(a.size-1).each do |i|
  	next if a[i] == a[0] || b[i] == a[0]
  	fa = false
  	break
  end

  0.upto(a.size-1).each do |i|
  	next if b[i] == b[0] || a[i] == b[0]
  	fb = false
  	break
  end

  return -1 if !fa && !fb
  m = fa ? a[0] : b[0]
  a.size - [a.count(m), b.count(m)].max
end

a = [2, 1, 2, 4, 2, 2]
b = [5, 2, 6, 2, 3, 2]
a = [2, 1, 1, 1, 2, 2, 2, 1, 1, 2]
b = [1, 1, 2, 1, 1, 1, 1, 2, 1, 1]
p min_domino_rotations(a, b)

#
# @lc app=leetcode id=1042 lang=ruby
#
# [1042] Flower Planting With No Adjacent
#
# https://leetcode.com/problems/flower-planting-with-no-adjacent/description/
#
# algorithms
# Easy (46.72%)
# Total Accepted:    3.9K
# Total Submissions: 8.3K
# Testcase Example:  '3\n[[1,2],[2,3],[3,1]]'
#
# You have N gardens, labelled 1 to N.  In each garden, you want to plant one
# of 4 types of flowers.
#
# paths[i] = [x, y] describes the existence of a bidirectional path from garden
# x to garden y.
#
# Also, there is no garden that has more than 3 paths coming into or leaving
# it.
#
# Your task is to choose a flower type for each garden such that, for any two
# gardens connected by a path, they have different types of flowers.
#
# Return any such a choice as an array answer, where answer[i] is the type of
# flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3,
# or 4.  It is guaranteed an answer exists.
#
#
#
#
# Example 1:
#
#
# Input: N = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
#
#
#
# Example 2:
#
#
# Input: N = 4, paths = [[1,2],[3,4]]
# Output: [1,2,1,2]
#
#
#
# Example 3:
#
#
# Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# Output: [1,2,3,4]
#
#
#
#
# Note:
#
#
# 1 <= N <= 10000
# 0 <= paths.size <= 20000
# No garden has 4 or more paths coming into or leaving it.
# It is guaranteed an answer exists.
#
#
#
#
#
# @param {Integer} n
# @param {Integer[][]} paths
# @return {Integer[]}

require 'set'
def garden_no_adj(n, paths)
  res = Array.new(n, 0)
  gd = Array.new(n) { |_| Set.new }
  paths.each do |i, j|
    gd[i - 1] << j - 1
    gd[j - 1] << i - 1
  end

  0.upto(n - 1).each do |i|
    used = Hash.new(false).tap { |h| gd[i].each { |j| h[res[j]] = true } }
    res[i] = ((1..4).to_a - used.keys).first
  end
  res
end

n = 4
paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
# paths = [[1, 2], [2, 3], [3, 1]]
a = [1, 2, 3, 4]
b = [2, 3]
# n = 3
p garden_no_adj(n, paths)

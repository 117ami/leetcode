#
# @lc app=leetcode id=939 lang=ruby
#
# [939] Minimum Area Rectangle
#
# https://leetcode.com/problems/minimum-area-rectangle/description/
#
# algorithms
# Medium (50.17%)
# Total Accepted:    15.7K
# Total Submissions: 31.3K
# Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
#
# Given a set of points in the xy-plane, determine the minimum area of a
# rectangle formed from these points, with sides parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.
#
#
#
#
# Example 1:
#
#
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
#
#
#
# Example 2:
#
#
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
#
#
#
#
# Note:
#
#
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
#
#
#
#
# @param {Integer[][]} points
# @return {Integer}

require 'set'
def min_area_rect(points)
  res = 1.0 / 0
  points.uniq!
  len = points.size
  lenx = points.map(&:first).uniq.size
  leny = points.map(&:last).size
  return 0 if len == lenx || len == leny

  points.map!(&:reverse) if leny > lenx
  points.sort_by!(&:last).sort_by!(&:first)

  prex = points.first.first
  prei = 0
  visited = {}

  points.each_with_index do |pair, i|
    if prex != pair.first
      prex = pair.first
      prei = i
    else
      x, y1 = pair
      prei.upto(i - 1).each do |j|
        y2 = points[j].last
        res = [res, (y1 - y2) * (x - visited[[y1, y2]])].min if visited.key?([y1, y2])
        visited[[y1, y2]] = x
      end
    end
  end

  res == 1.0 / 0 ? 0 : res
end

points = [[1, 1], [4, 3], [3, 1], [3, 3], [4, 1], [1, 3], [1, 7]]
points = [[1,1],[1,3],[3,1],[3,3],[2,2]]

p min_area_rect(points)

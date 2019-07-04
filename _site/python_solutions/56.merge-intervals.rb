#
# @lc app=leetcode id=56 lang=ruby
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (35.42%)
# Total Accepted:    337.2K
# Total Submissions: 950.8K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#
# @param {Integer[][]} intervals
# @return {Integer[][]}

def merge(intervals)
  res = []
  intervals.sort_by(&:first).each do |i|
    if res.empty? || res.last.last < i.first
      res << i
    else
      res[-1][-1] = [res[-1][-1], i.last].max
    end
  end
  res
end

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [0, 4]]
intervals = [[1, 4], [2, 3]]
p merge(intervals)

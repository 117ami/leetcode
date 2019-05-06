#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (41.51%)
# Total Accepted:    37.4K
# Total Submissions: 90.1K
# Testcase Example:  '[[1,2]]'
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
#
# Note:
#
#
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
# each other.
#
#
#
#
# Example 1:
#
#
# Input: [ [1,2], [2,3], [3,4], [1,3] ]
#
# Output: 1
#
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
#
#
#
#
# Example 2:
#
#
# Input: [ [1,2], [1,2], [1,2] ]
#
# Output: 2
#
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
#
#
#
#
# Example 3:
#
#
# Input: [ [1,2], [2,3] ]
#
# Output: 0
#
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
#
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#


class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        res = 0
        end = float('-inf')
        for i in intervals:
            if i[0] < end:
                res += 1
            else:
                end = i[1]
        return res


intervals = [[10, 16], [2, 8], [1, 6], [7, 12]]
intervals = [[1, 2], [1, 2], [1, 2]]
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(Solution().eraseOverlapIntervals(intervals))

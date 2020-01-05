from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=715 lang=python3
#
# [715] Range Module
#
# https://leetcode.com/problems/range-module/description/
#
# algorithms
# Hard (37.33%)
# Total Accepted:    15.3K
# Total Submissions: 40.9K
# Testcase Example:  '["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]\n' + '[[],[10,20],[14,16],[10,14],[13,15],[16,17]]'
#
# A Range Module is a module that tracks ranges of numbers. Your task is to
# design and implement the following interfaces in an efficient manner.
#
# addRange(int left, int right) Adds the half-open interval [left, right),
# tracking every real number in that interval.  Adding an interval that
# partially overlaps with currently tracked numbers should add any numbers in
# the interval [left, right) that are not already tracked.
#
# queryRange(int left, int right) Returns true if and only if every real number
# in the interval [left, right)
# ⁠is currently being tracked.
#
# removeRange(int left, int right) Stops tracking every real number currently
# being tracked in the interval [left, right).
#
# Example 1:
#
# addRange(10, 20): null
# removeRange(14, 16): null
# queryRange(10, 14): true (Every number in [10, 14) is being tracked)
# queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not
# being tracked)
# queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked,
# despite the remove operation)
#
#
#
# Note:
# A half open interval [left, right) denotes all real numbers left .
#
# 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
# The total number of calls to addRange in a single test case is at most 1000.
# The total number of calls to queryRange in a single test case is at most
# 5000.
# The total number of calls to removeRange in a single test case is at most
# 1000.
#
#


class RangeModule:

    def __init__(self):
        self.ds = []

    def addRange(self, left, right):
        i, j = bl(self.ds, left), br(self.ds, right)
        # print(i, j)
        self.ds[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)
        # print(self.ds)

    def queryRange(self, left, right):
        i, j = br(self.ds, left), bl(self.ds, right)
        # print(i, j)
        return i == j and i % 2 == 1

    def removeRange(self, left, right):
        i, j = bl(self.ds, left), br(self.ds, right)
        self.ds[i:j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(14, 16)
obj.addRange(20, 39)
obj.queryRange(23, 33)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

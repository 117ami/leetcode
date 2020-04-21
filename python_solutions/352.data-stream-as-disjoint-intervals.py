from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right, insort
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (45.89%)
# Total Accepted:    32.1K
# Total Submissions: 70K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n' +
# '[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
# Given a data stream input of non-negative integers a1, a2, ..., an, ...,
# summarize the numbers seen so far as a list of disjoint intervals.
#
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6,
# ..., then the summary will be:
#
#
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
#
#
#
#
# Follow up:
#
# What if there are lots of merges and the number of disjoint intervals are
# small compared to the data stream's size?
#
#


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.it = [-2, -2, 1 << 32, 1 << 32]

    def addNum(self, val: int) -> None:
        i = bisect_left(self.it, val)
        print(val, i)
        if self.it[i] == val or i % 2 == 1:
            return
        if self.it[i - 1] + 1 == val and val + 1 == self.it[i]:
            self.it = self.it[:i - 1] + self.it[i + 1:]
        elif self.it[i - 1] + 1 == val:
            self.it[i - 1] = val
        elif self.it[i] == val + 1:
            self.it[i] = val
        else:
            self.it = self.it[:i] + [val, val] + self.it[i:]

    def getIntervals(self) -> List[List[int]]:
        for i in range(2, len(self.it) - 2, 2):
            yield self.it[i:i + 2]


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
for n in [6,6,0,4,8,7,6,4,7,5]:
    obj.addNum(n)
    print(list(obj.getIntervals()))
# obj.addNum(val)
# param_2 = obj.getIntervals()

# sol = Solution()
# it = [1,2,8,9]
# print(bisect_left(it, 3))

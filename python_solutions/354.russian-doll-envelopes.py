from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (34.77%)
# Total Accepted:    54.6K
# Total Submissions: 157.2K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
#
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
#
# Note:
# Rotation is not allowed.
#
# Example:
#
#
#
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
#
#
#
#


class Solution:
    def maxEnvelopes(self, es):
        es.sort(key=lambda x: (x[0], -x[1]))
        heights = [0x3f3f3f3f] * len(es)
        for _, h in es:
            i = bisect_left(heights, h)
            heights[i] = h 
        return bisect_right(heights, 0x3f3f3f3f - 1)


sol = Solution()
# es = [[5, 4], [6, 4], [6, 7], [2, 3]]
es = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
# # es = [[4,5],[4,6],[6,7],[2,3],[1,1],[1,1]]
print(sol.maxEnvelopes(es))

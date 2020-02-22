from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left,  bisect_right 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=699 lang=python3
#
# [699] Falling Squares
#
# https://leetcode.com/problems/falling-squares/description/
#
# algorithms
# Hard (41.04%)
# Total Accepted:    11.6K
# Total Submissions: 28.3K
# Testcase Example:  '[[1,2],[2,3],[6,1]]'
#
# On an infinite number line (x-axis), we drop given squares in the order they
# are given.
# 
# The i-th square dropped (positions[i] = (left, side_length)) is a square with
# the left-most point being positions[i][0] and sidelength positions[i][1].
# 
# The square is dropped with the bottom edge parallel to the number line, and
# from a higher height than all currently landed squares. We wait for each
# square to stick before dropping the next.
# 
# The squares are infinitely sticky on their bottom edge, and will remain fixed
# to any positive length surface they touch (either the number line or another
# square). Squares dropped adjacent to each other will not stick together
# prematurely.
# 
# 
# Return a list ans of heights. Each height ans[i] represents the current
# highest height of any square we have dropped, after dropping squares
# represented by positions[0], positions[1], ..., positions[i].
# 
# Example 1:
# 
# 
# Input: [[1, 2], [2, 3], [6, 1]]
# Output: [2, 5, 5]
# Explanation:
# 
# 
# After the first drop of positions[0] = [1, 2]: _aa _aa ------- The maximum
# height of any square is 2.
# 
# After the second drop of positions[1] = [2, 3]: __aaa __aaa __aaa _aa__ _aa__
# -------------- The maximum height of any square is 5. The larger square stays
# on top of the smaller square despite where its center of gravity is, because
# squares are infinitely sticky on their bottom edge.
# 
# After the third drop of positions[1] = [6, 1]: __aaa __aaa __aaa _aa _aa___a
# -------------- The maximum height of any square is still 5. Thus, we return
# an answer of [2, 5, 5].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [[100, 100], [200, 100]]
# Output: [100, 100]
# Explanation: Adjacent squares don't get stuck prematurely - only their bottom
# edge can stick to surfaces.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= positions.length <= 1000.
# 1 <= positions[i][0] <= 10^8.
# 1 <= positions[i][1] <= 10^6.
# 
# 
# 
# 
#
class Interval:
    def __init__(self, start, end, height):
        self.start = start
        self.end = end 
        self.height = height

class Solution:
    def fallingSquares(self, positions):
        pos, heights = [0], [0]
        res = []
        maxheight = 0
        for l, sh in positions:
            i = bisect_right(pos, l)
            j = bisect_left(pos, l + sh)
            h = max(heights[i-1:j] or [0]) + sh 
            pos[i:j] = [l, l + sh]
            heights[i:j] = [h, heights[j-1]]
            maxheight = max(maxheight, h)
            res.append(maxheight)
        return res 

    def fallingSquares_2(self, pos):
        res = []
        intervals = []
        h = 0 
        for s, sh in pos:
            itv = Interval(s, s + sh, sh)
            h = self.get_max_height(intervals, itv)
            res.append(max(h, res[-1]) if res else h)
        # for i in intervals:
        #     print(i.start, i.end, i.height)
        return res 
    
    def get_max_height(self, intervals, itv):
        premax = 0
        for it in intervals:
            if it.end <= itv.start or it.start >= itv.end: continue 
            premax = max(premax, it.height)
        itv.height += premax
        intervals.append(itv)
        return itv.height


sol = Solution()
pos = [[1, 2], [2, 3], [6, 1]]
pos = [[100,100],[200,100]]
print(sol.fallingSquares(pos))


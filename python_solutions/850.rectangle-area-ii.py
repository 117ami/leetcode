from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=850 lang=python3
#
# [850] Rectangle Area II
#
# https://leetcode.com/problems/rectangle-area-ii/description/
#
# algorithms
# Hard (46.12%)
# Total Accepted:    9.3K
# Total Submissions: 20.2K
# Testcase Example:  '[[0,0,2,2],[1,0,2,3],[1,0,3,1]]'
#
# We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1,
# y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner,
# and (x2, y2) are the coordinates of the top-right corner of the ith
# rectangle.
#
# Find the total area covered by all rectangles in the plane.  Since the answer
# may be too large, return it modulo 10^9 + 7.
#
#
#
# Example 1:
#
#
# Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: As illustrated in the picture.
#
#
# Example 2:
#
#
# Input: [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 =
# (-7)^2 = 49.
#
#
# Note:
#
#
# 1 <= rectangles.length <= 200
# rectanges[i].length = 4
# 0 <= rectangles[i][j] <= 10^9
# The total area covered by all rectangles will never exceed 2^63 - 1 and thus
# will fit in a 64-bit signed integer.
#
#
MOD = pow(10, 9) + 7


def is_rectangle_overlap(a, b):
    if a[0] > b[0]:
        return is_rectangle_overlap(b, a)
    return not (a[2] <= b[0] or a[3] <= b[1] or a[1] >= b[3])


def intersecting_area(a, b):
    # Assume two rectangles a, b overlap
    return abs(min(a[2], b[2]) - max(a[0], b[0])) * \
        abs(min(a[3], b[3]) - max(a[1], b[1]))


class Solution:
    def rectangleArea(self, rectangles):
        def add_rects(rects, curr, start):
            if start >= len(rects):
                rects.append(curr)
                return
            
            cx1, cy1, cx2, cy2 = curr
            rx1, ry1, rx2, ry2 = rects[start]
            if cx2 <= rx1 or cx1 >= rx2 or cy2 <= ry1 or cy1 >= ry2:
                add_rects(rects, curr, start+1)
                return
            
            if cx1 < rx1:
                add_rects(rects, [cx1, cy1, rx1, cy2], start+1)
            if cx2 > rx2:
                add_rects(rects, [rx2, cy1, cx2, cy2], start+1)
            if cy1 < ry1:
                add_rects(rects, [max(cx1, rx1), cy1, min(cx2, rx2), ry1], start+1)
            if cy2 > ry2:
                add_rects(rects, [max(cx1, rx1), ry2, min(cx2, rx2), cy2], start+1)
            
        rects = []
        for r in rectangles:
            add_rects(rects, r, 0)
        area = lambda r: (r[2]-r[0])*(r[3]-r[1])
        return sum(area(r) for r in rects) % (10**9+7)

sol = Solution()
rs = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
print(sol.rectangleArea(rs))

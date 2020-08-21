from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1499 lang=python3
#
# [1499] Max Value of Equation
#
# https://leetcode.com/problems/max-value-of-equation/description/
#
# algorithms
# Hard (31.72%)
# Total Accepted:    1.7K
# Total Submissions: 3.9K
# Testcase Example:  '[[1,3],[2,0],[5,10],[6,-10]]\n1'
#
# Given an array points containing the coordinates of points on a 2D plane,
# sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all
# 1 <= i < j <= points.length. You are also given an integer k.
#
# Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <=
# k and 1 <= i < j <= points.length. It is guaranteed that there exists at
# least one pair of points that satisfy the constraint |xi - xj| <= k.
#
#
# Example 1:
#
#
# Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
# Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if
# we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points
# also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
# No other pairs satisfy the condition, so we return the max of 4 and 1.
#
# Example 2:
#
#
# Input: points = [[0,0],[3,0],[9,2]], k = 3
# Output: 3
# Explanation: Only the first two points have an absolute difference of 3 or
# less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
#
#
#
# Constraints:
#
#
# 2 <= points.length <= 10^5
# points[i].length == 2
# -10^8 <= points[i][0], points[i][1] <= 10^8
# 0 <= k <= 2 * 10^8
# points[i][0] < points[j][0] for all 1 <= i < j <= points.length
# xi form a strictly increasing sequence.
#
#
#


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        d = deque()
        res = float('-inf')
        for x, y in points:
            while d and d[0][0] + k < x:
                d.popleft()
            if d:
                res = max(res, d[0][1] + y + x)

            while d and d[-1][1] <= y - x:
                d.pop()
            d.append([x, y - x])
        return res


sol = Solution()


points = [[1, 3], [2, 0], [5, 10], [6, -10]]
k = 1
# points = [[0,0],[3,0],[9,2]], k = 3
print(sol.findMaxValueOfEquation(points, k))

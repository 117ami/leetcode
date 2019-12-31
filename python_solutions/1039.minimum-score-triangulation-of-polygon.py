from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=1039 lang=python3
#
# [1039] Minimum Score Triangulation of Polygon
#
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/
#
# algorithms
# Medium (45.11%)
# Total Accepted:    5.5K
# Total Submissions: 12.1K
# Testcase Example:  '[1,2,3]'
#
# Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i],
# ..., A[N-1] in clockwise order.
#
# Suppose you triangulate the polygon into N-2 triangles.  For each triangle,
# the value of that triangle is the product of the labels of the vertices, and
# the total score of the triangulation is the sum of these values over all N-2
# triangles in the triangulation.
#
# Return the smallest possible total score that you can achieve with some
# triangulation of the polygon.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: 6
# Explanation: The polygon is already triangulated, and the score of the only
# triangle is 6.
#
#
#
# Example 2:
#
#
#
#
# Input: [3,7,4,5]
# Output: 144
# Explanation: There are two triangulations, with possible scores: 3*7*5 +
# 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
#
#
#
# Example 3:
#
#
# Input: [1,3,1,4,1,5]
# Output: 13
# Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5
# + 1*1*1 = 13.
#
#
#
#
# Note:
#
#
# 3 <= A.length <= 50
# 1 <= A[i] <= 100
#
#
#
#
#


class Solution:
    def minScoreTriangulation(self, a):
        n = len(a)
        dp = [[0] * 50 for _ in range(50)]

        def product(i, j):
            if j == 0:
                j = n - 1
            if dp[i][j] > 0:
                return dp[i][j]
            res = 0
            for k in range(i + 1, j):
                res = min(0x3f3f3f3f if res == 0 else res,
                          product(i, k) + a[i] * a[j] * a[k] + product(k, j))

            dp[i][j] = res
            return res
        return product(0, n - 1)


sol = Solution()
a = [1, 3, 1, 4, 1, 5]
a = [3, 7, 4, 5]
print(sol.minScoreTriangulation(a))

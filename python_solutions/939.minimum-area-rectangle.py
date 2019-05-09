#
# @lc app=leetcode id=939 lang=python3
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


class Solution:
    def minAreaRect(self, points):
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if n == nx or n == ny:
            return 0
        if ny > nx:
            points = [(y, x) for x, y in points]
        points.sort(key=lambda p: p[1])
        points.sort(key=lambda p: p[0])

        res = float('inf')
        visited = {}
        prex = points[0][0]
        prei = 0

        for i, pair in enumerate(points):
            x, y = pair
            if prex != x:
                prex, prei = x, i
            for j in range(prei, i):
                y2 = points[j][1]

                if (y, y2) in visited:
                    res = min(res, (x - visited[y, y2]) * (y - y2))
                    # print(y, y2, res)
                visited[y, y2] = x

        return res if res < float('inf') else 0


points = [[1, 1], [4, 3], [3, 1], [3, 3], [4, 1], [1, 3]]
points = [[1, 2], [3, 2], [1, 3], [3, 3], [3, 0], [1, 4], [4, 2], [4, 0]]
print(Solution().minAreaRect(points))

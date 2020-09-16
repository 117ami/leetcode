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
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007


#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (31.62%)
# Total Accepted:    1.7K
# Total Submissions: 5.4K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
# absolute value of val.
#
# Return the minimum cost to make all points connected. All points are
# connected if there is exactly one simple path between any two points.
#
#
# Example 1:
#
#
#
#
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:
#
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
#
#
# Example 2:
#
#
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
#
#
# Example 3:
#
#
# Input: points = [[0,0],[1,1],[1,0],[-1,1]]
# Output: 4
#
#
# Example 4:
#
#
# Input: points = [[-1000000,-1000000],[1000000,1000000]]
# Output: 4000000
#
#
# Example 5:
#
#
# Input: points = [[0,0]]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.
#
#
#
class Solution:
    def minCostConnectPoints(self, ps: List[List[int]]) -> int:
        n = len(ps)
        if n < 2: return 0
        keys, visited = [MAX] * n, [False] * n
        keys[0] = 0
        cost = 0

        for _ in range(n):
            idx, n_min = 0, MAX
            for j in range(n):
                if not visited[j] and keys[j] < n_min:
                    idx, n_min = j, keys[j]
            
            visited[idx] = True
            cost += n_min

            for j in range(n):
                if not visited[j]:
                    weight = abs(ps[idx][0] - ps[j][0]) + abs(ps[idx][1] -
                                                              ps[j][1])
                    if weight < keys[j]:
                        keys[j] = weight

        return cost


sol = Solution()

points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
# points = [[3, 12], [-2, 5], [-4, 1]]
# points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
# points = [[-1000000, -1000000], [1000000, 1000000]]
# points = [[0, 0]]
print(sol.minCostConnectPoints(points))

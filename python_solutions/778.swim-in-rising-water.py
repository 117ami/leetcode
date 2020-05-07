import heapq
from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#
# https://leetcode.com/problems/swim-in-rising-water/description/
#
# algorithms
# Hard (51.63%)
# Total Accepted:    21.4K
# Total Submissions: 41.3K
# Testcase Example:  '[[0,2],[1,3]]'
#
# On an N x N grid, each square grid[i][j] represents the elevation at that
# point (i,j).
#
# Now rain starts to fall. At time t, the depth of the water everywhere is t.
# You can swim from a square to another 4-directionally adjacent square if and
# only if the elevation of both squares individually are at most t. You can
# swim infinite distance in zero time. Of course, you must stay within the
# boundaries of the grid during your swim.
#
# You start at the top left square (0, 0). What is the least time until you can
# reach the bottom right square (N-1, N-1)?
#
# Example 1:
#
#
# Input: [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a
# higher elevation than t = 0.
#
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
#
#
# Example 2:
#
#
# Input:
# [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation:
# ⁠0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6
#
# The final route is marked in bold.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
#
#
# Note:
#
#
# 2 <= N <= 50.
# grid[i][j] is a permutation of [0, ..., N*N - 1].
#
#
#


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        arr = [(grid[0][0], 0, 0)]
        cc = set()
        res = 0
        heapq.heapify(arr)
        while True:
            n, i, j = heapq.heappop(arr)
            res = max(res, n)
            if i == j == len(grid) - 1:
                return res
            cc.add((i, j))
            for ii, jj in ([i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]):
                if 0 <= ii < len(grid) and 0 <= jj < len(
                        grid[0]) and (ii, jj) not in cc:
                    heapq.heappush(arr, (grid[ii][jj], ii, jj))


sol = Solution()
grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
    12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
print(sol.swimInWater(grid))

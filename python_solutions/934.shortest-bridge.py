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
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (46.96%)
# Total Accepted:    23.4K
# Total Submissions: 49.8K
# Testcase Example:  '[[0,1],[1,0]]'
#
# In a given 2D binary array A, there are two islands.  (An island is a
# 4-directionally connected group of 1s not connected to any other 1s.)
#
# Now, we may change 0s to 1s so as to connect the two islands together to form
# 1 island.
#
# Return the smallest number of 0s that must be flipped.  (It is guaranteed
# that the answer is at least 1.)
#
#
# Example 1:
# Input: A = [[0,1],[1,0]]
# Output: 1
# Example 2:
# Input: A = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:
# Input: A = [
# [1,1,1,1,1],
# [1,0,0,0,1],
# [1,0,1,0,1],
# [1,0,0,0,1],
# [1,1,1,1,1]]
# Output: 1
#
#
# Constraints:
#
#
# 2 <= A.length == A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1
#
#
#


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n = len(A)
        borders = []

        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return (i, j)

        def dfs(i, j):
            A[i][j] = 2
            borders.append((i, j))
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)

        dfs(*first())
        for step in range(0, 100):
            tmp = []
            for i, j in borders:
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            tmp.append((x, y))
            borders = tmp


sol = Solution()
A = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
print(sol.shortestBridge(A))

from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
#
# algorithms
# Medium (55.09%)
# Total Accepted:    42.8K
# Total Submissions: 77.7K
# Testcase Example:  '[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]'
#
# On a 2D plane, we place stones at some integer coordinate points.  Each
# coordinate point may have at most one stone.
#
# Now, a move consists of removing a stone that shares a column or row with
# another stone on the grid.
#
# What is the largest possible number of moves we can make?
#
#
#
#
# Example 1:
#
#
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
#
#
#
# Example 2:
#
#
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
#
#
#
# Example 3:
#
#
# Input: stones = [[0,0]]
# Output: 0
#
#
#
#
# Note:
#
#
# 1 <= stones.length <= 1000
# 0 <= stones[i][j] < 10000
#
#
#
#
#
#


class UF:
    def __init__(self):
        self.p = {}

    def union(self, x, y):
        self.p.setdefault(x, x)
        self.p.setdefault(y, y)
        self.p[self.find(x)] = self.find(y)

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    def removeStones(self, ss):
        uf = UF()
        for r, c in ss:
            uf.union(r, ~c)
        return len(ss) - len({uf.find(k) for k in uf.p})


sol = Solution()
# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

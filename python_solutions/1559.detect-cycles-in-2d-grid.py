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
# @lc app=leetcode id=1559 lang=python3
#
# [1559] Detect Cycles in 2D Grid
#
# https://leetcode.com/problems/detect-cycles-in-2d-grid/description/
#
# algorithms
# Hard (41.58%)
# Total Accepted:    3.7K
# Total Submissions: 8.8K
# Testcase Example:  '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]'
#
# Given a 2D array of characters grid of size m x n, you need to find if there
# exists any cycle consisting of the same value in grid.
#
# A cycle is a path of length 4 or more in the grid that starts and ends at the
# same cell. From a given cell, you can move to one of the cells adjacent to it
# - in one of the four directions (up, down, left, or right), if it has the
# same value of the current cell.
#
# Also, you cannot move to the cell that you visited in your last move. For
# example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2)
# we visited (1, 1) which was the last visited cell.
#
# Return true if any cycle of the same value exists in grid, otherwise, return
# false.
#
#
# Example 1:
#
#
#
#
# Input: grid =
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true
# Explanation: There are two valid cycles shown in different colors in the
# image below:
#
#
#
# Example 2:
#
#
#
#
# Input: grid =
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# Explanation: There is only one valid cycle highlighted in the image below:
#
#
#
# Example 3:
#
#
#
#
# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m <= 500
# 1 <= n <= 500
# grid consists only of lowercase English letters.
#
#
#
dirs = [-1, 0, 1, 0, -1]


def pair2id(i, j):
    return i * 500 + j


class Solution:
    def is_cycle(self, g, i, j, a, b):
        self.visited.add(pair2id(i, j))
        for d in range(4):
            ni, nj = i + dirs[d], j + dirs[d + 1]
            if 0 <= ni < len(g) and 0 <= nj < len(
                    g[0]) and (ni != a or nj != b) and g[i][j] == g[ni][nj]:
                if pair2id(ni, nj) in self.visited or self.is_cycle(
                        g, ni, nj, i, j):
                    return True
        return False

    def containsCycle(self, g: List[List[str]]) -> bool:
        self.visited = set()
        n, m = len(g), len(g[0])
        for i in range(n):
            for j in range(m):
                cid = i * 500 + j
                if cid not in self.visited and self.is_cycle(g, i, j, -1, -1):
                    return True
        return False


sol = Solution()

grid = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"],
        ["a", "a", "a", "a"]]
grid = [["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"],
        ["f", "c", "c", "c"]]
grid = [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]
print(sol.containsCycle(grid))

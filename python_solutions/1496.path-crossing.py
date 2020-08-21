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
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#
# https://leetcode.com/problems/path-crossing/description/
#
# algorithms
# Easy (52.68%)
# Total Accepted:    5.3K
# Total Submissions: 10K
# Testcase Example:  '"NES"'
#
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
# moving one unit north, south, east, or west, respectively. You start at the
# origin (0, 0) on a 2D plane and walk on the path specified by path.
#
# Return True if the path crosses itself at any point, that is, if at any time
# you are on a location you've previously visited. Return False otherwise.
#
#
# Example 1:
#
#
#
#
# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.
#
#
# Example 2:
#
#
#
#
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
#
#
# Constraints:
#
#
# 1 <= path.length <= 10^4
# path will only consist of characters in {'N', 'S', 'E', 'W}
#
#
#


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cc = set()
        cur = (0, 0)
        cc.add(cur)
        for p in path:
            x = cur[0] + (1 if p == 'E' else (-1 if p == 'W' else 0))
            y = cur[1] + (1 if p == 'N' else (-1 if p == 'S' else 0))
            cur = (x, y)

            if cur in cc:
                return True
            cc.add(cur)
        return False


sol = Solution()
path = 'NES'
print(sol.isPathCrossing(path))

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
# @lc app=leetcode id=1411 lang=python3
#
# [1411] Number of Ways to Paint N × 3 Grid
#
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/
#
# algorithms
# Hard (59.43%)
# Total Accepted:    5K
# Total Submissions: 8.2K
# Testcase Example:  '1'
#
# You have a grid of size n x 3 and you want to paint each cell of the grid
# with exactly one of the three colours: Red, Yellow or Green while making sure
# that no two adjacent cells have the same colour (i.e no two cells that share
# vertical or horizontal sides have the same colour).
#
# You are given n the number of rows of the grid.
#
# Return the number of ways you can paint this grid. As the answer may grow
# large, the answer must be computed modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown:
#
#
#
# Example 2:
#
#
# Input: n = 2
# Output: 54
#
#
# Example 3:
#
#
# Input: n = 3
# Output: 246
#
#
# Example 4:
#
#
# Input: n = 7
# Output: 106494
#
#
# Example 5:
#
#
# Input: n = 5000
# Output: 30228214
#
#
#
# Constraints:
#
#
# n == grid.length
# grid[i].length == 3
# 1 <= n <= 5000
#
#


class Solution:
    def numOfWays(self, n: int) -> int:
        s_121 = s_123 = 6
        mod = 10**9 + 7
        for i in range(n - 1):
            new_s_121 = s_121 * 3 + s_123 * 2
            new_s_123 = s_121 * 2 + s_123 * 2
            s_121 = new_s_121 % mod
            s_123 = new_s_123 % mod

        return (s_121 + s_123) % mod


sol = Solution()
print(sol.numOfWays(5000))

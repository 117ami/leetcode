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
# @lc app=leetcode id=1504 lang=python3
#
# [1504] Count Submatrices With All Ones
#
# https://leetcode.com/problems/count-submatrices-with-all-ones/description/
#
# algorithms
# Medium (49.18%)
# Total Accepted:    5.5K
# Total Submissions: 9.3K
# Testcase Example:  '[[1,0,1],[1,1,0],[1,1,0]]'
#
# Given a rows * columns matrix mat of ones and zeros, return how many
# submatrices have all ones.
#
#
# Example 1:
#
#
# Input: mat = [[1,0,1],
# [1,1,0],
# [1,1,0]]
# Output: 13
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2.
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
#
#
# Example 2:
#
#
# Input: mat = [[0,1,1,0],
# [0,1,1,1],
# [1,1,1,0]]
# Output: 24
# Explanation:
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3.
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2.
# There are 2 rectangles of side 3x1.
# There is 1 rectangle of side 3x2.
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
#
#
# Example 3:
#
#
# Input: mat = [[1,1,1,1,1,1]]
# Output: 21
#
#
# Example 4:
#
#
# Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
# Output: 5
#
#
#
# Constraints:
#
#
# 1 <= rows <= 150
# 1 <= columns <= 150
# 0 <= mat[i][j] <= 1
#
#


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        def helper(arr):
            _sum = [0] * len(arr)
            st = [] # A stack storing indexes.
            for i, a in enumerate(arr):
                while st and arr[st[-1]] >= a:
                    st.pop()
                if st:
                    _pre_idx = st[-1]
                    _sum[i] = _sum[_pre_idx]
                    _sum[i] += a * (i - st[-1])
                else:
                    _sum[i] = a * (i + 1)
                st.append(i)
            return sum(_sum)

        m, n = len(mat), len(mat[0])
        ans = 0
        h = [0] * n

        for i in range(m):
            for j in range(n):
                h[j] = h[j] + 1 if mat[i][j] else 0
            print(helper(h))
            ans += helper(h)

        return ans


sol = Solution()
mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
print(sol.numSubmat(mat))

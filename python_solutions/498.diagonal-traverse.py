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
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (46.98%)
# Total Accepted:    72.8K
# Total Submissions: 154.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
#
#
#
# Example:
#
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]
#
# Explanation:
#
#
#
#
#
# Note:
#
# The total number of elements of the given matrix will not exceed 10,000.
#
#


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if not nums: return []
        m, n = len(nums), len(nums[0])
        cc = [deque() for _ in range(2 * max(n, m))]
        for i in range(m):
            for j in range(n):
                if (i + j) % 2 == 1:
                    cc[i + j].append(nums[i][j])
                else:
                    cc[i + j].appendleft(nums[i][j])

        return [n for d in cc for n in d]


sol = Solution()
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ]
matrix = [[6, 9, 7]]
matrix = []
print(sol.findDiagonalOrder(matrix))

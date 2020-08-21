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
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (48.96%)
# Total Accepted:    290.7K
# Total Submissions: 592.6K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
#


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        for i in range(1, rowIndex + 1):
            cur = [1] * (i + 1)
            if i > 1:
                for j in range(1, len(cur) - 1):
                    cur[j] = pre[j - 1] + pre[j]
            pre = cur[:]
        return pre


sol = Solution()


# for inputs in range(10):
    # print(sol.getRow(inputs))

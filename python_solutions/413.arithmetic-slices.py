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
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#
# https://leetcode.com/problems/arithmetic-slices/description/
#
# algorithms
# Medium (57.92%)
# Total Accepted:    91.8K
# Total Submissions: 158.5K
# Testcase Example:  '[1,2,3,4]'
#
# A sequence of numbers is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
#
# For example, these are arithmetic sequences:
#
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
#
# The following sequence is not arithmetic.
#
#
# 1, 1, 2, 5, 7
#
#
# A zero-indexed array A consisting of N numbers is given. A slice of that
# array is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
# A slice (P, Q) of the array A is called arithmetic if the sequence:
# A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means
# that P + 1 < Q.
#
# The function should return the number of arithmetic slices in the array A.
#
#
# Example:
#
#
# A = [1, 2, 3, 4]
#
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3,
# 4] itself.
#
#
#
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        cur = _sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                cur += 1
                _sum += cur
            else:
                cur = 0
        return _sum


sol = Solution()
print(sol.numberOfArithmeticSlices([1, 2, 3, 4, 5]))

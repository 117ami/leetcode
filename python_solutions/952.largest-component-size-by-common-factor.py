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
# @lc app=leetcode id=952 lang=python3
#
# [952] Largest Component Size by Common Factor
#
# https://leetcode.com/problems/largest-component-size-by-common-factor/description/
#
# algorithms
# Hard (30.37%)
# Total Accepted:    18.1K
# Total Submissions: 53.6K
# Testcase Example:  '[4,6,15,35]'
#
# Given a non-empty array of unique positive integers A, consider the following
# graph:
#
#
# There are A.length nodes, labelled A[0] to A[A.length - 1];
# There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a
# common factor greater than 1.
#
#
# Return the size of the largest connected component in the graph.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: [4,6,15,35]
# Output: 4
#
#
#
#
# Example 2:
#
#
# Input: [20,50,9,63]
# Output: 2
#
#
#
#
# Example 3:
#
#
# Input: [2,3,6,7,4,12,21,39]
# Output: 8
#
#
#
# Note:
#
#
# 1 <= A.length <= 20000
# 1 <= A[i] <= 100000
#
#
#
#
#
#
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def merge(self, x, y):
        # Merge by size of set
        px, py = self.find(x), self.find(y)
        if px == py: return
        if self.size[px] < self.size[py]:
            self.p[px] = py
            self.size[py] += self.size[px]
        else:
            self.p[py] = px
            self.size[px] += self.size[py]

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UF(max(A) + 1)
        for n in A:
            for i in range(2, math.ceil(math.sqrt(n)) + 1):
                if n % i == 0:
                    uf.merge(n, i)
                    uf.merge(n, max(n // i, 2))

        return Counter(map(uf.find, A)).most_common()[0][1]


sol = Solution()

ns = [2, 3, 6, 7, 4, 12, 21, 39]
ns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ns = [32, 5, 8, 11, 13, 78, 61, 16, 83, 22, 28, 93]
print(sol.largestComponentSize(ns))

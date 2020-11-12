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


# https://leetcode.com/problems/graph-connectivity-with-threshold/description/
# Hard
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
    def areConnected(self, n: int, threshold: int,
                     queries: List[List[int]]) -> List[bool]:
        uf = UF(n + 1)
        sz = len(queries)

        if threshold > n // 2: return [False] * sz
        if threshold == 0: return [True] * sz

        for i in range(threshold + 1, n + 1):
            j = i
            while j <= n:
                uf.merge(i, j)
                j += i

        return [uf.find(i) == uf.find(j) for i, j in queries]


queries = [[4, 5], [4, 5], [3, 2], [2, 3], [3, 4]]
queries = [[1, 4], [2, 5], [3, 6]]
print(Solution().areConnected(6, 2, queries))

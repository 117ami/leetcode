from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right, insort
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007


# https://leetcode.com/problems/create-sorted-array-through-instructions/description/
# Hard
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ns = []
        cost = 0
        for i, n in enumerate(instructions):
            l = bisect_left(ns, n)
            r = bisect_right(ns, n)
            cost += min(l, i - r)
            ns[l:l] = [n]
            # insort(ns, n)
        # print(ns)
        return cost % MOD


instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]
print(Solution().createSortedArray(instructions))

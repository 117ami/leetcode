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


# https://leetcode.com/problems/parallel-courses/description/
# Hard
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        g = [[] for _ in range(N + 1)]
        memo = [-1] * (N + 1)
        for a, b in relations:
            g[a].append(b)

        def dfs(i):
            if memo[i] > -1:
                return memo[i]
            if memo[i] == -2:
                return 0x3f3f3f3f
            memo[i] = -2
            for j in g[i]:
                memo[i] = max(memo[i], dfs(j) + 1)
            if memo[i] == -2: memo[i] = 0
            return memo[i]

        res = -1
        for i in range(1, N + 1):
            res = max(res, dfs(i))
            if res >= 0x3f3f3f3f: return -1
        return res+1

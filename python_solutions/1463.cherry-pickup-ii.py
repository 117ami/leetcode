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


# https://leetcode.com/problems/cherry-pickup-ii/description/
# Hard
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = defaultdict(lambda: -1)
        R, C = len(grid), len(grid[0])
        dirs = [-1, -1, 0, -1, 1, 0, 0, 1, 1, -1]

        @lru_cache(None)
        def dfs(r, c1, c2):
            if r == R: return 0
            val = dp[(r, c1, c2)]
            if val > -1: return val

            for i in range(9):
                nc1, nc2 = c1 + dirs[i], c2 + dirs[i + 1]
                if 0 <= nc1 <= C - 1 and 0 <= nc2 <= C - 1 and nc1 < nc2:
                    val = max(val, dfs(r + 1, nc1, nc2))
            dp[(r, c1, c2)] = val + grid[r][c1] + grid[r][c2]
            return dp[(r, c1, c2)]

        return dfs(0, 0, C - 1)


gs = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
print(Solution().cherryPickup(gs))

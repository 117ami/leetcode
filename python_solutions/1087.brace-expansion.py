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


# https://leetcode.com/problems/brace-expansion/description/
# Medium
class Solution:
    def expand(self, S: str) -> List[str]:
        expr = S.replace('{', '|').replace('}', '|').split('|')
        res = [""]
        for e in expr:
            res = map(lambda t: ''.join(t),
                      itertools.product(res, e.split(',')))
        return sorted(res)


print(Solution().expand("{a,b}c{d,e}f"))
a, b = [""], ["a", "b"]
print(list(itertools.product(a, b)))

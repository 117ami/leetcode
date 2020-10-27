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


# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/
# Medium
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def merge(self, x, y):
        # Merge by size of set
        px, py = self.find(x), self.find(y)
        if px == py: return
        self.p[px] = self.p[py] = min(px, py)

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        obj = UF(26)
        for i, a in enumerate(A):
            obj.merge(ord(a) - 97, ord(B[i]) - 97)
        return ''.join(chr(97 + obj.find(ord(c) - 97)) for c in S)


A, B, S = "leetcode", "programs", "sourcecode"
print(Solution().smallestEquivalentString(A, B, S))

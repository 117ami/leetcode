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


# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
# Medium
class SparseVector:
    def __init__(self, nums: List[int]):
        self.cc = []
        for i, n in enumerate(nums):
            if n > 0:
                self.cc.append((i, n))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i = j = res = 0
        while i < len(self.cc) and j < len(vec.cc):
            if self.cc[i][0] == vec.cc[j][0]:
                res += self.cc[i][1] * vec.cc[j][1]
                i += 1
                j += 1
            elif self.cc[i][0] < vec.cc[j][0]:
                i += 1
            elif self.cc[i][0] > vec.cc[j][0]:
                j += 1
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

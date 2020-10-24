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

# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/
# Medium
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        hi = 1
        while reader.get(hi) < target:
            hi <<= 1
        lo, mid = hi >> 1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            val = reader.get(mid)
            if val == target: return mid
            elif val == 2147483647 or val > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

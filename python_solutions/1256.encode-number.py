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


# https://leetcode.com/problems/encode-number/description/
# Medium
class Solution:
    def encode(self, num: int) -> str:
        bitlen = 0
        while num >= (1 << bitlen):
            num -= 1 << bitlen
            bitlen += 1
        return "".join(
            map(lambda i: str(num >> i & 1), range(bitlen - 1, -1, -1)))


print(Solution().encode(8))

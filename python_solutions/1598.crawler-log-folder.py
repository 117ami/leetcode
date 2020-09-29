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


# https://leetcode.com/problems/crawler-log-folder/description/
# Easy
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for l in logs:
            if l.startswith('../'): res = max(0, res - 1)
            elif not l.startswith('./'): res += 1
        return res

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


# https://leetcode.com/problems/sentence-screen-fitting/description/
# Medium
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        cc = {}
        res, n = 0, len(sentence)
        for i in range(rows):
            start = res % n
            if start in cc:
                res += cc[start]
            else:
                cnt, j, i = 0, 0, start
                while j + len(sentence[i]) <= cols:
                    j += len(sentence[i]) + 1
                    i = (i + 1) % n
                    cnt += 1
                cc[start] = cnt
                res += cnt
        return res // n


ss = [
    "pwievhoi", "nngx", "bbfnxbtx", "qvfpise", "xjzue", "ascrcacnmo", "bknodn",
    "spvlvcktbw", "rhklcmpd", "lwjxnfhx"
]
r, c = 9593, 3340

ss, r, c = ["I", "had", "apple", "pie"], 4, 5
print(Solution().wordsTyping(ss, r, c))

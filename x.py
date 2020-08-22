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


def get_lhp(t: str) -> List[int]:
    '''Compute the length of LHP for each t[:i], i \in [1..len(t)],
    where a prefix-suffix of t is a substring, u, of t s.t., t.startswith(u) and t.endswith(u).
    And proper means, len(u) < len(t), i.e., u != t
    '''
    j, lhp = 0, [0] * len(t)
    for i in range(1, len(t)):
        while j > 0 and t[i] != t[j]:
            j = lhp[j-1]
            
        if t[i] == t[j]:
            j += 1
            lhp[i] = j
    return lhp

t = 'abcabp'
print(get_lhp(t))

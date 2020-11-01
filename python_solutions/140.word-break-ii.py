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


# https://leetcode.com/problems/word-break-ii/description/
# Hard
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = defaultdict(list)

        def backtracking(s):
            if s in cache: return cache[s]
            for w in wordDict:
                if w == s: cache[s].append(s)
                elif s.startswith(w):
                    for str_tmp in backtracking(s[len(w):]):
                        cache[s].append(w + " " + str_tmp)
            return cache[s]

        return backtracking(s)


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, wordDict))

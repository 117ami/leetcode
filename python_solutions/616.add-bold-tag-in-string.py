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


# https://leetcode.com/problems/add-bold-tag-in-string/description/
# Medium
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False] * len(s)
        for w in words:
            start = s.find(w)
            while start != -1:
                for i in range(start, start + len(w)):
                    bold[i] = True
                start = s.find(w, start + 1)

        res = ""
        i = 0
        while i < len(s):
            if bold[i] == False:
                res += s[i]
                i += 1
            else:
                res += "<b>"
                while i < len(s) and bold[i] == True:
                    res += s[i]
                    i+=1
                res += "</b>"
        return res

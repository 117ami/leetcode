from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#
# https://leetcode.com/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (33.41%)
# Total Accepted:    17.3K
# Total Submissions: 51.6K
# Testcase Example:  '["WordFilter","f"]\n[[["apple"]],["a","e"]]'
#
# Given many words, words[i] has weight i.
#
# Design a class WordFilter that supports one function, WordFilter.f(String
# prefix, String suffix). It will return the word with given prefix and suffix
# with maximum weight. If no word exists, return -1.
#
# Examples:
#
#
# Input:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1
#
#
#
#
# Note:
#
#
# words has length in range [1, 15000].
# For each test case, up to words.length queries WordFilter.f may be made.
# words[i] has length in range [1, 10].
# prefix, suffix have lengths in range [0, 10].
# words[i] and prefix, suffix queries consist of lowercase letters only.
#
#
#
#
#


class WordFilter:

    def __init__(self, words):
        self._prefixes = prefixes = defaultdict(set)
        self._suffixes = suffixes = defaultdict(set)
        m = {word: weight for weight, word in enumerate(words)}
        for word, weight in m.items():
            for i in range(len(word)+1):
                prefixes[word[:i]].add(weight)
                suffixes[word[i:]].add(weight)

    def f(self, prefix: str, suffix: str) -> int: # O(n)
        cands = self._prefixes[prefix] & self._suffixes[suffix]
        return max(cands) if cands else -1


# Your WordFilter object will be instantiated and called as such:
words = ["apple"]
obj = WordFilter(words)
print(obj.f('a', 'e'))

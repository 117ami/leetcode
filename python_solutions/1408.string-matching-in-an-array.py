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
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#
# https://leetcode.com/problems/string-matching-in-an-array/description/
#
# algorithms
# Easy (57.89%)
# Total Accepted:    8.1K
# Total Submissions: 13.9K
# Testcase Example:  '["mass","as","hero","superhero"]'
#
# Given an array of string words. Return all strings in words which is
# substring of another word in any order. 
#
# String words[i] is substring of words[j], if can be obtained removing some
# characters to left and/or right side of words[j].
#
#
# Example 1:
#
#
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of
# "superhero".
# ["hero","as"] is also a valid answer.
#
#
# Example 2:
#
#
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
#
#
# Example 3:
#
#
# Input: words = ["blue","green","bu"]
# Output: []
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# It's guaranteed that words[i] will be unique.
#
#


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        words.sort(key=lambda w: len(w))
        for i, w in enumerate(words):
            for j in range(i + 1, len(words)):
                if w in words[j]:
                    res.add(w)
        return list(res)


sol = Solution()
words = ["mass", "as", "hero", "superhero"]
print(sol.stringMatching(words))

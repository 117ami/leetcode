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
#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (53.44%)
# Total Accepted:    113.5K
# Total Submissions: 212.3K
# Testcase Example:  '"USA"'
#
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# 
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# 
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# 
# 
# Example 1:
# 
# 
# Input: "USA"
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "FlaG"
# Output: False
# 
# 
# 
# 
# Note: The input will be a non-empty word consisting of uppercase and
# lowercase latin letters.
# 
#
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c = [c.isupper() for c in word]
        return all(c) or (c[0] and not any(c[1:])) or not any(c)


word = 'FALSEe'
print(Solution().detectCapitalUse(word))
        

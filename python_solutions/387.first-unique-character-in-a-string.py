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
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (51.91%)
# Total Accepted:    438.8K
# Total Submissions: 843K
# Testcase Example:  '"leetcode"'
#
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#
#


class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        cc = [n] * 26
        res = n 
        for i, c in enumerate(s):
            j = ord(c) - 97
            cc[j] = i if cc[j] == n else 0x3f3f3f3f
        
        res = min(set(cc))
        return res if res < n else -1


sol = Solution()
print(sol.firstUniqChar('loveleetcode'))
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
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
#
# algorithms
# Medium (40.23%)
# Total Accepted:    6.4K
# Total Submissions: 15.6K
# Testcase Example:  '"00110110"\n2'
#
# Given a binary string s and an integer k.
#
# Return True if all binary codes of length k is a substring of s. Otherwise,
# return False.
#
#
# Example 1:
#
#
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They
# can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
#
#
# Example 2:
#
#
# Input: s = "00110", k = 2
# Output: true
#
#
# Example 3:
#
#
# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that
# both exist as a substring.
#
#
# Example 4:
#
#
# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and doesn't exist in the
# array.
#
#
# Example 5:
#
#
# Input: s = "0000000001011100", k = 4
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^5
# s consists of 0's and 1's only.
# 1 <= k <= 20
#
#
#


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        n = len(s)
        cap = 2 ** k
        if n <= cap: return False 

        for i in range(n - k + 1):
            codes.add(s[i:i+k])
            if len(codes) == cap: return True 
        # print(ns)
        return False


sol = Solution()
s, k = "0000000001011100", 4
# s,k = "00110110", 2
# s,k="00110",2
print(sol.hasAllCodes(s, k))

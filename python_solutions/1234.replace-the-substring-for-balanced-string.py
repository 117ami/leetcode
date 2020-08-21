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
# @lc app=leetcode id=1234 lang=python3
#
# [1234] Replace the Substring for Balanced String
#
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/description/
#
# algorithms
# Medium (33.29%)
# Total Accepted:    11.4K
# Total Submissions: 34.1K
# Testcase Example:  '"QWER"'
#
# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E'
# and 'R'.
#
# A string is said to be balanced if each of its characters appears n/4 times
# where n is the length of the string.
#
# Return the minimum length of the substring that can be replaced with any
# other string of the same length to make the original string s balanced.
#
# Return 0 if the string is already balanced.
#
#
# Example 1:
#
#
# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced.
#
# Example 2:
#
#
# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is
# balanced.
#
#
# Example 3:
#
#
# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER".
#
#
# Example 4:
#
#
# Input: s = "QQQQ"
# Output: 3
# Explanation: We can replace the last 3 'Q' to make s = "QWER".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s.length is a multiple of 4
# s contains only 'Q', 'W', 'E' and 'R'.
#
#
#
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        avg = n // 4
        cc = Counter(s)
        print(cc)
        cnt, i = n, 0
        print(cnt, i)
        for j, c in enumerate(s):
            cc[c] -= 1
            while i < n and all(cc[_c] <= avg for _c in cc):
                cnt = min(cnt, j - i + 1)
                print(i, j, cc)
                cc[s[i]] += 1
                i += 1

        return cnt


sol = Solution()

s = "QWER"
s = "WWWEQRQEWWQQQWQQQWEWEEWRRRRRWWQE"
s = "QEQRWRRWWWRQQQWQQEQEQREWRQEQRQQRRQEW"
# s = "WWEQERQWQWWRWWERQWEQ"

print(sol.balancedString(s))

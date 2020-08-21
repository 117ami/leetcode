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
# @lc app=leetcode id=1542 lang=python3
#
# [1542] Find Longest Awesome Substring
#
# https://leetcode.com/problems/find-longest-awesome-substring/description/
#
# algorithms
# Hard (26.70%)
# Total Accepted:    1.9K
# Total Submissions: 6.4K
# Testcase Example:  '"3242415"'
#
# Given a string s. An awesome substring is a non-empty substring of s such
# that we can make any number of swaps in order to make it palindrome.
#
# Return the length of the maximum length awesome substring of s.
#
#
# Example 1:
#
#
# Input: s = "3242415"
# Output: 5
# Explanation: "24241" is the longest awesome substring, we can form the
# palindrome "24142" with some swaps.
#
#
# Example 2:
#
#
# Input: s = "12345678"
# Output: 1
#
#
# Example 3:
#
#
# Input: s = "213123"
# Output: 6
# Explanation: "213123" is the longest awesome substring, we can form the
# palindrome "231132" with some swaps.
#
#
# Example 4:
#
#
# Input: s = "00"
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists only of digits.
#
#
#


class Solution:
    def longestAwesome(self, s: str) -> int:
        '''Use bitmask.
        '''
        res, mask = 1, 0
        cc = [len(s)] * 1024
        cc[0] = -1
        for i, c in enumerate(s):
            mask ^= 1 << int(c)
            res = max(res, i - cc[mask])
            for j in range(10):
                res = max(res, i - cc[mask ^ (1 << j)])
            cc[mask] = min(cc[mask], i)

        return res


sol = Solution()


s = "3242415"
s = "12345678"
# s = "213123"
# s = "00"
# s = '51224'
print(sol.longestAwesome(s))

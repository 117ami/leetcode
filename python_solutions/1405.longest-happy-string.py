from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
import heapq
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#
# https://leetcode.com/problems/longest-happy-string/description/
#
# algorithms
# Medium (44.56%)
# Total Accepted:    6K
# Total Submissions: 13.4K
# Testcase Example:  '1\n1\n7'
#
# A string is called happy if it does not have any of the strings 'aaa', 'bbb'
# or 'ccc' as a substring.
#
# Given three integers a, b and c, return any string s, which satisfies
# following conditions:
#
#
# s is happy and longest possible.
# s contains at most a occurrences of the letter 'a', at most b occurrences of
# the letter 'b' and at most c occurrences of the letter 'c'.
# s will only contain 'a', 'b' and 'c' letters.
#
#
# If there is no such string s return the empty string "".
#
#
# Example 1:
#
#
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
#
#
# Example 2:
#
#
# Input: a = 2, b = 2, c = 1
# Output: "aabbc"
#
#
# Example 3:
#
#
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It's the only correct answer in this case.
#
#
#
# Constraints:
#
#
# 0 <= a, b, c <= 100
# a + b + c > 0
#
#
#


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(d)
        res, i = [], 0
        while True:
            top = heapq.heappop(d)
            # print(top, d)
            if top[0] == 0:
                break
            if i < 2 or not(res[i - 1] == top[1] and res[i - 2] == top[1]):
                top = (top[0] + 1, top[1])
                i += 1
                res.append(top[1])
            else:
                s_top = heapq.heappop(d)
                if s_top[0] < 0:
                    s_top = (s_top[0] + 1, s_top[1])
                    i += 1
                    res.append(s_top[1])
                    heapq.heappush(d, s_top)
                else:
                    break
            heapq.heappush(d, top)

        return ''.join(res)



sol = Solution()
print(sol.longestDiverseString(0, 9, 12))

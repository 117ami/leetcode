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
# @lc app=leetcode id=1593 lang=python3
#
# [1593] Split a String Into the Max Number of Unique Substrings
#
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/
#
# algorithms
# Medium (38.03%)
# Total Accepted:    5.2K
# Total Submissions: 12.5K
# Testcase Example:  '"ababccc"'
#
# Given a string s, return the maximum number of unique substrings that the
# given string can be split into.
#
# You can split string s into any list of non-empty substrings, where the
# concatenation of the substrings forms the original string. However, you must
# split the substrings such that all of them are unique.
#
# A substring is a contiguous sequence of characters within a string.
#
#
# Example 1:
#
#
# Input: s = "ababccc"
# Output: 5
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc'].
# Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a'
# and 'b' multiple times.
#
#
# Example 2:
#
#
# Input: s = "aba"
# Output: 2
# Explanation: One way to split maximally is ['a', 'ba'].
#
#
# Example 3:
#
#
# Input: s = "aa"
# Output: 1
# Explanation: It is impossible to split the string any further.
#
#
#
# Constraints:
#
#
#
# 1 <= s.length <= 16
#
#
# s contains only lower case English letters.
#
#
#
#
# class Solution:
#     def maxUniqueSplit(self, s: str) -> int:
#         def bt(i):
#             if i >= len(s): return 0
#             res = 0
#             for j in range(i + 1, len(s) + 1):
#                 ss = s[i:j]
#                 if ss not in cc:
#                     cc.add(ss)
#                     res = max(res, 1 + bt(j))
#                     cc.remove(ss)
#             return res

#         cc = set()
#         return bt(0)


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(index=0, visited=set()):
            nonlocal ans
            if s[index:n] and s[index:n] not in visited:
                ans = max(ans, len(visited) + 1)
            for i in range(index, n):
                if s[index:i] and s[index:i] not in visited and len(
                        visited) + 1 + n - i > ans:
                    nv = visited.copy()
                    nv.add(s[index:i])
                    dfs(i, nv)

        n, ans = len(s), 0
        dfs()
        return ans


sol = Solution()

s = "ababccc"
# s = "aba"
# s = "aa"
print(sol.maxUniqueSplit(s))

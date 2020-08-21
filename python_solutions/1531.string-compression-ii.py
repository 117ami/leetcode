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
# @lc app=leetcode id=1531 lang=python3
#
# [1531] String Compression II
#
# https://leetcode.com/problems/string-compression-ii/description/
#
# algorithms
# Hard (28.75%)
# Total Accepted:    3K
# Total Submissions: 10.4K
# Testcase Example:  '"aaabcccd"\n2'
#
# Run-length encoding is a string compression method that works by replacing
# consecutive identical characters (repeated 2 or more times) with the
# concatenation of the character and the number marking the count of the
# characters (length of the run). For example, to compress the string "aabccc"
# we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string
# becomes "a2bc3".
#
# Notice that in this problem, we are not adding '1' after single characters.
#
# Given a string s and an integer k. You need to delete at most k characters
# from s such that the run-length encoded version of s has minimum length.
#
# Find the minimum length of the run-length encoded version of s after deleting
# at most k characters.
#
#
# Example 1:
#
#
# Input: s = "aaabcccd", k = 2
# Output: 4
# Explanation: Compressing s without deleting anything will give us "a3bc3d" of
# length 6. Deleting any of the characters 'a' or 'c' would at most decrease
# the length of the compressed string to 5, for instance delete 2 'a' then we
# will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way
# is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of
# length 4.
#
# Example 2:
#
#
# Input: s = "aabbaa", k = 2
# Output: 2
# Explanation: If we delete both 'b' characters, the resulting compressed
# string would be "a4" of length 2.
#
#
# Example 3:
#
#
# Input: s = "aaaaaaaaaaa", k = 0
# Output: 3
# Explanation: Since k is zero, we cannot delete anything. The compressed
# string is "a11" of length 3.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# 0 <= k <= s.length
# s contains only lowercase English letters.
#
#
#


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def _len(cnt): return 1 if cnt == 1 else 1 + len(str(cnt))

        @lru_cache(None)
        def solve(left, k):
            if k < 0:
                return float('inf')
            # remove s[0:left+1]
            if left + 1 <= k:
                return 0
            # 1. keep s[left]
            # 2. remove s[left]
            res = min(solve(left - 1, k) + 1, solve(left - 1, k - 1))
            cnt = 1
            for j in range(left - 1, -1, -1):
                if s[j] != s[left]:
                    k -= 1
                    if k < 0:
                        break
                else:
                    cnt += 1
                    res = min(res, solve(j - 1, k) + _len(cnt))
            return res
        return solve(len(s) - 1, k)


sol = Solution()


s, k = "aaabcccd", 2
s, k = "aabbaa", 2
s, k = "aaaaaaaaaaa", 0
print(sol.getLengthOfOptimalCompression(s, k))

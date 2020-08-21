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
# @lc app=leetcode id=927 lang=python3
#
# [927] Three Equal Parts
#
# https://leetcode.com/problems/three-equal-parts/description/
#
# algorithms
# Hard (33.58%)
# Total Accepted:    7.3K
# Total Submissions: 21.8K
# Testcase Example:  '[1,0,1,0,1]'
#
# Given an array A of 0s and 1s, divide the array into 3 non-empty parts such
# that all of these parts represent the same binary value.
#
# If it is possible, return any [i, j] with i+1 < j, such that:
#
#
# A[0], A[1], ..., A[i] is the first part;
# A[i+1], A[i+2], ..., A[j-1] is the second part, and
# A[j], A[j+1], ..., A[A.length - 1] is the third part.
# All three parts have equal binary value.
#
#
# If it is not possible, return [-1, -1].
#
# Note that the entire part is used when considering what binary value it
# represents.  For example, [1,1,0] represents 6 in decimal, not 3.  Also,
# leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
#
#
#
# Example 1:
#
#
# Input: [1,0,1,0,1]
# Output: [0,3]
#
#
#
# Example 2:
#
#
# Input: [1,1,0,1,1]
# Output: [-1,-1]
#
#
#
#
# Note:
#
#
# 3 <= A.length <= 30000
# A[i] == 0 or A[i] == 1
#
#
#
#
#
#
class KMP():
    def get_lhp(self, t: str) -> List[int]:
        '''Compute the length of LHP for each t[:i], i \in [1..len(t)],
        where a prefix-suffix of t is a substring, u, of t s.t., t.startswith(u) and t.endswith(u).
        And proper means, len(u) < len(t), i.e., u != t
        '''
        j, lhp = 0, [0] * len(t)
        for i in range(1, len(t)):
            while j > 0 and t[i] != t[j]:
                j = lhp[j - 1]

            if t[i] == t[j]:
                j += 1
                lhp[i] = j
        return lhp

    def pattern_search(self, text: str, pat: str) -> List[int]:
        """KMP (Knuth Morris Pratt) Pattern Searching
        Return a list of indexes i, such that t occurs in s starting from i.
        """
        j = 0
        lhp, res = self.get_lhp(pat), []
        for i in range(len(text)):
            while j > 0 and text[i] != pat[j]:
                j = lhp[j - 1]

            if text[i] == pat[j]:
                j += 1

            if j == len(pat):
                res.append(i + 1 - len(pat))
                j = lhp[j - 1]
        return res


class Solution:
    def threeEqualParts(self, a: List[int]) -> List[int]:
        n, s = len(a), sum(a)
        if s % 3:
            return [-1, -1]
        if not s: return [0, n - 1]

        i, cnt = len(a) - 1, 0
        while cnt < s // 3:
            if a[i] == 1: cnt += 1
            i -= 1

        pat = ''.join(map(str, a[i + 1:]))
        s = ''.join(map(str, a))
        res = KMP().pattern_search(s, pat)

        if len(res) < 3: return [-1, -1]
        second_idx = bisect_left(res, res[0] + len(pat))

        # print(res, second_idx)
        return a + len(pat) - 1, res[second_idx] + len(pat)


sol = Solution()

a = [1, 0, 1, 0, 1]
# a =   [1,1,0,1,1]
# a = "000000000010010011000000010010011000000000010010011"
# a=[0,0,0,0,0]
a = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
a = [1, 1, 0, 0, 1]
aa = list(map(int, list(a)))
print(sol.threeEqualParts(aa))

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
# @lc app=leetcode id=1520 lang=python3
#
# [1520] Maximum Number of Non-Overlapping Substrings
#
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description/
#
# algorithms
# Hard (31.89%)
# Total Accepted:    4.3K
# Total Submissions: 13K
# Testcase Example:  '"adefaddaccc"'
#
# Given a string s of lowercase letters, you need to find the maximum number of
# non-empty substrings of s that meet the following conditions:
#
#
# The substrings do not overlap, that is for any two substrings s[i..j] and
# s[k..l], either j < k or i > l is true.
# A substring that contains a certain character c must also contain all
# occurrences of c.
#
#
# Find the maximum number of substrings that meet the above conditions. If
# there are multiple solutions with the same number of substrings, return the
# one with minimum total length. It can be shown that there exists a unique
# solution of minimum total length.
#
# Notice that you can return the substrings in any order.
#
#
# Example 1:
#
#
# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the
# conditions:
# [
# "adefaddaccc"
# "adefadda",
# "ef",
# "e",
# ⁠ "f",
# "ccc",
# ]
# If we choose the first string, we cannot choose anything else and we'd get
# only 1. If we choose "adefadda", we are left with "ccc" which is the only one
# that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not
# optimal to choose "ef" since it can be split into two. Therefore, the optimal
# way is to choose ["e","f","ccc"] which gives us 3 substrings. No other
# solution of the same number of substrings exist.
#
#
# Example 2:
#
#
# Input: s = "abbaccd"
# Output: ["d","bb","cc"]
# Explanation: Notice that while the set of substrings ["d","abba","cc"] also
# has length 3, it's considered incorrect since it has larger total length.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
#
#
#


class Solution:
    def _search_new_right(self, s, i, l, r):
        new_right = r[s[i]]
        j = i
        while j <= new_right:
            if l[s[j]] < i:
                return -1
            new_right = max(new_right, r[s[j]])
            j += 1
        return new_right

    def maxNumOfSubstrings(self, s: str) -> List[str]:
        l, r = defaultdict(lambda: float('inf')), defaultdict(int)
        for i, c in enumerate(s):
            l[c] = min(l[c], i)
            r[c] = i
        res = []
        right = -1

        for i, c in enumerate(s):
            if i == l[c]:
                new_right = self._search_new_right(s, i, l, r)
                if new_right > -1:
                    if i > right:
                        res.append("")
                    right = new_right
                    res[-1] = s[i:right + 1]
            # print(i, res)
        return res


sol = Solution()


s = "adefaddaccc"
# s = "abbaccd"
# s = "cbaabaabc"
s = 'abcdkcdef'
s = "bbcacbaba"
print(sol.maxNumOfSubstrings(s))

from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (73.56%)
# Total Accepted:    90K
# Total Submissions: 122.4K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
#
# A string S of lowercase letters is given.  We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.
#
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
#
#
#
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
#
#


class Solution:
    def partitionLabels(self, S: str):
        counts = Counter(S)
        res = []
        records = {}
        preidx = -1
        for i, c in enumerate(S):
            records[c] = records[c] - 1 if c in records else counts[c] - 1

            if records[c] == 0:
                del records[c]

            if len(records) == 0:
                res.append(i - preidx)
                preidx = i
        return res


sol = Solution()
S = "ababcbacadefegdehijhklij"
print(sol.partitionLabels(S))

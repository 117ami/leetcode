from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=982 lang=python3
#
# [982] Triples with Bitwise AND Equal To Zero
#
# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/description/
#
# algorithms
# Hard (55.15%)
# Total Accepted:    6.2K
# Total Submissions: 11.3K
# Testcase Example:  '[2,1,3]'
#
# Given an array of integers A, find the number of triples of indices (i, j, k)
# such that:
#
#
# 0 <= i < A.length
# 0 <= j < A.length
# 0 <= k < A.length
# A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.
#
#
#
#
# Example 1:
#
#
# Input: [2,1,3]
# Output: 12
# Explanation: We could choose the following i, j, k triples:
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 1000
# 0 <= A[i] < 2^16
#
#
#


class Solution:
    def countTriplets(self, arr):
        cc = defaultdict(int)
        cc = [0] * (1<<16)
        s = set()
        for a in arr:
            for b in arr:
                cc[a & b] += 1
                s.add(a&b)

        res = 0
        for a in arr:
            for k in s:
                if a & k == 0:
                    res += cc[k]
        return res


sol = Solution()
arr = [2, 1, 3]
print(sol.countTriplets(arr))

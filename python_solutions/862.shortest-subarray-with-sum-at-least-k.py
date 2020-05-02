from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (23.65%)
# Total Accepted:    26.2K
# Total Submissions: 110.5K
# Testcase Example:  '[1]\n1'
#
# Return the length of the shortest, non-empty, contiguous subarray of A with
# sum at least K.
#
# If there is no non-empty subarray with sum at least K, return -1.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: A = [1], K = 1
# Output: 1
#
#
#
# Example 2:
#
#
# Input: A = [1,2], K = 4
# Output: -1
#
#
#
# Example 3:
#
#
# Input: A = [2,-1,2], K = 3
# Output: 3
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9
#
#
#
#
#
#


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        deq = deque()
        res = 0x3f3f3f3f
        _len = len(A)
        b = [0] + list(itertools.accumulate(A, lambda x, y: x+y))
        
        for i in range(_len + 1):
            while deq and b[i] - b[deq[0]] >= K:
                res = min(res, i - deq.popleft())
            while deq and b[i] <= b[deq[-1]]:
                deq.pop()
            deq.append(i)
        return res if res <= _len else -1


sol = Solution()
A, K = [2,-1,2], 3
print(sol.shortestSubarray(A,K))
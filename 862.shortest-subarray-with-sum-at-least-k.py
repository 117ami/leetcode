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
    def shortestSubarray(self, ns: List[int], k: int) -> int:
        n = len(ns)
        ctmp = [0] * (n + 1)
        min_negative = min(ns)
        for i in range(n):
            ctmp[i + 1] = ns[i] + ctmp[i] - min_negative

        def is_valid(len_i32):
            for i in range(len_i32, n + 1):
                # print('...', ctmp[i], ctmp[i - mid], ctmp[i] - ctmp[i - mid])
                if ctmp[i] - ctmp[i - len_i32] >= k - len_i32 * min_negative:
                    return True 
            return False 


        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            print(lo, hi, mid)
            if is_valid(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo if lo < n or ctmp[-1] >= k else -1


sol = Solution()
ns, k = [2, -1, 2], 3
# ns, k = [84, -37, 32, 40, 95], 167
# ns, k = [1,2], 4
ns, k =[-28,81,-20,28,-29], 89
print(sol.shortestSubarray(ns, k))

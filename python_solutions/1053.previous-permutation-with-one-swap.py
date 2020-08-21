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
# @lc app=leetcode id=1053 lang=python3
#
# [1053] Previous Permutation With One Swap
#
# https://leetcode.com/problems/previous-permutation-with-one-swap/description/
#
# algorithms
# Medium (48.47%)
# Total Accepted:    13.2K
# Total Submissions: 27.3K
# Testcase Example:  '[3,2,1]'
#
# Given an array A of positive integers (not necessarily distinct), return the
# lexicographically largest permutation that is smaller than A, that can be
# made with one swap (A swap exchanges the positions of two numbers A[i] and
# A[j]).  If it cannot be done, then return the same array.
#
#
#
# Example 1:
#
#
# Input: [3,2,1]
# Output: [3,1,2]
# Explanation: Swapping 2 and 1.
#
#
# Example 2:
#
#
# Input: [1,1,5]
# Output: [1,1,5]
# Explanation: This is already the smallest permutation.
#
#
# Example 3:
#
#
# Input: [1,9,4,6,7]
# Output: [1,7,4,6,9]
# Explanation: Swapping 9 and 7.
#
#
# Example 4:
#
#
# Input: [3,1,1,3]
# Output: [1,3,1,3]
# Explanation: Swapping 1 and 3.
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 10000
# 1 <= A[i] <= 10000
#
#
#
class Solution:
    def prevPermOpt1(self, ns: List[int]) -> List[int]:
        if len(ns) <= 1: return ns
        idx = next(
            filter(lambda i: ns[i] < ns[i - 1], range(len(ns) - 1, 0, -1)),
            0) - 1

        # ns is sorted, no smaller permutation
        if idx == -1: return ns
        print(ns, idx)
        for j in range(len(ns) - 1, idx, -1):
            # Find the largest j such that ns[j] < ns[idx], then swap them.
            # The second check to skip duplicate numbers
            print(j)
            if ns[j] < ns[idx] and ns[j] != ns[j - 1]:
                ns[j], ns[idx] = ns[idx], ns[j]
                break 
        return ns


sol = Solution()

inputs = [3, 2, 1]
inputs = [1, 1, 5]
# inputs = [1, 9, 4, 6, 7]
inputs = [3, 1, 1, 3]
print(sol.prevPermOpt1(inputs))

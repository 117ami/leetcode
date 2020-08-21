from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right, insort_left
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
# @lc app=leetcode id=975 lang=python3
#
# [975] larger smaller Jump
#
# https://leetcode.com/problems/larger-smaller-jump/description/
#
# algorithms
# Hard (42.15%)
# Total Accepted:    30.9K
# Total Submissions: 73.4K
# Testcase Example:  '[10,13,12,14,15]'
#
# You are given an integer array A.  From some starting index, you can make a
# series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called larger
# numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called
# smaller numbered jumps.
#
# You may from index i jump forward to index j (with i < j) in the following
# way:
#
#
# During larger numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j
# such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are
# multiple such indexes j, you can only jump to the smallest such index j.
# During smaller numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j
# such that A[i] >= A[j] and A[j] is the largest possible value.  If there are
# multiple such indexes j, you can only jump to the smallest such index j.
# (It may be the case that for some index i, there are no legal jumps.)
#
#
# A starting index is good if, starting from that index, you can reach the end
# of the array (index A.length - 1) by jumping some number of times (possibly 0
# or more than once.)
#
# Return the number of good starting indexes.
#
#
#
# Example 1:
#
#
# Input: [10,13,12,14,15]
# Output: 2
# Explanation:
# From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest
# among A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can't
# jump any more.
# From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump
# any more.
# From starting index i = 3, we can jump to i = 4, so we've reached the end.
# From starting index i = 4, we've reached the end already.
# In total, there are 2 different starting indexes (i = 3, i = 4) where we can
# reach the end with some number of jumps.
#
#
#
# Example 2:
#
#
# Input: [2,3,1,1,4]
# Output: 3
# Explanation:
# From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
#
# During our 1st jump (larger numbered), we first jump to i = 1 because A[1] is
# the smallest value in (A[1], A[2], A[3], A[4]) that is greater than or equal
# to A[0].
#
# During our 2nd jump (smaller numbered), we jump from i = 1 to i = 2 because A[2]
# is the largest value in (A[2], A[3], A[4]) that is less than or equal to
# A[1].  A[3] is also the largest value, but 2 is a smaller index, so we can
# only jump to i = 2 and not i = 3.
#
# During our 3rd jump (larger numbered), we jump from i = 2 to i = 3 because A[3]
# is the smallest value in (A[3], A[4]) that is greater than or equal to A[2].
#
# We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
#
# In a similar manner, we can deduce that:
# From starting index i = 1, we jump to i = 4, so we reach the end.
# From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
# From starting index i = 3, we jump to i = 4, so we reach the end.
# From starting index i = 4, we are already at the end.
# In total, there are 3 different starting indexes (i = 1, i = 3, i = 4) where
# we can reach the end with some number of jumps.
#
#
#
# Example 3:
#
#
# Input: [5,1,3,4,2]
# Output: 3
# Explanation:
# We can reach the end from starting indexes 1, 2, and 4.
#
#
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 20000
# 0 <= A[i] < 100000
#
#
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        larger = [0] * (N - 1) + [1]
        smaller = larger.copy()

        next_larger, next_smaller, stack = [0] * N, [0] * N, []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_larger[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_smaller[stack.pop()] = i
            stack.append(i)

        print(next_smaller, next_larger)
        for i in range(N - 2, -1, -1):
            # The order of computing larger and smaller matters 
            larger[i] = smaller[next_larger[i]]
            smaller[i] = larger[next_smaller[i]]

        print(larger, smaller)
        return sum(larger)


sol = Solution()
inputs = [10, 13, 12, 14, 15]
# inputs = [2, 3, 1, 1, 4]
# inputs = [5, 1, 3, 4, 2]
# inputs = [1, 2, 3, 2, 1, 4, 4, 5]
inputs = [50, 28]
print(sol.oddEvenJumps(inputs))

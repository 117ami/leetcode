from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
true = True
false = False
#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
#
# algorithms
# Medium (33.69%)
# Total Accepted:    15.5K
# Total Submissions: 46K
# Testcase Example:  '[1,-2,3,-2]'
#
# Given a circular array C of integers represented by A, find the maximum
# possible sum of a non-empty subarray of C.
#
# Here, a circular array means the end of the array connects to the beginning
# of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and
# C[i+A.length] = C[i] when i >= 0.)
#
# Also, a subarray may only include each element of the fixed buffer A at most
# once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not
# exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
#
#
#
#
# Example 1:
#
#
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
#
#
#
# Example 2:
#
#
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
#
#
#
# Example 3:
#
#
# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
#
#
#
# Example 4:
#
#
# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
#
#
# Example 5:
#
#
# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
#
#
#
#
# Note:
#
#
# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000
#
#
#
#
#
#
INF = 0x3f3f3f3f


class Solution:
    def maxSubarraySumCircular(self, a):
        maxsum = -INF
        curmax = curmin = 0
        minsum = INF
        total = 0
        for n in a:
            curmax = max(curmax + n, n)
            maxsum = max(curmax, maxsum)

            curmin = min(curmin + n, n)
            minsum = min(curmin, minsum)

            total += n

        # Conner case: return max(A) when all numbers are negative
        # Return the sum of an empty subarray is against the requirements of
        # this problem
        return max(total - minsum, maxsum) if maxsum > 0 else maxsum


sol = Solution()
a = [1, -2, 3, -2]
a = [5, -3, 5]
# a = [3, -1, 2, -1]
# a = [3, -2, 2, -3]
# a = [-2, -3, -1]
print(sol.maxSubarraySumCircular(a))

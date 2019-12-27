from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
true = True
false = False
#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (47.27%)
# Total Accepted:    22K
# Total Submissions: 46.5K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an array A of integers, return the number of (contiguous, non-empty)
# subarrays that have a sum divisible by K.
#
#
#
#
# Example 1:
#
#
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
#
#
#


class Solution:
    def subarraysDivByK(self, a, k):
        sums = defaultdict(int)
        sums[0] = 1
        res = curr = 0
        for n in a:
            curr = (curr + n) % k
            res += sums[curr]
            sums[curr] += 1
        return res


s = Solution()
a, k = [4, 5, 0, -2, -3, 1], 5
print(s.subarraysDivByK(a, k))

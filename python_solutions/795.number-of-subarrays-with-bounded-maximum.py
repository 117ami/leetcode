from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
from functools import reduce 
true = True
false = False
#
# @lc app=leetcode id=795 lang=python3
#
# [795] Number of Subarrays with Bounded Maximum
#
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (44.70%)
# Total Accepted:    14.6K
# Total Submissions: 32.7K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# We are given an array A of positive integers, and two positive integers L and
# R (L <= R).
# 
# Return the number of (contiguous, non-empty) subarrays such that the value of
# the maximum array element in that subarray is at least L and at most R.
# 
# 
# Example :
# Input: 
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2,
# 1], [3].
# 
# 
# Note:
# 
# 
# L, R  and A[i] will be an integer in the range [0, 10^9].
# The length of A will be in the range of [1, 50000].
# 
# 
#
class Solution:
    def numSubarrayBoundedMax(self, a, l, r):
        left = res = 0
        pre = -1
        for i, n in enumerate(a):
            if n > r:
                left = i + 1
            if n >= l:
                pre = i 
            res += pre - left + 1
            # print(i, n, res)
        return res 
                    
s = Solution()
a, l, r = [2, 1, 4, 3], 2, 3
a = [1,2,1,2]
a, l, r = [73,55,36,5,55,14,9,7,72,52], 32, 69
a, l, r = [16,69,88,85,79,87,37,33,39,34], 55, 57
print(s.numSubarrayBoundedMax(a, l, r))


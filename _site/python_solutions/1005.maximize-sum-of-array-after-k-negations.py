#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
#
# algorithms
# Easy (48.98%)
# Total Accepted:    7K
# Total Submissions: 14.3K
# Testcase Example:  '[4,2,3]\n1'
#
# Given an array A of integers, we must modify the array in the following way:
# we choose an i and replace A[i] with -A[i], and we repeat this process K
# times in total.  (We may choose the same index i multiple times.)
# 
# Return the largest possible sum of the array after modifying it in this
# way.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [3,-1,0,2], K = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100
# 
# 
#
class Solution:
    def largestSumAfterKNegations(self, a, k):
        a.sort()
        i = 0
        while i < len(a) and a[i] <= 0:
            a[i] *= -1
            i += 1
            k -= 1
            if k == 0: return sum(a)
        minv = abs(a[0]) if i == 0 or len(a) == 1 else min(abs(a[i]), abs(a[i-1]))
        return sum(a) - (minv * 2 if k & 1 else 0)
        
# a = [2,-3,-1,5,-4]
# k = 4
# print(Solution().largestSumAfterKNegations(a, k))


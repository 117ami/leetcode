#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#
# https://leetcode.com/problems/longest-turbulent-subarray/description/
#
# algorithms
# Medium (46.06%)
# Total Accepted:    17.6K
# Total Submissions: 38.3K
# Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
#
# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only
# if:
# 
# 
# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is
# even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is
# odd.
# 
# 
# That is, the subarray is turbulent if the comparison sign flips between each
# adjacent pair of elements in the subarray.
# 
# Return the length of a maximum size turbulent subarray of A.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# 
# 
# 
# Example 2:
# 
# 
# Input: [4,8,12,16]
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: [100]
# Output: 1
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9
# 
#
class Solution:
    def maxTurbulenceSize(self, a):
        cter = res = 0
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                cter = cter + 1 if cter > 0 else 1
            elif a[i] < a[i+1]:
                cter = cter - 1 if cter < 0 else -1 
            else:
                cter = 0
            res = max(res, abs(cter))
            cter *= -1
        return res + 1
        
s = Solution()
a = [9,4,2,10,7,8,8,1,9]
a = [1]
print(s.maxTurbulenceSize(a))





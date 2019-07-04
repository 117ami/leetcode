#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Partition Array Into Three Parts With Equal Sum
#
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (51.36%)
# Total Accepted:    4.7K
# Total Submissions: 9K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# Given an array A of integers, return true if and only if we can partition the
# array into three non-empty parts with equal sums.
# 
# Formally, we can partition the array if we can find indexes i+1 < j with
# (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1]
# + ... + A[A.length - 1])
# 
# 
# 
# Example 1:
# 
# 
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 
# 
# 
# Example 2:
# 
# 
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000
# 
# 
#
class Solution:
	def canThreePartsEqualSum(self, a):
		xsum = sum(a)    	
		if xsum % 3 != 0: return False
		n = xsum // 3
		xsum = cter = 0
		for e in a:
			xsum += e
			if xsum == n :
				xsum = 0 
				cter += 1
		return xsum == 0 and cter == 3


a = [0,2,1,-6,6,-7,9,1,2,0,1]
a = [3,3,6,5,-2,2,5,1,-9,4]
a = [0,2,1,-6,6,7,9,-1,2,0,1]
print(Solution().canThreePartsEqualSum(a))

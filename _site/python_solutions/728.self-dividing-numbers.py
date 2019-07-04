#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#
# https://leetcode.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (68.15%)
# Total Accepted:    62.4K
# Total Submissions: 91.4K
# Testcase Example:  '1\n22'
#
# 
# A self-dividing number is a number that is divisible by every digit it
# contains.
# 
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 ==
# 0, and 128 % 8 == 0.
# 
# Also, a self-dividing number is not allowed to contain the digit zero.
# 
# Given a lower and upper number bound, output a list of every possible self
# dividing number, including the bounds if possible.
# 
# Example 1:
# 
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# 
# 
# 
# Note:
# The boundaries of each input argument are 1 .
# 
#
class Solution:
	def selfDividingNumbers(self, left, right):
		"""
		:type left: int
		:type right: int
		:rtype: List[int]
		"""
		res = []
		for i in range(left, right+1):
			if self.helper(i):
				res.append(i)
		return res

	def helper(self, n):
		if n == 0 or '0' in str(n): return False 
		return all(n % int(i) == 0 for i in str(n))



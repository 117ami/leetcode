#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (32.77%)
# Total Accepted:    32.9K
# Total Submissions: 100K
# Testcase Example:  '28'
#
# We define the Perfect Number is a positive integer that is equal to the sum
# of all its positive divisors except itself. 
# 
# Now, given an integer n, write a function that returns true when it is a
# perfect number and false when it is not.
# 
# 
# Example:
# 
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 
# 
# 
# Note:
# The input number n will not exceed 100,000,000. (1e8)
# 
#
class Solution:
	def checkPerfectNumber(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num <= 1: return False 
		res = 1
		for i in range(2, math.ceil(num ** 0.5)):
			if num % i == 0:
				res += i
				res += int(num / i)
		return res == num

		


num = 10923993
Solution().checkPerfectNumber(num)
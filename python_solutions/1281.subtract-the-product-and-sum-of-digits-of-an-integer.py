#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
#
# algorithms
# Easy (83.96%)
# Total Accepted:    12.2K
# Total Submissions: 14.5K
# Testcase Example:  '234'
#
# Given an integer number n, return the difference between the product of its
# digits and the sum of its digits.
# 
# Example 1:
# 
# 
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# 
# 
# Example 2:
# 
# 
# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# 
# 
#
import functools
class Solution:
    def subtractProductAndSum(self, n):
        digits = list(map(int, list(str(n))))
        return functools.reduce(lambda x, y: x * y, digits) - sum(digits)
        
s = Solution()
print(s.subtractProductAndSum(4421))



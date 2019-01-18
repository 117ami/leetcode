#
# @lc app=leetcode id=7 lang=ruby
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.87%)
# Total Accepted:    572.7K
# Total Submissions: 2.3M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
#
#
# @param {Integer} x
# @return {Integer}
def reverse(x)
  sign = x > 0 ? 1 : -1
  ans = x.abs.to_s.reverse.to_i
  ans < 2**31 ? ans * sign : 0
end

# x = 108834
# p reverse(x)

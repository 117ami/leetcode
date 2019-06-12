#
# @lc app=leetcode id=263 lang=ruby
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (40.63%)
# Total Accepted:    158.2K
# Total Submissions: 389.2K
# Testcase Example:  '6'
#
# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example 1:
#
#
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
#
# Example 2:
#
#
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
#
#
# Example 3:
#
#
# Input: 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.
#
#
# Note:
#
#
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−231,  231 − 1].
#
#
# @param {Integer} num
# @return {Boolean}
require 'prime'
def is_ugly(num)
  return false if num <= 0
  return true if num <= 3
  num /= 2 while num.even?
  num /= 3 while num % 3 == 0
  num /= 5 while num % 5 == 0
  num == 1
end

num = 14
p is_ugly(num)

#
# @lc app=leetcode id=172 lang=ruby
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.09%)
# Total Accepted:    142.5K
# Total Submissions: 383.5K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
#
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
# Example 2:
#
#
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
# Note: Your solution should be in logarithmic time complexity.
#
#
# @param {Integer} n
# @return {Integer}
def trailing_zeroes(n)
  return 0 if n <= 4

  i = 0
  i += 1 while 5**i < n
  (1..i).map { |k| n / (5**k) }.reduce(:+)
  # (1..n).inject(:*) || 1
end

p trailing_zeroes(30)

# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
# Example 1:
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 &times; 1 = 1.
# Example 2:
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 &times;3 &times;4 = 36.
# Note: You may assume that n is not less than 2 and not larger than 58.
#
#  https://leetcode.com/problems/integer-break/description/
require './aux.rb'

# @param {Integer} n
# @return {Integer}
def integer_break(n)
  return n - 1 if n < 4
  return n if n == 4
  res = 1
  while n > 4
    n -= 3
    res *= 3
  end
  res * n
end

n = 11
p integer_break(n)

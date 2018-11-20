# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
# Example:
# Input: 13
# Output: 6
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
#
#  https://leetcode.com/problems/number-of-digit-one/description/
require './aux.rb'

# @param {Integer} n
# @return {Integer}
def count_digit_one(n)
  return 0 if n <= 0
  return 1 if n < 10
  fd = n
  rest = 1
  while fd >= 10
    fd /= 10
    rest *= 10
  end
  (fd == 1 ? 1 + n - rest + count_digit_one(rest - 1) : rest + fd * count_digit_one(rest - 1)) + count_digit_one(n % rest)
end

n = 1999
p count_digit_one(n)

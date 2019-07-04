#
# @lc app=leetcode id=507 lang=ruby
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
# @param {Integer} num
# @return {Boolean}
def check_perfect_number(num)
	return false if num <= 1
  res = 1
  2.upto(Math.sqrt(num)).each do |i|
    next if num % i > 0

    res += i
    res += num / i if num / i != i
    return false if res > num
  end
  return false if res < num

  true
end

num = 12
p check_perfect_number(num)

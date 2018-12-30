#
# @lc app=leetcode id=342 lang=ruby
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (39.80%)
# Total Accepted:    101.4K
# Total Submissions: 254.7K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
#
# Example 1:
#
#
# Input: 16
# Output: true
#
#
#
# Example 2:
#
#
# Input: 5
# Output: false
#
#
# Follow up: Could you solve it without loops/recursion?
#
# @param {Integer} num
# @return {Boolean}
def is_power_of_four_2(num)
  cs = num.to_s(2)[1..-1].chars
  cs.uniq == ['0'] && cs.size.even? || num == 1
end

def is_power_of_four(num)
	(num & (num - 1)).zero? && ((num - 1) % 3).zero?
	# power of 2  and 4^a - 1 = (2^a + 1) * (2^a - 1), one of them divided by 3
end


p is_power_of_four(1)

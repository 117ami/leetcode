#
# @lc app=leetcode id=869 lang=ruby
#
# [869] Reordered Power of 2
#
# https://leetcode.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (50.35%)
# Total Accepted:    8.7K
# Total Submissions: 17.3K
# Testcase Example:  '1'
#
# Starting with a positive integer N, we reorder the digits in any order
# (including the original order) such that the leading digit is not zero.
#
# Return true if and only if we can do this in a way such that the resulting
# number is a power of 2.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: 1
# Output: true
#
#
#
# Example 2:
#
#
# Input: 10
# Output: false
#
#
#
# Example 3:
#
#
# Input: 16
# Output: true
#
#
#
# Example 4:
#
#
# Input: 24
# Output: false
#
#
#
# Example 5:
#
#
# Input: 46
# Output: true
#
#
#
#
# Note:
#
#
# 1 <= N <= 10^9
#
#
#
#
#
#
#
#
# @param {Integer} n
# @return {Boolean}
def reordered_power_of2(n)
  arr = n.to_s.chars.map(&:to_i).sort
  maxp = arr.reverse.join.to_i
  x = 1
  while x <= maxp
    return true if x.to_s.chars.map(&:to_i).sort == arr
    x *= 2
  end
  false
end

n = 1
p reordered_power_of2(n)

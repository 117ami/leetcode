#
# @lc app=leetcode id=1015 lang=ruby
#
# [1015] Numbers With Repeated Digits
#
# https://leetcode.com/problems/numbers-with-repeated-digits/description/
#
# algorithms
# Hard (33.80%)
# Total Accepted:    1.8K
# Total Submissions: 5.3K
# Testcase Example:  '20'
#
# Given a positive integer N, return the number of positive integers less than
# or equal to N that have at least 1 repeated digit.
#
#
#
#
# Example 1:
#
#
# Input: 20
# Output: 1
# Explanation: The only positive number (<= 20) with at least 1 repeated digit
# is 11.
#
#
#
# Example 2:
#
#
# Input: 100
# Output: 10
# Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are
# 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
#
#
#
# Example 3:
#
#
# Input: 1000
# Output: 262
#
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
# @param {Integer} n
# @return {Integer}
def num_dup_digits_at_most_n(n)
  digits = (n + 1).to_s.chars.map(&:to_i)
  perm = ->(a, b) { b.zero? ? 1 : perm.call(a, b - 1) * (a - b + 1) }

  res = (1..digits.size - 1).map { |k| 9 * perm.call(9, k - 1) }.reduce(:+) || 0
  seen = {}

  digits.each_with_index do |x, i|
    si = i.zero? ? 1 : 0
    si.upto(x - 1).each do |y|
      res += perm.call(9 - i, digits.size - i - 1) unless seen.key?(y)
    end
    break if seen.key?(x)

    seen[x] = true
  end
  n - res
end

n = 1
p num_dup_digits_at_most_n(n)

#
# @lc app=leetcode id=967 lang=ruby
#
# [967] Numbers With Same Consecutive Differences
#
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
#
# algorithms
# Medium (29.98%)
# Total Accepted:    2.9K
# Total Submissions: 8.9K
# Testcase Example:  '3\n7'
#
# Return all non-negative integers of length N such that the absolute
# difference between every two consecutive digits is K.
#
# Note that every number in the answer must not have leading zeros except for
# the number 0 itself. For example, 01 has one leading zero and is invalid, but
# 0 is valid.
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
#
# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading
# zeroes.
#
#
#
# Example 2:
#
#
# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#
#
#
# Note:
#
#
# 1 <= N <= 9
# 0 <= K <= 9
#
#
#
# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def nums_same_consec_diff(n, k)
  return (0..9).to_a if n == 1

  res = (1..9).to_a

  (n - 1).times do |_|
    tmp = []
    res.each do |n|
      last_digit = n % 10
      tmp << n * 10 + last_digit - k if last_digit >= k
      tmp << n * 10 + last_digit + k if last_digit + k <= 9
    end
    res = tmp
  end
  res.uniq
  # res.map(&:join).reject { |s| s[0] == '0' }.map(&:to_i).uniq
end

p nums_same_consec_diff(2, 1)

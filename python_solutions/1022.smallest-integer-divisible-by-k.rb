#
# @lc app=leetcode id=1022 lang=ruby
#
# [1022] Smallest Integer Divisible by K
#
# https://leetcode.com/problems/smallest-integer-divisible-by-k/description/
#
# algorithms
# Medium (23.03%)
# Total Accepted:    3.2K
# Total Submissions: 13.1K
# Testcase Example:  '1'
#
# Given a positive integer K, you need find the smallest positive integer N
# such that N is divisible by K, and N only contains the digit 1.
#
# Return the length of N.  If there is no such N, return -1.
#
#
#
# Example 1:
#
#
# Input: 1
# Output: 1
# Explanation: The smallest answer is N = 1, which has length 1.
#
# Example 2:
#
#
# Input: 2
# Output: -1
# Explanation: There is no such positive integer N divisible by 2.
#
# Example 3:
#
#
# Input: 3
# Output: 3
# Explanation: The smallest answer is N = 111, which has length 3.
#
#
#
# Note:
#
#
# 1 <= K <= 10^5
#
#
# @param {Integer} k
# @return {Integer}
def smallest_repunit_div_by_k(k)
  return -1 if k.even? || k % 5 == 0

  r = 0
  1.upto(k).each do |i|
    r = (r * 10 + 1) % k
    return i if r.zero?
  end
  -1
end

p smallest_repunit_div_by_k(7)

1.upto(100).each do |k|
  p [k, smallest_repunit_div_by_k(k)]
end

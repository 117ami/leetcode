# We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}. (Note that '0' is not included.)
# Now, we write numbers using these digits, using each digit as many times as we want. For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.
# Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.
#
# Example 1:
# Input: D = ["1","3","5","7"], N = 100
# Output: 20
# Explanation:
# The 20 numbers that can be written are:
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
# Example 2:
# Input: D = ["1","4","9"], N = 1000000000
# Output: 29523
# Explanation:
# We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
# 81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
# 2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
# In total, this is 29523 integers that can be written using the digits of D.
#
# Note:
#   D is asubset of digits '1'-'9' in sorted order.
#   1 <= N <= 10^9
#
#  https://leetcode.com/problems/numbers-at-most-n-given-digit-set/description/
require './aux.rb'

# @param {String[]} d
# @param {Integer} n
# @return {Integer}
def at_most_n_given_digit_set(d, n)
  1.upto(n.to_s.size).map { |len| lessthan(d, n, len) }.reduce(:+)
end

def lessthan(d, n, len)
  # p [d, n, len ]
  n -= 1 if n % 10 == 0
  sn = n.to_s
  return 0 if len > sn.length || len.zero?
  return d.select { |k| k.to_i <= sn.to_i }.size if len == 1
  return d.size**len if len < sn.length
  res = 0
  d.each do |k|
    break if k.to_i > sn[0].to_i
    res += k.to_i == sn[0].to_i ? lessthan(d, sn[1..-1], len - 1) : lessthan(d, 10**len, len - 1)
  end
  res
end

d = %w[1 4 9]
d = %w[1 7]
n = 1_000_000_000
n = 231
p at_most_n_given_digit_set(d, n)
p lessthan(d, n, 9)

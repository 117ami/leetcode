# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
# Example 1:
# Input: [5,7]
# Output: 4
# Example 2:
# Input: [0,1]
# Output: 0
#
#  https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
require './aux.rb'

# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def range_bitwise_and(m, n)
  return 0 if m.zero?
  # return Array(m..n).reduce(:&) if n - m < 10000
  sn = n.to_s(2)
  sm = m.to_s(2)
  res = sn.dup
  (0..sm.size - 1).each { |i| res[sn.size - sm.size + i] = '0' if sm[i] == '0' }

  sdup = sn.dup
  (0..sn.size - 1).each do |i|
    next if sn[i] == '0'
    sdup[i] = '0'
    res[i] = '0' if sn.size > sm.size || sdup.to_i(2) >= m
    # p [i, res, sn, sdup]
    sdup[i] = '1'
  end
  res.to_i(2)
end

def range_bitwise_and2(m, n)
  return 0 if m.zero?
  n > m ? range_bitwise_and(m >> 1, n >> 1) << 1 : m
end

def range_bitwise_and3(m, n)
  a, b = [m, n].map { |i| i.to_s(2) }
  return 0 if a.size != b.size
  i = -1
  i += 1 while i + 1 <= a.size - 1 && a[i + 1] == b[i + 1]
  a[0..i].to_i(2) << (a.size - i - 1)
end

m = 100
n = 120
p range_bitwise_and(m, n)
p range_bitwise_and2(m, n)
p range_bitwise_and3(m, n)

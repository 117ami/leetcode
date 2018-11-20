#
# Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?
# Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.
# Example 1:
# Input: m = 3, n = 3, k = 5
# Output:
# Explanation:
# The Multiplication Table:
# 1  2  3
# 2  4  6
# 3  6  9
# The 5-th smallest number is 3 (1, 2, 2, 3, 3).
# Example 2:
# Input: m = 2, n = 3, k = 6
# Output:
# Explanation:
# The Multiplication Table:
# 1  2  3
# 2  4  6
# The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
# Note:
# The m and n will be in the range [1, 30000].
# The k will be in the range [1, m * n]
#
#  https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/
require './aux.rb'

# @param {Integer} m
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def find_kth_number(m, n, k)
  low = 1
  high = m * n
  cter = ->(x, m, n) { 1.upto(m).map { |i| [x / i, n].min }.reduce(:+) }

  while low < high
    mi = (low + high) / 2
    high, low = cter.call(mi, m, n) >= k ? [mi, low] : [high, mi + 1]
  end

  low
end

p find_kth_number(4, 5, 11)

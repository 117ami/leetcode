# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).
# After this process, we have some array B.
# Return the smallest possible difference between the maximum value of Band the minimum value of B.
#
# Example 1:
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]
# Example 2:
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]
# Example 3:
# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]
#
# Note:
#   1 <= A.length <= 10000
#   0 <= A[i] <= 10000
#   0 <= K <= 10000
#
#  https://leetcode.com/problems/smallest-range-ii/description/
require './aux.rb'

# @param {Integer[]} a
# @param {Integer} k
# @return {Integer}
def smallest_range_ii(a, k)
  return 0 if a.size == 1
  a.sort!
  mx = a.last
  mn = a.first
  res = mx - mn
  0.upto(a.size - 2).each do |idx|
    mx = [mx, a[idx] + 2 * k].max
    mn = [a[idx + 1], a[0] + 2 * k].min
    res = [res, mx - mn].min
  end
  res
 end

a = [7, 8, 8, 5, 2]
k = 3
# a = [1, 3, 5, 8, 9, 13]
# k = 1
p smallest_range_ii(a, k)

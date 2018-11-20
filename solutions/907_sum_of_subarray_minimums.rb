# Given an array of integers A, find the sum of min(B), where B ranges overevery (contiguous) subarray of A.
# Since the answer may be large, return the answer modulo 10^9 + 7.
#
# Example 1:
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1. Sum is 17.
#
# Note:
#   1 <= A.length <= 30000
#   1 <= A[i] <= 30000
#
#  https://leetcode.com/problems/sum-of-subarray-minimums/description/
require './aux.rb'

# @param {Integer[]} a
# @return {Integer}
def sum_subarray_mins(a)
  return a.first if a.size == 1
  a.unshift(0)
  a << 0
  lbound = [0]
  1.upto(a.size - 1).each do |idx|
    lbound[idx] = idx - 1
    if a[idx] < a[idx - 1]
      lbound[idx] = lbound[lbound[idx]] while a[idx] < a[lbound[idx]]
    end
  end

  rbound = []
  rbound[a.size - 1] = a.size - 1
  (a.size - 2).downto(0).each do |idx|
    rbound[idx] = idx + 1
    if a[idx] <= a[idx + 1]
      rbound[idx] = rbound[rbound[idx]] while rbound[idx] < a.size - 1 && a[idx] <= a[rbound[idx]]
    end
  end

  res = 0
  1.upto(a.size - 2).each do |idx|
    res += (idx - lbound[idx]) * (rbound[idx] - idx) * a[idx]
  end

  res % (10**9 + 7)
end

a = [3, 1, 2, 4]
p sum_subarray_mins(a)

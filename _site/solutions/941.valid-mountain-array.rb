# require './aux.rb'
# @param {Integer[]} a
# @return {Boolean}
def valid_mountain_array(a)
  return false if a.size < 3
  idx = 0
  idx += 1 while idx < a.size - 1 && a[idx] < a[idx + 1]
  return false if idx.zero? || idx == a.size - 1
  idx += 1 while idx < a.size - 1 && a[idx] > a[idx + 1]
  idx == a.size - 1
end
# a = [0, 1, 2, 3, 1]
# a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# p valid_mountain_array(a)
# [941] Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/description/
# * algorithms
# * Easy (33.29%)
# * Total Accepted:    4.2K
# * Total Submissions: 12.5K
# * Testcase Example:  '[2,1]'
# Given an array A of integers, return true if and only if it is a valid mountain array.
# Recall that A is a mountain array if and only if:
#   A.length >= 3
#   There exists some i with 0 < i < A.length - 1 such that:
#     A[0] < A[1] < ... A[i-1] < A[i]
#     A[i] > A[i+1] > ... > A[B.length - 1]
# Example 1:
# Input: [2,1]
# Output: false
# Example 2:
# Input: [3,5,5]
# Output: false
# Example 3:
# Input: [0,3,2,1]
# Output: true
# Note:
#   0 <= A.length <= 10000
#   0 <= A[i] <= 10000 

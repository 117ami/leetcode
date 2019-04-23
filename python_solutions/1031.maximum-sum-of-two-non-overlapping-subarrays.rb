#
# @lc app=leetcode id=1031 lang=ruby
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
#
# algorithms
# Medium (52.51%)
# Total Accepted:    2.8K
# Total Submissions: 5.2K
# Testcase Example:  '[0,6,5,2,2,5,1,9,4]\n1\n2'
#
# Given an array A of non-negative integers, return the maximum sum of elements
# in two non-overlapping (contiguous) subarrays, which have lengths L and M.
# (For clarification, the L-length subarray could occur before or after the
# M-length subarray.)
#
# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1])
# + (A[j] + A[j+1] + ... + A[j+M-1]) and either:
#
#
# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length.
#
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
# Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with
# length 2.
#
#
#
# Example 2:
#
#
# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with
# length 2.
#
#
#
# Example 3:
#
#
# Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8]
# with length 3.
#
#
#
#
# Note:
#
#
# L >= 1
# M >= 1
# L + M <= A.length <= 1000
# 0 <= A[i] <= 1000
#
#
#
#
#
#
# @param {Integer[]} a
# @param {Integer} l
# @param {Integer} m
# @return {Integer}
def max_sum_two_no_overlap(a, l, m)
  1.upto(a.size - 1).map { |i| a[i] += a[i - 1] }
  res = a[l + m - 1]
  lmax = a[l - 1]
  mmax = a[m - 1]
  (l + m).upto(a.size - 1).each do |i|
    lmax = [lmax, a[i - m] - a[i - l - m]].max
    mmax = [mmax, a[i - l] - a[i - l - m]].max
    res = [res, a[i] - a[i - m] + lmax, a[i] - a[i - l] + mmax].max
  end
  res
end

a = [3, 8, 1, 3, 2, 1, 8, 9, 0]
l = 3
m = 2

# a = [2,1,5,6,0,9,5,0,3,8]
# l = 4
# m = 3

# a = [0, 6, 5, 2, 2, 5, 1, 9, 4]
# l = 1
# m = 2

p max_sum_two_no_overlap(a, l, m)

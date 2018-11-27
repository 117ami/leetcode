# require './aux.rb'
# @param {Integer} n
# @return {Integer[]}
def beautiful_array(n)
  res = [1]
  res = res.map { |i| i * 2 - 1 } + res.map { |i| i * 2 } while res.size < n
  res.select { |i| i <= n }
end
# 1.upto(10).each do |n|
#   p [n, beautiful_array(n) ]
# end
# [932] Beautiful Array
# https://leetcode.com/problems/beautiful-array/description/
# * algorithms
# * Medium (46.21%)
# * Total Accepted:    2.2K
# * Total Submissions: 4.8K
# * Testcase Example:  '4'
# For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
# Given N, return any beautiful array A.  (It is guaranteed that one exists.)
# Example 1:
# Input: 4
# Output: [2,1,4,3]
# Example 2:
# Input: 5
# Output: [3,1,2,5,4]
# Note:
#   1 <= N <= 1000

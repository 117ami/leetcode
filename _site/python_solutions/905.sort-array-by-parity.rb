#
# @lc app=leetcode id=905 lang=ruby
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (71.54%)
# Total Accepted:    54.7K
# Total Submissions: 76.1K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
#
#
#
# Example 1:
#
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
#
#
#
#
# @param {Integer[]} a
# @return {Integer[]}
def sort_array_by_parity(a)
  a = a.group_by(&:even?).values.flatten
  a.first.even? ? a : a.reverse
end

a = [3, 1, 2, 4]
a = [0, 1]
p sort_array_by_parity(a)

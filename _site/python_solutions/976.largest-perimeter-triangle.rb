#
# @lc app=leetcode id=976 lang=ruby
#
# [976] Largest Perimeter Triangle
#
# https://leetcode.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (56.17%)
# Total Accepted:    7.3K
# Total Submissions: 13.1K
# Testcase Example:  '[2,1,2]'
#
# Given an array A of positive lengths, return the largest perimeter of a
# triangle with non-zero area, formed from 3 of these lengths.
#
# If it is impossible to form any triangle of non-zero area, return 0.
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
# Input: [2,1,2]
# Output: 5
#
#
#
# Example 2:
#
#
# Input: [1,2,1]
# Output: 0
#
#
#
# Example 3:
#
#
# Input: [3,2,3,4]
# Output: 10
#
#
#
# Example 4:
#
#
# Input: [3,6,2,3]
# Output: 8
#
#
#
#
# Note:
#
#
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6
#
#
#
#
#
#
#
# @param {Integer[]} a
# @return {Integer}
def largest_perimeter(a)
  a.sort!
  (a.size - 1).downto(2).map { |i| return a[i] + a[i - 1] + a[i - 2] if a[i] < a[i - 1] + a[i - 2] }
  0
end

a = [2, 6, 3, 3]
a = [1, 2,]
p largest_perimeter(a)

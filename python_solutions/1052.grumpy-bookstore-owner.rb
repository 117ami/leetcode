#
# @lc app=leetcode id=1052 lang=ruby
#
# [1052] Grumpy Bookstore Owner
#
# https://leetcode.com/problems/grumpy-bookstore-owner/description/
#
# algorithms
# Medium (48.54%)
# Total Accepted:    3K
# Total Submissions: 6.2K
# Testcase Example:  '[1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3'
#
# Today, the bookstore owner has a store open for customers.length minutes.
# Every minute, some number of customers (customers[i]) enter the store, and
# all those customers leave after the end of that minute.
#
# On some minutes, the bookstore owner is grumpy.  If the bookstore owner is
# grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the
# bookstore owner is grumpy, the customers of that minute are not satisfied,
# otherwise they are satisfied.
#
# The bookstore owner knows a secret technique to keep themselves not grumpy
# for X minutes straight, but can only use it once.
#
# Return the maximum number of customers that can be satisfied throughout the
# day.
#
#
#
# Example 1:
#
#
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3
# minutes.
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5
# = 16.
#
#
#
#
# Note:
#
#
# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1
#
#
# @param {Integer[]} customers
# @param {Integer[]} grumpy
# @param {Integer} x
# @return {Integer}
def max_satisfied(customers, grumpy, x)
  maxc = customers.reduce(:+)
  lost = grumpy.zip(customers)[x..-1].map { |a, b| a * b }.reduce(:+) || 0
  res = maxc - lost

  1.upto(customers.size - x).each do |i|
    lost += customers[i - 1] * grumpy[i - 1] - customers[i + x - 1] * grumpy[i + x - 1]
    res = [res, maxc - lost].max
  end

  res
end

customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
customers = [1]
grumpy = [0]
x = 1
p max_satisfied(customers, grumpy, x)

#
# @lc app=leetcode id=949 lang=ruby
#
# [949] Largest Time for Given Digits
#
# https://leetcode.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (34.00%)
# Total Accepted:    8.7K
# Total Submissions: 25.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of 4 digits, return the largest 24 hour time that can be
# made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
# 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made,
# return an empty string.
#
#
#
#
# Example 1:
#
#
# Input: [1,2,3,4]
# Output: "23:41"
#
#
#
# Example 2:
#
#
# Input: [5,5,5,5]
# Output: ""
#
#
#
#
# Note:
#
#
# A.length == 4
# 0 <= A[i] <= 9
#
#
#
#
# @param {Integer[]} a
# @return {String}
def valid_time(a)
  a[0] * 10 + a[1] < 24 && a[2] * 10 + a[3] <= 59
end

def largest_time_from_digits(a)
  a.permutation.sort { |a, b| b <=> a }.each do |arr|
    return "#{arr[0]}#{arr[1]}:#{arr[2]}#{arr[3]}" if valid_time(arr)
  end
  ''
end

a = [1, 2, 3, 4]
a = [5, 5, 5, 5]
p largest_time_from_digits(a)

#
# @lc app=leetcode id=485 lang=ruby
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (54.13%)
# Total Accepted:    118.2K
# Total Submissions: 217.8K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
#
# Example 1:
#
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
#
#
#
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
#
#
# @param {Integer[]} nums
# @return {Integer}
def find_max_consecutive_ones(nums)
	nums.join.split('0').map(&:size).max || 0
end

nums = [1,1,0,1,1,1]
nums = [0]
p find_max_consecutive_ones(nums)
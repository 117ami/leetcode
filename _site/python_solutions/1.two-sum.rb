#
# @lc app=leetcode id=1 lang=ruby
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (39.22%)
# Total Accepted:    1.2M
# Total Submissions: 3.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
#
#
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  v2i = nums.map.with_index { |n, i| [n, i] }.to_h
  nums.each_with_index { |n, i| return [i, v2i[target - n]] if v2i.key?(target - n) && v2i[target - n] != i }
end
nums = [2, 7, 11, 15]
target = 9
p two_sum(nums, target)

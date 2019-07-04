#
# @lc app=leetcode id=34 lang=ruby
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (33.24%)
# Total Accepted:    284.1K
# Total Submissions: 854.3K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
#
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def search_range(nums, target)
  leftidx = (0..nums.size - 1).bsearch { |i| nums[i] >= target } || -1
  rightidx = (0..nums.size - 1).bsearch { |i| nums[i] > target } || nums.size
  return [-1, -1] if leftidx == -1 || nums[rightidx - 1] != target

  [leftidx, rightidx - 1]
end

nums = [5, 7, 7, 8, 9, 9, 10, 10]
target = 8

nums = [5,7,7,8,8,10]
target = 6

nums = [1]
target = 1
p search_range(nums, target)

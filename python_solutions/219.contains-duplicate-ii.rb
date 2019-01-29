#
# @lc app=leetcode id=219 lang=ruby
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (34.23%)
# Total Accepted:    178.8K
# Total Submissions: 519.1K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
#
#
#
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
  pre = {}
  nums.each_with_index do |n, i|
    return true if pre.key?(n) && i - pre[n] <= k

    pre[n] = i
  end
  false
end

nums = [1,2,3,1,2,3]
p contains_nearby_duplicate(nums, 2)

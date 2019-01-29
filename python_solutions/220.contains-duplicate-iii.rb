#
# @lc app=leetcode id=220 lang=ruby
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (19.13%)
# Total Accepted:    83.7K
# Total Submissions: 434.2K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
#
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
#
#
#
# Example 3:
#
#
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
#
#
#
#
#
#
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} t
# @return {Boolean}
def contains_nearby_almost_duplicate(nums, k, t)
  return false if t < 0

  d = {}
  nums.each_with_index do |n, i|
    m = n / (t + 1)
    return true if d.key?(m) || d.key?(m - 1) && (d[m - 1] - n).abs <= t || d.key?(m + 1) && (d[m + 1] - n).abs <= t

    d[m] = n
    d.delete(nums[i - k] / (t + 1)) if i >= k
  end
  false
end

#
# @lc app=leetcode id=324 lang=ruby
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (27.11%)
# Total Accepted:    50.8K
# Total Submissions: 187K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] >
# nums[2] < nums[3]....
#
# Example 1:
#
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
#
# Example 2:
#
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
#
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
#
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def wiggle_sort(nums)
  sorted = nums.dup
  sorted.sort!
  i = nums.size - 1
  j = 0
  k = i / 2 + 1
  while i >= 0
    nums[i] = i.odd? ? sorted[k] : sorted[j]
    k += 1 if i.odd?
    j += 1 unless i.odd?
    i -= 1
  end
  nums
end

nums = [1, 3, 2, 2, 3, 1]
nums = [1, 5, 1, 1, 6, 4]
p wiggle_sort(nums)

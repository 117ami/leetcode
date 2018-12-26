#
# @lc app=leetcode id=215 lang=ruby
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (44.45%)
# Total Accepted:    292.7K
# Total Submissions: 657.9K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
#
# Example 2:
#
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
#
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_kth_largest(nums, k)
  nums.sort[-k]
end

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
p find_kth_largest(nums, k)

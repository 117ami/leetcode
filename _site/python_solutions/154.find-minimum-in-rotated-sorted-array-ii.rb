#
# @lc app=leetcode id=154 lang=ruby
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (39.25%)
# Total Accepted:    128.4K
# Total Submissions: 327K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# The array may contain duplicates.
#
# Example 1:
#
#
# Input: [1,3,5]
# Output: 1
#
# Example 2:
#
#
# Input: [2,2,2,0,1]
# Output: 0
#
# Note:
#
#
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
#
#
#
# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
  rec = lambda do |arr|
    return arr.first if arr.size == 1
    return arr.min if arr.size == 2

    mid = (arr.size - 1) / 2
    return rec.call(arr[0..mid]) if arr[mid] < arr.last
    return rec.call(arr[mid..-1])  if arr[mid] > arr.last

    return [rec.call(arr[0..mid]), rec.call(arr[mid..-1])].min
  end
  rec.call(nums)
end

nums = [3, 3, 3, 1, 3]
p find_min(nums)

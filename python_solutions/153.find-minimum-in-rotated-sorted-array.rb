#
# @lc app=leetcode id=153 lang=ruby
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (42.13%)
# Total Accepted:    249K
# Total Submissions: 589.7K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
#
#
# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
  low = 0
  high = nums.size - 1
  key = nums.last
  while low < high
    mid = (low + high) / 2
    if nums[mid] <= key
      high = mid
    else
      low = mid + 1
    end
  end
  nums[low]
end

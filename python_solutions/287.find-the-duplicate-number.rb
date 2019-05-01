#
# @lc app=leetcode id=287 lang=ruby
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (49.21%)
# Total Accepted:    182.2K
# Total Submissions: 370.2K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
#
# Input: [1,3,4,2,2]
# Output: 2
#
#
# Example 2:
#
#
# Input: [3,1,3,4,2]
# Output: 3
#
# Note:
#
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
#
#
#
# @param {Integer[]} nums
# @return {Integer}
def find_duplicate(nums)
  slow = nums.first
  fast = nums[slow]
  cond = 0
  loop do
    if slow == fast
      fast = 0
      cond += 1
    end
    return slow if cond == 2

    slow = nums[slow]
    fast = cond.zero? ? nums[nums[fast]] : nums[fast]
  end
  fast
end

nums = [2, 1, 3, 2, 4, 5]
# nums = [3, 1, 3, 4, 2]
p find_duplicate(nums)

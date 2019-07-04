#
# @lc app=leetcode id=55 lang=ruby
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (30.74%)
# Total Accepted:    218K
# Total Submissions: 709.3K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
# @param {Integer[]} nums
# @return {Boolean}
def can_jump(nums)
  cur_true_idx = nums.size - 1
  (nums.size - 2).downto(0).each do |idx|
    cur_true_idx = idx if idx + nums[idx] >= cur_true_idx
  end
  cur_true_idx.zero?
end

nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
p can_jump(nums)

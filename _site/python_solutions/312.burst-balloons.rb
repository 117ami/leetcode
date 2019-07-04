#
# @lc app=leetcode id=312 lang=ruby
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (47.02%)
# Total Accepted:    62.6K
# Total Submissions: 132.9K
# Testcase Example:  '[3,1,5,8]'
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# number on it represented by array nums. You are asked to burst all the
# balloons. If the you burst balloon i you will get nums[left] * nums[i] *
# nums[right] coins. Here left and right are adjacent indices of i. After the
# burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
# not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
#
# Example:
#
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  -->
# []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
#
# @param {Integer[]} nums
# @return {Integer}
def max_coins(nums)
  return 0 if nums.empty?

  sz = nums.size
  nums.unshift(1)
  nums.push(1)
  dp = Array.new(nums.size) { |_i| Array.new(nums.size, 0) }

  1.upto(sz).each do |len|
    1.upto(sz - len + 1).each do |i|
      j = i + len - 1
      i.upto(j).each do |k|
        dp[i][j] = [dp[i][j], dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1]].max
      end
    end
  end
  dp[1][sz]
end

nums = [3, 1, 5, 8]
p max_coins(nums)

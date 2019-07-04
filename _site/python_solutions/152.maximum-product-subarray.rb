#
# @lc app=leetcode id=152 lang=ruby
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.27%)
# Total Accepted:    211.5K
# Total Submissions: 722.5K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
  m = nums.size
  return nums.first if m == 1

  imax = imin = 1
  res = 0
  nums.each do |n|
    imax, imin = imin, imax if n < 0

    imax = [n, n * imax].max
    imin = [n, n * imin].min
    res = [res, imax].max
  end
  res
end

nums = [2, 3, -2, 4,-1]
p max_product(nums)

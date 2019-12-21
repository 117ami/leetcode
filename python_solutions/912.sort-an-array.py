#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (62.73%)
# Total Accepted:    39.8K
# Total Submissions: 63.4K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order.
# 
# 
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
# 
# 
#
class Solution:
    def sortArray(self, ns):
        return sorted(ns)
        



s = Solution()



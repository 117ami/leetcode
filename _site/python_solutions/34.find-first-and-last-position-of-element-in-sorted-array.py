#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (33.24%)
# Total Accepted:    284.1K
# Total Submissions: 854.3K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
#
import bisect


class Solution:
    def searchRange(self, nums, target):
        i = bisect.bisect_left(nums, target)
        j = bisect.bisect_right(nums, target)
        if i == j or nums[j - 1] != target:
            return [-1, -1]
        return [i, j - 1]


nums = [5, 7, 7, 9, 9, 10, 10]
target = 8

nums = [5, 7, 7, 8, 8, 10]
target = 7

# nums = [1]
# target = 1
print(Solution().searchRange(nums, target))

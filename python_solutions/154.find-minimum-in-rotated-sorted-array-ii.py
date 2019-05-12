#
# @lc app=leetcode id=154 lang=python3
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


class Solution:
    def findMin(self, nums):
        start, end, pivot = 0, len(nums) - 1, nums[-1]
        mid = (start + end) // 2
        if end - start <= 1:
            return nums[start] if nums[start] < nums[end] else nums[end]

        if nums[mid] < pivot:
            return self.findMin(nums[:mid + 1])
        elif nums[mid] > pivot:
            return self.findMin(nums[mid:])
        else:
            return min(self.findMin(nums[mid:]), self.findMin(nums[:mid+1]))



s = Solution()
nums = [2, 2, 2, 0, 0, 0, 1]
nums = [1, 2, 3, 5]
nums = [3, 1, 3, 3, 3, ]
print(s.findMin(nums))

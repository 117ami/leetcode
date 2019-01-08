#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (27.11%)
# Total Accepted:    50.8K
# Total Submissions: 187K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] >
# nums[2] < nums[3]....
#
# Example 1:
#
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
#
# Example 2:
#
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
#
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
#


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        dup = sorted(nums)
        i = len(dup) - 1
        k = int(i / 2 + 1)
        j = 0
        while i >= 0:
            nums[i] = dup[k] if i & 1 else dup[j]
            if i & 1:
                k += 1
            if not(i & 1):
                j += 1
            i -= 1
   

nums = [1, 3, 2, 2, 3, 1]
nums = [1, 5, 1, 1, 6, 4]
Solution().wiggleSort(nums)

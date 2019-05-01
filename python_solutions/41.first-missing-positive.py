#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (28.67%)
# Total Accepted:    206.5K
# Total Submissions: 719.7K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#
#


class Solution:
    def firstMissingPositive(self, nums):
        length = len(nums)
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > length or nums[i] == i + 1:
                continue
            n = nums[i]
            while True:
                tmp, nums[n - 1] = nums[n - 1], n
                if tmp <= 0 or tmp >= length or tmp == n:
                    break
                n = tmp

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1

        return 1 if len(nums) == 0 else nums[-1] + 1

nums = [1, 2, 0]
nums = [3, 4, -1, 1]
# nums = [7,8,9,11,12]
# nums = [3, 1]
# nums = []
print(Solution().firstMissingPositive(nums))
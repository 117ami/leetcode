#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (53.24%)
# Total Accepted:    149.1K
# Total Submissions: 280K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
#
#
#


class Solution:
    def findDisappearedNumbers(self, nums):
        i = 0
        while i < len(nums):
            n = nums[i]
            while n > 0:
                m = nums[n - 1]
                nums[n - 1] = -1 * n
                n = m
            i += 1
        return [i + 1 for i, n in enumerate(nums) if n > 0]


# nums = [4, 3, 2, 7, 8, 2, 3, 1]
# nums =[1, 2, 5, 4, 4]
# s = Solution()
# print(s.findDisappearedNumbers(nums))

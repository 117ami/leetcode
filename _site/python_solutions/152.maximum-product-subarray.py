#
# @lc app=leetcode id=152 lang=python3
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


class Solution:
    def maxProduct(self, nums):
        res = nums[0]
        imax = imin = 1
        for n in nums:
            if n < 0:
                imax, imin = imin, imax
            imax = max(n * imax, n)
            imin = min(n * imin, n)
            res = max(res, imax)
        return res


s = Solution()
nums = [2, 3, -2, 4]
print(s.maxProduct(nums))

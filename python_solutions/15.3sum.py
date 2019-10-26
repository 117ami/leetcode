#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (24.88%)
# Total Accepted:    678.3K
# Total Submissions: 2.7M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#
class Solution:
    def threeSum(self, nums):
        def nsum(l, r, target, cter, cur, res):
            if r - l + 1 < cter or cter < 2 or nums[l] * cter > target or nums[r] * cter < target: 
                return 
            if cter == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(cur + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                    elif s < target: l += 1 
                    else: r -= 1
            else:
                for i in range(l, r+1):
                    if i == l or nums[i] != nums[i-1]:
                        nsum(i + 1, r, target - nums[i], cter - 1, cur + [nums[i]], res)
            
        nums.sort()
        res = [] 
        nsum(0, len(nums) - 1, 0, 3, [], res)
        return res 

s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))


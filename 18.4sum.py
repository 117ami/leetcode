#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (31.60%)
# Total Accepted:    266.5K
# Total Submissions: 843.2K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution:
    def fourSum(self, nums, target):
        def nSum(l, r, target, N, result, results):
            if r - l + 1 < N or N < 2 or  nums[l] * N > target or nums[r] * N < target:
                return 
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]: 
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r+1):
                    if i == l or nums[i-1] != nums[i]:
                        nSum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)
        
        nums.sort()
        results = []
        nSum(0, len(nums)-1, target, 4, [], results)
        return results

s = Solution()
nums = [-2,-1,0,0,1,2]
print(s.fourSum(nums, 0))


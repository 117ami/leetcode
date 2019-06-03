#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (40.57%)
# Total Accepted:    86.4K
# Total Submissions: 212.9K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# Note:
# 
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# 
#
class Solution:
    def canPartition(self, nums):
    	mus = sum(nums)
    	if mus % 2 == 1: return False
    	self.target = mus / 2
    	self.seen = {}
    	return self.dfs(0, 0, nums)

    def dfs(self, i, acc, nums):
    	if acc == self.target: return True
    	if i >= len(nums) or acc > self.target: return False 

    	key = "{}-{}".format(acc, i)
    	if key in self.seen: return self.seen[key]

    	res = self.dfs(i+1, acc+nums[i], nums) or self.dfs(i+1, acc, nums) 
    	self.seen[key] = res

    	return res
        



s = Solution()
nums = [1, 5, 11, 5, 8]
print(s.canPartition(nums))


#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#
# https://leetcode.com/problems/random-pick-index/description/
#
# algorithms
# Medium (49.74%)
# Total Accepted:    54.7K
# Total Submissions: 110K
# Testcase Example:  '["Solution","pick"]\n[[[1,2,3,3,3]],[3]]'
#
# Given an array of integers with possible duplicates, randomly output the
# index of a given target number. You can assume that the given target number
# must exist in the array.
# 
# Note:
# The array size can be very large. Solution that uses too much extra space
# will not pass the judge.
# 
# Example:
# 
# 
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should
# have equal probability of returning.
# solution.pick(3);
# 
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
# 
# 
#
class Solution:

    def __init__(self, nums):
    	self.nums = nums
        

    def pick(self, target):
    	import random
    	res = count = 0
    	for i, n in enumerate(self.nums):
    		if n == target:
    			count += 1
    			if random.randint(1, 10 ** 9) % count == 0:
    				res = i
    	return res 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)



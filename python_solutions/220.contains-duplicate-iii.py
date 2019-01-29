#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (19.13%)
# Total Accepted:    83.7K
# Total Submissions: 434.2K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# 
# 
# 
#
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False 
        buckets = {}
        for i, n in enumerate(nums):
        	bid = n // (t+1)
        	if bid in buckets:
        		return True
        	if bid - 1 in buckets and abs(n - buckets[bid-1]) <= t:
        		return True 
        	if bid + 1 in buckets and abs(n - buckets[bid+1]) <= t:
        		return True 
        	buckets[bid] = n 
        	if i >= k: del buckets[nums[i-k] // (t+1)]
        	# print(buckets)
        return False

print(Solution().containsNearbyAlmostDuplicate([2, 1], 1, 1))

        

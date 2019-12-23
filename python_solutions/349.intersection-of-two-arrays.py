from collections import Counter, defaultdict
true = True
false = False
#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (58.34%)
# Total Accepted:    282.2K
# Total Submissions: 483.5K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# 
# 
# Note:
# 
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# 
# 
# 
#
class Solution:
    def intersection(self, a, b):
        return list(set(a).intersection(set(b)))
        

s = Solution()



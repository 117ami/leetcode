#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (33.65%)
# Total Accepted:    57.8K
# Total Submissions: 171.7K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# The length of path between two nodes is represented by the number of edges
# between them.
# 
# 
# 
# Example 1:
# 
# Input:
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input:
# 
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# Output: 2
# 
# 
# 
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
    	self.res = 0    	
    	def dfs(r):
    		lv = dfs(r.left) if r.left else 0
    		rv = dfs(r.right) if r.right else 0    		
    		lv_ = lv + 1 if r.left and r.left.val == r.val else 0
    		rv_ = rv + 1 if r.right and r.right.val == r.val else 0    		
    		self.res = max(self.res, lv_ + rv_)
    		return max(lv_, rv_)

    	if root:
    		dfs(root)
    	return self.res



s = Solution()



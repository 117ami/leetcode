#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (36.54%)
# Total Accepted:    270.5K
# Total Submissions: 739.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def hasPathSum(self, root, n):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		if not root:
			return False
		if root.val == n and not root.left and not root.right:
			return True
		n -= root.val
		return self.hasPathSum(root.left, n) or self.hasPathSum(root.right, n)
		

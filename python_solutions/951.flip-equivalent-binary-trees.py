#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#
# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
#
# algorithms
# Medium (65.41%)
# Total Accepted:    29.3K
# Total Submissions: 44.9K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]'
#
# For a binary tree T, we can define a flip operation as follows: choose any
# node, and swap the left and right child subtrees.
# 
# A binary tree X is flip equivalent to a binary tree Y if and only if we can
# make X equal to Y after some number of flip operations.
# 
# Write a function that determines whether two binary trees are flip
# equivalent.  The trees are given by root nodes root1 and root2.
# 
# 
# 
# Example 1:
# 
# 
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
# [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
# 
# 
# 
# 
# 
# Note:
# 
# 
# Each tree will have at most 100 nodes.
# Each value in each tree will be a unique integer in the range [0, 99].
# 
# 
# 
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, r1, r2):
        if not r1 or not r2: return r1 == r2
        return r1.val == r2.val and (self.flipEquiv(r1.left, r2.left) and  self.flipEquiv(r1.right, r2.right) \
                                or self.flipEquiv(r1.left, r2.right) and self.flipEquiv(r1.right, r2.left))





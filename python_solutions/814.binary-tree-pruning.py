#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#
# https://leetcode.com/problems/binary-tree-pruning/description/
#
# algorithms
# Medium (72.47%)
# Total Accepted:    47.8K
# Total Submissions: 66K
# Testcase Example:  '[1,null,0,0,1]'
#
# We are given the head node root of a binary tree, where additionally every
# node's value is either a 0 or a 1.
#
# Return the same tree where every subtree (of the given tree) not containing a
# 1 has been removed.
#
# (Recall that the subtree of a node X is X, plus every node that is a
# descendant of X.)
#
#
# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]
# ⁠
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
#
#
#
#
#
# Example 2:
# Input: [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
#
#
#
#
#
#
# Example 3:
# Input: [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
#
#
#
#
#
# Note:
#
#
# The binary tree will have at most 100 nodes.
# The value of each node will only be 0 or 1.
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
    
    def pruneTree(self, root):
        def includeOne(r):
            if r.left and not includeOne(r.left):
                r.left = None
            if r.right and not includeOne(r.right):
                r.right = None 
            if r.left or r.right or r.val == 1:
                return True 

        return root if includeOne(root) else None   


s = Solution()

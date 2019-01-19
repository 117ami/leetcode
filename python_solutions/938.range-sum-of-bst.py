#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#
# https://leetcode.com/problems/range-sum-of-bst/description/
#
# algorithms
# Medium (82.91%)
# Total Accepted:    7K
# Total Submissions: 8.4K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# Given the root node of a binary search tree, return the sum of values of all
# nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.
#
#
#
#
# Example 1:
#
#
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
#
#
#
# Example 2:
#
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
#
#
#
#
# Note:
#
#
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.
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
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        return root.val + \
            self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

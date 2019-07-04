#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (39.89%)
# Total Accepted:    278.3K
# Total Submissions: 697.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# Return false.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._depth(root, 0)[0]

    def _depth(self, root, d):
        '''
        :rtype: [bool, int]
        '''
        if not root:
            return [True, d]

        lb, ld = self._depth(root.left, d + 1)
        rb, rd = self._depth(root.right, d + 1)
        return [lb and rb and abs(ld - rd) <= 1, max(ld, rd)]

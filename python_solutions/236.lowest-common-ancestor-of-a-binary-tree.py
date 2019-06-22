#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (37.72%)
# Total Accepted:    286.5K
# Total Submissions: 759.1K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
#
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
#
#
#
#
# Note:
#
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# import aux


class Solution:
    def lowestCommonAncestor(self, r, p, q):
        if r is None or r.val == p.val or r.val == q.val:
            return r
        left = self.lowestCommonAncestor(r.left, p, q)
        right = self.lowestCommonAncestor(r.right, p, q)
        return right if not left else (left if not right else r)


# arr = [3,5,1,6,2,0,8,None,None,7,4]
# root = aux.tree_from_list(arr)
# p = root.left
# q = root.left.right.right
# s = Solution()
# print(s.lowestCommonAncestor(root, p, q).val)

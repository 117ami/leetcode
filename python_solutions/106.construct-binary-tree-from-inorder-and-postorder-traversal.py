from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (42.33%)
# Total Accepted:    184.1K
# Total Submissions: 433.9K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
#
# Return the following binary tree:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, ino, pos):
        idx = {n:i for i, n in enumerate(ino)}
        def rec(lo, hi):
            if lo > hi: return 
            i = idx[pos[-1]]
            r = TreeNode(pos.pop())
            r.right = rec(i + 1, hi)
            r.left = rec(lo, i - 1)
            return r 
        return rec(0, len(ino) - 1)

sol = Solution()
ino, pos = [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
r = sol.buildTree(ino, pos)
print(r.right.right.val)

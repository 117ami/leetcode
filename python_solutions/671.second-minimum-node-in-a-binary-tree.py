from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
from functools import reduce 
import string
true = True
false = False
#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (43.04%)
# Total Accepted:    62.1K
# Total Submissions: 144.2K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. More formally, the property root.val =
# min(root.left.val, root.right.val) always holds.
# 
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree.
# 
# If no such second minimum value exists, output -1 instead.
# 
# Example 1:
# 
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
# 
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   2
# 
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest
# value.
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
    def treeToList(self, root):
        """Encodes a tree to a list
        :type root: TreeNode
        :rtype: list[int]
        """
        if not root: return []
        jobs = [root]
        res = []
        while jobs:
            r = jobs.pop(0)
            if r:
                res.append(r.val)
                jobs += [r.left, r.right]
        return res

    
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = sorted(list(set(self.treeToList(root))))
        return -1 if len(res) < 2 else res[1]
        

sol = Solution()



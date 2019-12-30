from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
from functools import reduce 
import string
true = True
false = False
#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
## algorithms
# Hard (31.85%)
# Total Accepted:    256.3K
# Total Submissions: 804.3K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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

    def listToTree(self, arr):
        """Build tree for a list. E.g., [1,2,3,None,4]
        """
        if not arr:
            return
        children = 0
        i = 1
        jobs = [TreeNode(arr[0])]
        root = jobs[0]
        while i < len(arr):
            if children == 2:
                jobs.pop(0)
                children = 0

            if arr[i] is not None:
                c = TreeNode(arr[i])
                if children == 0:
                    jobs[0].left = c
                else:
                    jobs[0].right = c
                jobs.append(c)

            children += 1
            i += 1

        return root

    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -0x3f3f3f3f
        def dfs(node):
            if not node: return 0 
            left, right = max(0, dfs(node.left)), max(0, dfs(node.right))
            self.res = max(self.res, left + right + node.val)
            return node.val + max(left, right)
        dfs(root)
        return self.res 
        
sol = Solution()
arr = [-10, 9, 20, None, None, 15, 7]
# arr = [-3]
# arr =[2,-1]
root = sol.listToTree(arr)
print(sol.maxPathSum(root))




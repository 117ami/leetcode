
from aux import * 
import collections
import functools
import bisect

#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (39.57%)
# Total Accepted:    43.2K
# Total Submissions: 109.2K
# Testcase Example:  '[1,3,2,5,3,None,9]'
#
# Given a binary tree, write a function to get the maximum width of the given
# tree. The width of a tree is the maximum width among all levels. The binary
# tree has the same structure as a full binary tree, but some nodes are None.
#
# The width of one level is defined as the length between the end-nodes (the
# leftmost and right most non-None nodes in the level, where the None nodes
# between the end-nodes are also counted into the length calculation.
#
# Example 1:
#
#
# Input:
#
# ⁠          1
# ⁠        /   \
# ⁠       3     2
# ⁠      / \     \
# ⁠     5   3     9
#
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4
# (5,3,None,9).
#
#
# Example 2:
#
#
# Input:
#
# ⁠         1
# ⁠        /
# ⁠       3
# ⁠      / \
# ⁠     5   3
#
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2
# (5,3).
#
#
# Example 3:
#
#
# Input:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /
# ⁠     5
#
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2
# (3,2).
#
#
# Example 4:
#
#
# Input:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /     \
# ⁠     5       9
# ⁠    /         \
# ⁠   6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8
# (6,None,None,None,None,None,None,7).
#
#
#
#
# Note: Answer will in the range of 32-bit signed integer.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        jobs = [(root, 0, 0)]
        cur_d = res = left = 0
        while len(jobs):
            n, d, pos = jobs.pop(0)
            if not n: continue
            if cur_d != d:
                cur_d = d
                left = pos
            res = max(res, pos - left)
            newid = 2 * (pos - left)
            if n.left: jobs.append((n.left, d + 1, newid))
            if n.right: jobs.append((n.right, d + 1, newid + 1))

        return res + 1


# from aux import * 
# s = Solution()
# arr = [1, 3, 2, 5, 3, None, 9]
# arr = [1, 3, 2, 5, None, None, 9, 7, ]
# arr = [0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,0]
# print(arr.count(0))
# print(arr.count(None))
# print(s.widthOfBinaryTree(Trees().listToTree(arr)))

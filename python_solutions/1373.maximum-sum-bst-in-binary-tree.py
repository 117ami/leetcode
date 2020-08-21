from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1373 lang=python3
#
# [1373] Maximum Sum BST in Binary Tree
#
# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
#
# algorithms
# Hard (42.28%)
# Total Accepted:    5.5K
# Total Submissions: 13.1K
# Testcase Example:  '[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]'
#
# Given a binary tree root, the task is to return the maximum sum of all keys
# of any sub-tree which is also a Binary Search Tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
#
#
#
# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# Explanation: Maximum sum in a valid Binary search tree is obtained in root
# node with key equal to 3.
#
#
# Example 2:
#
#
#
#
# Input: root = [4,3,null,1,2]
# Output: 2
# Explanation: Maximum sum in a valid Binary search tree is obtained in a
# single root node with key equal to 2.
#
#
# Example 3:
#
#
# Input: root = [-4,-2,-5]
# Output: 0
# Explanation: All values are negatives. Return an empty BST.
#
#
# Example 4:
#
#
# Input: root = [2,1,3]
# Output: 6
#
#
# Example 5:
#
#
# Input: root = [5,4,8,3,null,6,3]
# Output: 7
#
#
#
# Constraints:
#
#
# Each tree has at most 40000 nodes..
# Each node's value is between [-4 * 10^4 , 4 * 10^4].
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.res = 0

        def is_bst(node):
            if not node:
                return (True, 0)
            v = node.val
            ans = True
            left, right = node.left, node.right
            if left and v <= left.val or right and v >= right.val:
                ans = False

            x = is_bst(left)
            y = is_bst(right)
            if ans and x[0] and y[0]:
                self.res = max(self.res, v + x[1] + y[1])
                return (True, v + x[1] + y[1])
            return (False, 0)

        is_bst(root)
        return self.res


sol = Solution()

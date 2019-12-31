
from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (54.94%)
# Total Accepted:    285.5K
# Total Submissions: 519.4K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# Output: 1
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# Output: 3
#
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorder(self, root):
        def rec(node):
            if node.left:
                for other in rec(node.left):
                    yield other
            yield node
            if node.right:
                for other in rec(node.right):
                    yield other

        for node in rec(root):
            yield node

    def kthSmallest(self, root, k):
        cter = 0 
        for n in self.inorder(root):
            cter += 1
            if cter == k:
                return n.val 

# from aux import Trees
# sol = Solution()
# root = [5, 3, 6, 2, 4, None, None, 1]
# k = 3
# t = Trees()
# r = t.listToTree(root)
# print(sol.kthSmallest(r, k))

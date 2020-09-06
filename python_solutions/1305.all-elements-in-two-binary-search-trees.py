from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
from functools import reduce 
import string
true = True
false = False
#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
#
# algorithms
# Medium (77.29%)
# Total Accepted:    3.7K
# Total Submissions: 4.8K
# Testcase Example:  '[2,1,4]\r\n[1,0,3]\r'
#
# Given two binary search trees root1 and root2.
# 
# Return a list containing all the integers from both trees sorted in ascending
# order.
# 
# 
# Example 1:
# 
# 
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
# Output: [-10,0,0,1,2,5,7,10]
# 
# 
# Example 3:
# 
# 
# Input: root1 = [], root2 = [5,1,7,0,2]
# Output: [0,1,2,5,7]
# 
# 
# Example 4:
# 
# 
# Input: root1 = [0,-10,10], root2 = []
# Output: [-10,0,10]
# 
# 
# Example 5:
# 
# 
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
# 
# 
# 
# Constraints:
# 
# 
# Each tree has at most 5000 nodes.
# Each node's value is between [-10^5, 10^5].
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
        jobs = [root]
        res = []
        while len(jobs):
            r = jobs.pop(0)
            if r:
                res.append(r.val)
                jobs += [r.left, r.right]
        return res

    def getAllElements(self, r1, r2):
        a = self.treeToList(r1) + self.treeToList(r2)
        a.sort()
        return a 

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
        jobs = [root]
        res = []
        while len(jobs):
            r = jobs.pop(0)
            if r:
                res.append(r.val)
                jobs += [r.left, r.right]
        return res

    def getAllElements(self, r1, r2):
        a = self.treeToList(r1) + self.treeToList(r2)
        a.sort()
        return a 

        
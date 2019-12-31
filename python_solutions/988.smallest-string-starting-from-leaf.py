from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#
# https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
#
# algorithms
# Medium (44.89%)
# Total Accepted:    17.8K
# Total Submissions: 39.6K
# Testcase Example:  '[0,1,2,3,4,3,4]'
#
# Given the root of a binary tree, each node has a value from 0 to 25
# representing the letters 'a' to 'z': a value of 0 represents 'a', a value of
# 1 represents 'b', and so on.
#
# Find the lexicographically smallest string that starts at a leaf of this tree
# and ends at the root.
#
# (As a reminder, any shorter prefix of a string is lexicographically smaller:
# for example, "ab" is lexicographically smaller than "aba".  A leaf of a node
# is a node that has no children.)
#
#
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
#
#
# Input: [0,1,2,3,4,3,4]
# Output: "dba"
#
#
#
# Example 2:
#
#
#
#
# Input: [25,1,3,1,3,0,2]
# Output: "adz"
#
#
#
# Example 3:
#
#
#
#
# Input: [2,2,1,null,1,0,null,0]
# Output: "abc"
#
#
#
#
# Note:
#
#
# The number of nodes in the given tree will be between 1 and 8500.
# Each node in the tree will have a value between 0 and 25.
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
    def smallestFromLeaf(self, root, s=""):
        # use top-bottom approach 
        if not root:
            return '|'
        s = chr(root.val + 97) + s
        return s if not root.left and not root.right else min(
            self.smallestFromLeaf(
                root.left, s), self.smallestFromLeaf(
                root.right, s))


# from aux import Trees
# t = Trees()
# arr = [0,1,2,3,4,3,4]
# root = t.listToTree(arr)
# sol = Solution()
# print(sol.smallestFromLeaf(root))

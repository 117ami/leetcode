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
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
#
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
#
# algorithms
# Medium (65.34%)
# Total Accepted:    7.4K
# Total Submissions: 11.3K
# Testcase Example:  '[2,3,1,3,1,null,1]'
#
# Given a binary tree where node values are digits from 1 to 9. A path in the
# binary tree is said to be pseudo-palindromic if at least one permutation of
# the node values in the path is a palindrome.
# 
# Return the number of pseudo-palindromic paths going from the root node to
# leaf nodes.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are
# three paths going from the root node to leaf nodes: the red path [2,3,3], the
# green path [2,1,1], and the path [2,3,1]. Among these paths only red path and
# green path are pseudo-palindromic paths since the red path [2,3,3] can be
# rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be
# rearranged in [1,2,1] (palindrome).
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are
# three paths going from the root node to leaf nodes: the green path [2,1,1],
# the path [2,1,3,1], and the path [2,1]. Among these paths only the green path
# is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1]
# (palindrome).
# 
# 
# Example 3:
# 
# 
# Input: root = [9]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The given binary tree will have between 1 and 10^5 nodes.
# Node values are digits from 1 to 9.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root) -> int:
        cc = [0] * 10
        self.odd = 0
        self.res = 0 
        def dfs(n):
            if not n: return 
            v = n.val 
            cc[v] += 1
            self.odd += 1 if cc[v] & 1 else -1 
            
            dfs(n.left)
            dfs(n.right)
            if not n.left and not n.right:
                if self.odd <= 1: self.res += 1
            
            cc[v] -= 1
            self.odd += 1 if cc[v] & 1 else -1

            
        dfs(root)
        return self.res 

                
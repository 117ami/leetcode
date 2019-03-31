#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#
# https://leetcode.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (52.75%)
# Total Accepted:    10.3K
# Total Submissions: 19.5K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# In a binary tree, the root node is at depth 0, and children of each depth k
# node are at depth k+1.
# 
# Two nodes of a binary tree are cousins if they have the same depth, but have
# different parents.
# 
# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree.
# 
# Return true if and only if the nodes corresponding to the values x and y are
# cousins.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
# 
# 
# 
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
    def isCousins(self, root, x, y):
        arr = [[0, 0] for _ in range(101)]        
        def traverse(r, depth, pv):
            if not r: return 
            arr[r.val] = [depth, pv]
            traverse(r.left, depth + 1, r.val)
            traverse(r.right, depth + 1, r.val)            
        
        traverse(root, 0, -1)
        return arr[x][0] == arr[y][0] and arr[x][1] != arr[y][1]

# arr = [[0, 0] for _ in range(100)]
# arr[0][1] = 100
# print(arr)
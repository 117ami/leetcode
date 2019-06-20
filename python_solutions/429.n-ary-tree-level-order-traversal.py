#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Easy (59.64%)
# Total Accepted:    34.7K
# Total Submissions: 58.1K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# We should return its level order traversal:
# 
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
# 
# 
# 
# Note:
# 
# 
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
# 
# 
#
"""
# Definition for a Node.
"""
# class Node:
#     def __init__(self, val, children):
#         self.val = val
#         self.children = children

class Solution:
    def levelOrder(self, root):
        self.res = []
        self.tra(root, 0)
        return self.res

    def tra(self, r, depth):
        if r == None: return
        if depth >= len(self.res):
            self.res.append([])
        self.res[depth].append(r.val)
        for c in r.children:
            self.tra(c, depth+1)

# r = Node(3, [Node(2, []), Node(4, [])])
# s = Solution()
# print(s.levelOrder(r))



#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (66.88%)
# Total Accepted:    37.6K
# Total Submissions: 56.2K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the preorder traversal of its nodes' values.
#
# For example, given a 3-ary tree:
#
#
#
#
#
#
#
# Return its preorder traversal as: [1,3,5,6,2,4].
#
#
#
# Note:
#
# Recursive solution is trivial, could you do it iteratively?
#
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        ans = [root.val]
        for c in root.children:
            ans += self.preorder(c)
        return ans

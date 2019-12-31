from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce 
import string
true = True
false = False
#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (36.52%)
# Total Accepted:    216.3K
# Total Submissions: 592K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# Given a binary tree
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# 
# Follow up:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         t = []
#         def c(n, d):
#             if not n: return 
#             if len(t) <= d:
#                 t.append(n) 
#             else:
#                 t[d].next = n 
#                 t[d] = n 
#             c(n.left, d+1)
#             c(n.right, d+1)
#         c(root, 0)
#         return root 
class Solution:
    def connect(self, root):
        dummy = root 
        nxlevel, pre, cur = None, None, root
        while cur:
            while cur:
                if cur.left:
                    if pre:
                        pre.next = cur.left 
                    else:
                        nxlevel = cur.left
                    pre = cur.left 
                if cur.right:
                    if pre:
                        pre.next = cur.right
                    else:
                        nxlevel = cur.right 
                    pre = cur.right
                cur = cur.next 
            nxlevel, pre, cur = None, None, nxlevel
        return root
                

sol = Solution()



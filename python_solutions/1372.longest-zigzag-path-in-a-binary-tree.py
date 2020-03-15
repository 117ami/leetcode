from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
#
# algorithms
# Medium (49.07%)
# Total Accepted:    3.7K
# Total Submissions: 7.5K
# Testcase Example:  '[1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1]'
#
# Given a binary tree root, a ZigZag path for a binary tree is defined as
# follow:
# 
# 
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right then move to the right child of the current
# node otherwise move to the left child.
# Change the direction from right to left or right to left.
# Repeat the second and third step until you can't move in the tree.
# 
# 
# Zigzag length is defined as the number of nodes visited - 1. (A single node
# has a length of 0).
# 
# Return the longest ZigZag path contained in that tree.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [1,1,1,None,1,None,None,1,1,None,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left ->
# right).
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# Each tree has at most 50000 nodes..
# Each node's value is between [1, 100].
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_from_list(lis):
    if len(lis) == 0:
        return None
    root = TreeNode(lis[0])
    st = [root]
    i, j = 0, 1
    while j < len(lis):
        r = st[i]
        i += 1
        if r is None:
            j += 1
        else:
            lv = lis[j]
            r.left = TreeNode(lv) if lv else None
            st.append(r.left)

            if j + 1 >= len(lis):
                break

            rv = lis[j + 1]
            r.right = TreeNode(rv) if rv else None
            st.append(r.right)

            j += 2

    return root

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0
        def rec(n):
            if not n: return (-1, -1)
            nl, nr = 1 + rec(n.left)[1], 1 + rec(n.right)[0]
            self.res = max([self.res, nl, nr])
            return (nl, nr)
        rec(root)
        return self.res 

sol = Solution()
arr = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1]
# arr = [1,2,3,None,4,None,None,5,6,None,7]
root = tree_from_list(arr)
print(sol.longestZigZag(root))


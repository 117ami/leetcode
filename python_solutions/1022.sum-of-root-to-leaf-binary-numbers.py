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
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007


#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (67.47%)
# Total Accepted:    65.6K
# Total Submissions: 93.2K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path
# represents a binary number starting with the most significant bit.  For
# example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
# 01101 in binary, which is 13.
#
# For all leaves in the tree, consider the numbers represented by the path from
# the root to that leaf.
#
# Return the sum of these numbers.
#
#
#
# Example 1:
#
#
#
#
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
#
#
#
#
# Note:
#
#
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, r, cur):
        if not r: return 0
        cur = cur * 2 + r.val
        if not r.left and not r.right:
            self.res += cur
        self.solve(r.left, cur)
        self.solve(r.right, cur)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        self.solve(root, 0)
        return self.res

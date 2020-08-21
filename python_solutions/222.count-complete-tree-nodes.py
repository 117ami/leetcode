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
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (43.17%)
# Total Accepted:    213.5K
# Total Submissions: 484.1K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
#
# Note:
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level h.
#
# Example:
#
#
# Input:
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
#
# Output: 6
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.left) + \
            self.countNodes(root.right) if root else 0


sol = Solution()

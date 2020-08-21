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
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (51.56%)
# Total Accepted:    312.8K
# Total Submissions: 604.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        jobs = deque()
        jobs.append((root, 0))
        while jobs:
            n, d = jobs.popleft()
            if not n: continue 
            if len(ans) <= d:
                ans.append([])
            ans[d].append(n.val)
            if n.left:
                jobs.append((n.left, d + 1))
            if n.right:
                jobs.append((n.right, d + 1))

        return ans[::-1]


sol = Solution()


# print(sol.__init__())
# print(sol.levelOrderBottom())

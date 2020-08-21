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
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
#
# algorithms
# Medium (67.18%)
# Total Accepted:    5.5K
# Total Submissions: 8.2K
# Testcase Example:  '[3,1,4,3,null,1,5]'
#
# Given a binary tree root, a node X in the tree is named good if in the path
# from root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.
#
#
# Example 1:
#
#
#
#
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
#
# Example 2:
#
#
#
#
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
#
# Example 3:
#
#
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
#
#
# Constraints:
#
#
# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        jobs = deque([(root, -12345)])

        while len(jobs):
            n, v = jobs.popleft()
            if not n: continue
            if n.val >= v: res += 1
            nv = max(n.val, v)
            if n.left:
                jobs.append((n.left, nv))
            if n.right:
                jobs.append((n.right, nv))
        return res

        # self.res = 0
        # def dfs(n, premax):
        #     if not n: return
        #     if n.val >= premax: self.res += 1
        #     premax = max(n.val, premax)
        #     dfs(n.left, premax)
        #     dfs(n.right, premax)
        # dfs(root, -12345)
        # return self.res


sol = Solution()

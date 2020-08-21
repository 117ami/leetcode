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
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/
#
# algorithms
# Medium (47.15%)
# Total Accepted:    6.4K
# Total Submissions: 12.6K
# Testcase Example:  '[1,2,3,null,4]\n3'
#
# Given the root of a binary tree and an integer distance. A pair of two
# different leaf nodes of a binary tree is said to be good if the length of the
# shortest path between them is less than or equal to distance.
#
# Return the number of good leaf node pairs in the tree.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the
# shortest path between them is 3. This is the only good pair.
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The
# pair [4,6] is not good because the length of ther shortest path between them
# is 4.
#
#
# Example 3:
#
#
# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# Explanation: The only good pair is [2,5].
#
#
# Example 4:
#
#
# Input: root = [100], distance = 1
# Output: 0
#
#
# Example 5:
#
#
# Input: root = [1,1,1], distance = 2
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 2^10].
# Each node's value is between [1, 100].
# 1 <= distance <= 10
#
#
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return [0]
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans += len([0 for a, b in itertools.product(left, right)
                             if a > 0 and b > 0 and a + b <= distance])
            res = [l + 1 for l in left + right if l > 0 and l + 1 < distance]
            return res
        dfs(root)
        return self.ans


# r = TreeNode(0)
# r.left = TreeNode(1)
# r.right = TreeNode(1)
# r.left.right = TreeNode(2)
# print(Solution().countPairs(r, 3))

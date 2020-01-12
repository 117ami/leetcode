from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
#
# algorithms
# Medium (83.80%)
# Total Accepted:    2.4K
# Total Submissions: 2.9K
# Testcase Example:  '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
#
# Given a binary tree, return the sum of values of nodes with even-valued
# grandparent.  (A grandparent of a node is the parent of its parent, if it
# exists.)
# 
# If there are no nodes with an even-valued grandparent, return 0.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while
# the blue nodes are the even-value grandparents.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def rec(n, p, gp):
            if not n: return 0
            ans = 0
            if gp == 0:
                ans += n.val
            ans += rec(n.left, n.val % 2, p)
            ans += rec(n.right, n.val % 2, p)
            return ans 
        return rec(root, 1, 1)

sol = Solution()



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
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#
# https://leetcode.com/problems/linked-list-in-binary-tree/description/
#
# algorithms
# Medium (40.10%)
# Total Accepted:    18.8K
# Total Submissions: 45.9K
# Testcase Example:  '[4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'
#
# Given a binary tree root and a linked list with head as the first node.
#
# Return True if all the elements in the linked list starting from the head
# correspond to some downward path connected in the binary tree otherwise
# return False.
#
# In this context downward path means a path that starts at some node and goes
# downwards.
#
#
# Example 1:
#
#
#
#
# Input: head = [4,2,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.
#
#
# Example 2:
#
#
#
#
# Input: head = [1,4,2,6], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
#
#
# Example 3:
#
#
# Input: head = [1,4,2,6,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: false
# Explanation: There is no path in the binary tree that contains all the
# elements of the linked list from head.
#
#
#
# Constraints:
#
#
# 1 <= node.val <= 100 for each node in the linked list and binary tree.
# The given linked list will contain between 1 and 100 nodes.
# The given binary tree will contain between 1 and 2500 nodes.
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kmp(self, head, root):
        def get_lhp(head):
            values = []
            while head:
                values.append(head.val)
                head = head.next
            j = 0
            res = [0] * len(values)
            for i in range(1, len(values)):
                while j > 0 and values[i] != values[j]:
                    j = res[j - 1]
                if values[i] == values[j]:
                    j += 1
                    res[i] = j
            return res, values

        lhp, values = get_lhp(head)

        def dfs(root, j):
            if j == len(lhp): return True
            if not root: return False
            while j > 0 and root.val != values[j]:
                j = lhp[j - 1]
            if root.val == values[j]:
                j += 1
            return dfs(root.left, j) or dfs(root.right, j)

        return dfs(root, 0)

    def isSubPath(self, head, root):
        return self.kmp(head, root)
        def dfs(h, r):
            if not h: return True
            if not r: return False
            return h.val == r.val and (dfs(h.next, r.left)
                                       or dfs(h.next, r.right))

        if not head: return True
        if not root: return False
        return dfs(head, root) or self.isSubPath(
            head, root.left) or self.isSubPath(head, root.right)


# sol = Solution()

# head, root = [4,2,8], [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# head, root = [1,4,2,6], [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# head, root = [1,4,2,6,8], [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# print(sol.__init__(head, root))
# print(sol.__init__(head, root))
# print(sol.isSubPath(head, root))

from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
#
# algorithms
# Medium (39.46%)
# Total Accepted:    65.2K
# Total Submissions: 165.2K
# Testcase Example:  '"9,3,4,#,#,1,#,#,2,#,6,#,#"'
#
# One way to serialize a binary tree is to use pre-order traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as #.
#
#
# ⁠    _9_
# ⁠   /   \
# ⁠  3     2
# ⁠ / \   / \
# ⁠4   1  #  6
# / \ / \   / \
# # # # #   # #
#
#
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
#
# Given a string of comma separated values, verify whether it is a correct
# preorder traversal serialization of a binary tree. Find an algorithm without
# reconstructing the tree.
#
# Each comma separated value in the string must be either an integer or a
# character '#' representing null pointer.
#
# You may assume that the input format is always valid, for example it could
# never contain two consecutive commas such as "1,,3".
#
# Example 1:
#
#
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
#
# Example 2:
#
#
# Input: "1,#"
# Output: false
#
#
# Example 3:
#
#
# Input: "9,#,#,1"
# Output: false
#


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        diff = 1  # diff is the difference of out degree and in degree
        for n in preorder.split(','):
            diff -= 1  # provides an in degree 
            if diff < 0: return false 
            if n.isdigit(): diff += 2  # provides two out degree 
        
        return diff == 0



sol = Solution()
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
preorder = '9,#,#,1'
preorder = "1"
print(sol.isValidSerialization(preorder))

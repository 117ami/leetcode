#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#
# https://leetcode.com/problems/balance-a-binary-search-tree/description/
#
# algorithms
# Medium (73.86%)
# Total Accepted:    5.1K
# Total Submissions: 6.9K
# Testcase Example:  '[1,null,2,null,3,null,4,null,null]'
#
# Given a binary search tree, return a balanced binary search tree with the
# same node values.
# 
# A binary search tree is balanced if and only if the depth of the two subtrees
# of every node never differ by more than 1.
# 
# If there is more than one answer, return any of them.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is
# also correct.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The tree nodes will have distinct values between 1 and 10^5.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, arr):
        if not arr: return 
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self.sortedArrayToBST(arr[:mid])
        root.right = self.sortedArrayToBST(arr[mid+1:])
        return root 

    def treeToList(self, root):
        """Encodes a tree to a list
        :type root: TreeNode
        :rtype: list[int]
        """
        if not root: return []
        jobs, res = [root], []
        while jobs:
            r = jobs.pop(0)
            if r:
                res.append(r.val)
                jobs += [r.left, r.right]
        return res

    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.sortedArrayToBST(sorted(self.treeToList(root)))

        

sol = Solution()



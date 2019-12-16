#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (36.61%)
# Total Accepted:    137.1K
# Total Submissions: 374.1K
# Testcase Example:  '[1,3,null,null,2]'
#
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# Example 1:
# 
# 
# Input: [1,3,null,null,2]
# 
# 1
# /
# 3
# \
# 2
# 
# Output: [3,1,null,null,2]
# 
# 3
# /
# 1
# \
# 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,4,null,null,2]
# 
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
# 
# Output: [2,1,4,null,null,3]
# 
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
# 
# 
# Follow up:
# 
# 
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        last = TreeNode(- 1 << 32)
        ws = []
        while cur:
            if cur.left is None:
                if last.val > cur.val:
                    ws += [last, cur]
                last, cur = cur, cur.right
            else:
                prenode = cur.left 
                while prenode.right is not None and prenode.right is not cur:
                    prenode = prenode.right
                
                if prenode.right is None:
                    prenode.right = cur
                    cur = cur.left 
                else: # restore tree
                    prenode.right = None
                    if last.val > cur.val:
                        ws += [last, cur]
                    last, cur = cur, cur.right 
        
        # print(len(wrongnodes))
        # print(ws[0].val, ws[-1].val)
        ws[0].val, ws[-1].val = ws[-1].val, ws[0].val 

                
# s = Solution()
# from aux import * 
# arr = [3,1,4,None,None,2]
# arr = [1,3,None, None, 2]
# arr = [5,3,9,-2147483648,2]
# root = Trees().listToTree(arr)
# s.recoverTree(root)



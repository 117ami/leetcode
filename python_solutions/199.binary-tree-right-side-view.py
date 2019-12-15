#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (50.66%)
# Total Accepted:    215K
# Total Submissions: 424.2K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def listToTree(self, arr):
        """Build tree for a list. E.g., [1,2,3,None,4]
        """
        if not arr: return 
        children = 0 
        i = 1
        jobs = [TreeNode(arr[0])]
        root = jobs[0]
        while i < len(arr):
            if children == 2: 
                jobs.pop(0)
                children = 0
            
            if arr[i] is not None:
                c = TreeNode(arr[i])
                if children == 0: jobs[0].left = c
                else: jobs[0].right = c
                jobs.append(c) 
            
            children += 1
            i += 1

        return root  
    
    def rightSideView(self, root):
        res = []
        def dfs(node, depth):
            if not node: return 
            if len(res) <= depth:
                res.append([])
            dfs(node.left, depth+1)
            res[depth].append(node.val)
            dfs(node.right, depth+1)
        
        dfs(root, 0)
        return [e[-1] for e in res]
        

s = Solution()
arr = [6,1,None,None,3,2,5,None,None,4]
print(s.rightSideView(s.listToTree(arr)))


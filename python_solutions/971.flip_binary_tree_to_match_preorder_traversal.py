# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal
# Medium (Difficulty)

# Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
# A node in this binary tree can be flipped by swapping the left child and the right child of that node.
# Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.
# (Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)
# Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.
# If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.
# If we cannot do so, then return the list [-1].
#  
# Example 1:
# 
# Example 2:
# 
# Example 3:
# 
#  
# Note:
# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# 
# Input: root = [1,2,3], voyage = [1,3,2]
# Output: [1]
# 
# Input: root = [1,2,3], voyage = [1,2,3]
# Output: []
# 
# xxxxxxxxxx
# /**
#  * Definition for a binary tree node.
#  * struct TreeNode {
#  *     int val;
#  *     TreeNode *left;
#  *     TreeNode *right;
#  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
#  * };
#  */
# class Solution {
# public:
#     vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
#         
#     }
# };


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, r, v):
        #  TreeNode, voyage: List[int]) -> List[int]:
        res = []
        self.idx = 0
        def dfs(root):
            if not root:return True 
            if root.val != v[self.idx]: return False 
            self.idx += 1
            if root.left and root.left.val != v[self.idx]:
                res.append(root.val)
                root.left, root.right = root.right, root.left
            return dfs(root.left) and dfs(root.right)
        return res if dfs(r) else [-1]
        
        
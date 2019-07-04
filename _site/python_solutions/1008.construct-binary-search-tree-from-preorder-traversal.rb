#
# @lc app=leetcode id=1008 lang=ruby
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (72.76%)
# Total Accepted:    5.8K
# Total Submissions: 8K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# Return the root node of a binary search tree that matches the given preorder
# traversal.
# 
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of
# node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then
# traverses node.right.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# 
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= preorder.length <= 100
# The values of preorder are distinct.
# 
# 
#
# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# @param {Integer[]} preorder
# @return {TreeNode}
def bst_from_preorder(preorder)
    return nil if preorder.empty?
    root = TreeNode.new(preorder.first) 
    i = 1
    i += 1 while i < preorder.size && preorder[0] > preorder[i]
    root.left = bst_from_preorder(preorder[1..i-1])
    root.right = bst_from_preorder(preorder[i..preorder.size-1])    
    root
end


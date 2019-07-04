# Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
# /        / \
# 1        7   9
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#  1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#            \
#             7
#              \
#               8
#                \
#                  9
# Note:
#   The number of nodes in the given tree will be between 1 and 100.
#   Each node will have a unique integer value from 0 to 1000.
#
#  https://leetcode.com/problems/increasing-order-search-tree/
require './aux.rb'

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {TreeNode}
def increasing_bst(root)
  return root if root.nil?
  if root.left.nil?
    root.right = increasing_bst(root.right)
    return root
  else
    newroot = increasing_bst(root.left)
    tmp = newroot
    tmp = tmp.right while tmp.right
    tmp.right = root
    root.right = increasing_bst(root.right)
    root.left = nil
    return newroot
  end
end

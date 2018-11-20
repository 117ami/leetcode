# Given inorder and postorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# For example, given
# inorder =[9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
require './aux.rb'

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} inorder
# @param {Integer[]} postorder
# @return {TreeNode}
def build_tree(inorder, postorder)
  return nil if postorder.nil? || postorder.empty?
  return TreeNode.new(postorder[0]) if postorder.size == 1

  rval = postorder.pop
  root = TreeNode.new(rval)
  i = 0
  i += 1 while inorder[i] != rval
  root.left = i.zero? ? nil : build_tree(inorder[0..i - 1], postorder[0..i - 1])
  root.right = build_tree(inorder[i + 1..-1], postorder[i..-1])
  root
end

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
inorder = [1, 3, 2]
postorder = [3, 2, 1]
p build_tree(inorder, postorder)

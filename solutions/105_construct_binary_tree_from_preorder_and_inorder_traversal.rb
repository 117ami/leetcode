# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# For example, given
# preorder =[3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
require './aux.rb'

# @param {Integer[]} preorder
# @param {Integer[]} inorder
# @return {TreeNode}
def build_tree(preorder, inorder)
  return if preorder.empty?
  root = TreeNode.new(preorder[0])
  idx = 0
  idx += 1 until inorder[idx] == preorder[0]

  root.left = build_tree(preorder[1..idx], inorder[0..idx - 1])
  root.right = build_tree(preorder[idx + 1..-1], inorder[idx + 1..-1])
  root
end

preorder = [3, 9, 1, 20, 15, 7]
inorder =  [1, 9, 3, 15, 20, 7]
p build_tree(preorder, inorder)

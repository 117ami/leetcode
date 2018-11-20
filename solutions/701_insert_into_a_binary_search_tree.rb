# Given the root node of a binary search tree (BST) and a value to be inserted into the tree,insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Note that there may existmultiple valid ways for theinsertion, as long as the tree remains a BST after insertion. You can return any of them.
# For example,
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# This tree is also valid:
#          5
#        /   \
#       2     7
#      / \
#     1   3
#          \
#           4
#
#  https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
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
# @param {Integer} val
# @return {TreeNode}
def insert_into_bst(root, val)
  return TreeNode.new(val) unless root
  if val > root.val
    root.right = insert_into_bst(root.right, val)
  else
    root.left = insert_into_bst(root.left, val)
  end
  root
end

root = construct_tree([4, 2, 7, 1, 3])
p insert_into_bst(root, 5)

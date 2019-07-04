# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.
# Example 1:
# Input:
#     2
#    / \
#   1   3
# Output: true
# Example 2:
#     5
#    / \
#   1   4
#     / \
#    3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#             is 5 but its right child's value is 4.
#
#  https://leetcode.com/problems/validate-binary-search-tree/description/
require './aux.rb'

# @param {TreeNode} root
# @return {Boolean}
def is_valid_bst(root)
  bst = lambda do |r, minval, maxval|
    return true if r.nil?
    return false if r.val <= minval || r.val >= maxval
    bst.call(r.left, minval, r.val) && bst.call(r.right, r.val, maxval)
  end
  bst.call(root, -Float::INFINITY, Float::INFINITY)
end

arr = [2, 1, 4]
p is_valid_bst(construct_tree(arr))
# Find the sum of all left leaves in a given binary tree.
# Example:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#  https://leetcode.com/problems/sum-of-left-leaves/description/
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
# @return {Integer}
def sum_of_left_leaves(root, key = 'right')
  return 0 if root.nil?
  if root.left.nil? && root.right.nil?
    return key == 'left' ? root.val : 0
  end

  sum_of_left_leaves(root.left, 'left') + sum_of_left_leaves(root.right, 'right')
end

root = construct_tree([2, 9, 20, 8, 2, 15, 7])
root = construct_tree([1])
p sum_of_left_leaves(root)

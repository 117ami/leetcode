# Given a binary tree, return the tilt of the whole tree.
# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
# Example:
# Input:
#          1
#        /   \
#       2     3
# Output: 1
# Explanation:
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# Note:
# The sum of node values in any subtree won't exceed the range of 32-bit integer.
# All the tilt values won't exceed the range of 32-bit integer.
#
#  https://leetcode.com/problems/binary-tree-tilt/description/
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
def find_tilt(root)
	return 0 if root.nil?
  res = []
  helper = lambda do |r|
    return 0 if r.nil?
    leftsum = helper.call(r.left)
    rightsum = helper.call(r.right)
    res << (leftsum - rightsum).abs
    return leftsum + rightsum + r.val
  end
  helper.call(root)
  res.reduce(:+)
end

arr = [1, 2, 3, 4, 5]
root = construct_tree(arr)
p find_tilt(root)

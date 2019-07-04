#!/usr/bin/ruby -w

# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false

# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

# @param {TreeNode} p
# @param {TreeNode} q
# @return {Boolean}
def same_tree?(p, q)
  return true if p.nil? && q.nil?
  return false if (p.nil? ^ q.nil?) ||
                  (p.val != q.val)

  same_tree?(p.left, q.left) && same_tree?(p.right, q.right)
end

q = TreeNode.new(1)
p = TreeNode.new(1)
q.right = TreeNode.new(nil)
p.right = TreeNode.new(nil)
# p p.left, q.left
p same_tree?(p, q)

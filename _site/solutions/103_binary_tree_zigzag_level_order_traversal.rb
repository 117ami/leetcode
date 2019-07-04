# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
#  https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
require './aux.rb'

# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

# @param {TreeNode} root
# @return {Integer[][]}
def zigzag_level_order(root)
  res = []
  helper = lambda do |r, d|
    return if r.nil?
    res[d] = [] if res[d].nil?
    res[d].push(r.val) if d.even?
    res[d].unshift(r.val) if d.odd?
    helper.call(r.left, d + 1)
    helper.call(r.right, d + 1)
  end
  helper.call(root, 0)
  res
end

root = TreeNode.new(3)
root.left = TreeNode.new(9)
root.right = TreeNode.new(20)
root.right.left = TreeNode.new(15)
root.right.right = TreeNode.new(7)
p zigzag_level_order(root)

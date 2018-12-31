#
# @lc app=leetcode id=111 lang=ruby
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (34.51%)
# Total Accepted:    260.3K
# Total Submissions: 754K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its minimum depth = 2.
#
#
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
def min_depth(root)
  return 0 if root.nil?

  left = min_depth(root.left)
  right = min_depth(root.right)
  1 + (left.zero? || right.zero? ? left + right : [left, right].min)
end

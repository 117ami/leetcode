#
# @lc app=leetcode id=110 lang=ruby
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (39.89%)
# Total Accepted:    278.3K
# Total Submissions: 697.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# Return false.
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
# @return {Boolean}
def is_balanced(root)
  return true if root.nil?

  _depth = lambda do |r, d|
    return [true, d] if r.nil?

    lb, ld = _depth.call(r.left, d + 1)
    rb, rd = _depth.call(r.right, d + 1)
    return [lb && rb && (ld - rd).abs <= 1, [ld, rd].max]
  end
  _depth.call(root, 0).first
end

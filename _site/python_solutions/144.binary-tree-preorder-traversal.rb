#
# @lc app=leetcode id=144 lang=ruby
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (50.93%)
# Total Accepted:    326.1K
# Total Submissions: 639.9K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,2,3]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
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
# @return {Integer[]}
def preorder_traversal(root)
  return [] if root.nil?

  ans = []
  stack = [root]
  until stack.empty?
    e = stack.pop
    ans << e.val
    stack << e.right unless e.right.nil?
    stack << e.left unless e.left.nil?
  end
  ans
end

# p [2] + [3, 4]

#
# @lc app=leetcode id=965 lang=ruby
#
# [965] Univalued Binary Tree
#
# https://leetcode.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (77.53%)
# Total Accepted:    6K
# Total Submissions: 8.1K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# A binary tree is univalued if every node in the tree has the same value.
#
# Return true if and only if the given tree is univalued.
#
#
#
# Example 1:
#
#
# Input: [1,1,1,1,1,null,1]
# Output: true
#
#
#
# Example 2:
#
#
# Input: [2,2,2,5,2]
# Output: false
#
#
#
#
#
# Note:
#
#
# The number of nodes in the given tree will be in the range [1, 100].
# Each node's value will be an integer in the range [0, 99].
#
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
def is_unival_tree(root)
  helper = lambda do |r, v|
    return true if r.nil?
    return false if r.val != v

    helper.call(r.left, v) && helper.call(r.right, v)
  end
  return true if root.nil?

  helper.call(root, root.val)
end

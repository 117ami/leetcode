# Given a binary tree, return the postorder traversal of its nodes' values.
# Example:
# Input:[1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output:[3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#  https://leetcode.com/problems/binary-tree-postorder-traversal/description/
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
# @return {Integer[]}
def postorder_traversal(root)
  res = []
  helper = lambda do |r|
    return if r.nil?
    helper.call(r.left)
    helper.call(r.right)
    res << r.val
  end
  helper.call(root)
  res
end

def method2(root)
  res = []
  return res if root.nil?
  xtd = [root]
  until xtd.empty?
    node = xtd.pop
    next if node.nil?
    res << node.val
    xtd << node.left
    xtd << node.right
  end
  res.reverse
end

arr = [1, 2, 3, nil, 5, 6, 7]
tree = construct_tree(arr)
p tree
p postorder_traversal(tree)
p method2(tree)

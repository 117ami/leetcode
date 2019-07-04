# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Example:
# Input:[1,2,3,null,5,null,4]
# Output:[1, 3, 4]
# Explanation:
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#
#  https://leetcode.com/problems/binary-tree-right-side-view/
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
def right_side_view(root)
  res = []
  trav = lambda do |r, depth|
    return if r.nil?
    res[depth] = r.val
    trav.call(r.left, depth + 1)
    trav.call(r.right, depth + 1)
  end
  trav.call(root, 0)
  res
end

arr = [1, 2, 3, nil, 5, nil, 4]
root = construct_tree(arr)
p right_side_view(root)

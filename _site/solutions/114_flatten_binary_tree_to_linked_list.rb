# Given a binary tree, flatten it to a linked list in-place.
# For example, given the following tree:
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#
#  https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
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
# @return {Void} Do not return anything, modify root in-place instead.
def flatten2(root)
  return root if root.nil?
  helper = lambda do |r|
    return [nil, nil] if r.nil?
    return [r, r] if r.left.nil? && r.right.nil? # r is never nil
    cleft = helper.call(r.left)
    cright = helper.call(r.right)
    if r.left.nil?
      r.left = nil
      r.right = cright[0]
      return [r, cright.last]
    elsif r.right.nil?
      r.left = nil
      r.right = cleft[0]
      return [r, cleft.last]
    else
      r.left = nil
      cleft[-1].right = cright[0]
      r.right = cleft[0]
      return [r, cright[-1]]
    end
  end
  helper.call(root).first
end

def flatten(root)
  return unless root
  cleft = flatten(root.left)
  cright = flatten(root.right)
  root.left = nil
  root.right = cleft
  cur = root
  cur = cur.right while cur.right
  cur.right = cright
  root
end

arr = [1, 2, 5, 3, 4, nil, 6]
root = construct_tree(arr)
p root
p flatten2(root)
p flatten(root)

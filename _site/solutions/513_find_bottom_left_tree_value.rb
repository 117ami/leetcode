#  Given a binary tree, find the leftmost value in the last row of the tree.
#
# Example 1:
#
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
#
# Example 2:
#
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7
#
# Note: You may assume the tree (i.e., the given root node) is not NULL.

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
# @return {Integer}
def rec(root, depth)
  return [root.val, depth] if root.left.nil? && root.right.nil?
  return rec(root.left, depth + 1) if root.right.nil?
  return rec(root.right, depth + 1) if root.left.nil?
  lr = rec(root.left, depth + 1)
  rr = rec(root.right, depth + 1)
  return lr if lr[1] >= rr[1]
  rr
end

def find_bottom_left_value(root)
  rec(root, 0).first
end

root = TreeNode.new(1)
root.left = TreeNode.new(2)
root.right = TreeNode.new(3)
root.left.left = TreeNode.new(4)
root.right.left = TreeNode.new(5)
root.right.right = TreeNode.new(6)
root.right.left.left = TreeNode.new(7)

p find_bottom_left_value(root)

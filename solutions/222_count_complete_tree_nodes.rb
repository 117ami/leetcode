# Given a complete binary tree, count the number of nodes.
#
# Note:
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Example:
#
# Input:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# Output: 6

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
def count_nodes(root)
  return 0 if root.nil?
  ld = get_depth(root.left)
  rd = get_depth(root.right)
  return 2**ld + count_nodes(root.right) if ld == rd
  2**rd + count_nodes(root.left)
end

def get_depth(root)
  return 0 if root.nil?
  1 + get_depth(root.left)
end

root = TreeNode.new(1)
root.left = TreeNode.new(2)
root.right = TreeNode.new(3)

root.left.left = TreeNode.new(4)
root.left.right = TreeNode.new(5)
p count_nodes(root)

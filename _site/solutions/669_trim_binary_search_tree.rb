# Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

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
# @param {Integer} l
# @param {Integer} r
# @return {TreeNode}
def tree2list(root)
  return [] if root.nil?
  list = [root.val].push(*tree2list(root.left)).push(*tree2list(root.right))
end

def trim_bst(root, l, r)
  return root if root.nil?
  if root.val < l
    return trim_bst(root.right, l, r)
  elsif root.val > r
    return trim_bst(root.left, l, r)
  end
  root.left = trim_bst(root.left, l, r)
  root.right = trim_bst(root.right, l, r)
  root
end

root = TreeNode.new(3)
root.left = TreeNode.new(0)
root.right = TreeNode.new(4)
root.left.right = TreeNode.new(2)
root.left.right.left = TreeNode.new(1)

p trim_bst(root, 1, 3)

# Given a binary tree, return all root-to-leaf paths.
# Note:&nbsp;A leaf is a node with no children.
# Example:
# Input:
#    1
#  /   \
# 2     3
#  \
#   5
# Output: [&quot;1-&gt;2-&gt;5&quot;, &quot;1-&gt;3&quot;]
# Explanation: All root-to-leaf paths are: 1-&gt;2-&gt;5, 1-&gt;3
#

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
# @return {String[]}
def binary_tree_paths(root)
  return [] if root.nil?
  return [root.val.to_s] if root.left.nil? && root.right.nil?
  binary_tree_paths(root.left).concat(binary_tree_paths(root.right)).map { |path| "#{root.val}->" + path.to_s }
end

root = TreeNode.new(1)
root.left = TreeNode.new(2)
root.right = TreeNode.new(3)
root.left.right = TreeNode.new(5)
p binary_tree_paths(root)

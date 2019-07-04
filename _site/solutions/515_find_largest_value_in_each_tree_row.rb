# You need to find the largest value in each row of a binary tree.
# Input:
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
# Output: [1, 3, 9]
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
# @return {Integer[]}
def largest_values(root)
  ret = []
  traverse = lambda do |r, dep|
    return if r.nil?
    ret[dep] = [ret[dep] || -Float::INFINITY, r.val].max
    traverse.call(r.left, dep + 1)
    traverse.call(r.right, dep + 1)
  end
  traverse.call(root, 0)
  ret
end

root = TreeNode.new(1)
root.left = TreeNode.new(3)
root.left.left = TreeNode.new(5)
root.left.right = TreeNode.new(3)
root.right = TreeNode.new(2)
root.right.right = TreeNode.new(9)

p largest_values(root)

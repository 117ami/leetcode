# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.
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
# @return {Boolean}
def is_balanced(root)
  balanced = lambda do |r|
    return 0 if r.nil?
    da = balanced.call(r.left)
    db = balanced.call(r.right)
    (da - db).abs > 1 ? raise : 1 + [da, db].max
  end
  begin
    balanced.call(root) && true
  rescue StandardError
    false
  end
end

def assert(tree)
  return 0 unless tree
  left = assert(tree.left)
  right = assert(tree.right)
  (left - right).abs > 1 ? raise : 1 + [left, right].max
end

root = TreeNode.new(1)
root.left = TreeNode.new(2)
root.right = TreeNode.new(2)
root.left.left = TreeNode.new(3)
root.left.right = TreeNode.new(3)
root.left.left.left = TreeNode.new(4)
root.left.left.right = TreeNode.new(4)
root = nil
p is_balanced(root)
# p assert(root) && true rescue false

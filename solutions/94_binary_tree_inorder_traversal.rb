# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
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
# @return {Integer[]}
def inorder_traversal(root)
  return [] if root.nil?
  inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
end

def inorder_traversal2(root)
  return [] if root.nil?
  ans = []
  undone = [root]
  until undone.empty?
    x = undone.pop
    next if x.nil?
    if x.instance_of?(Integer)
      ans << x
    else
      undone.concat([x.right, x.val, x.left])
    end
  end
  ans
end

root = TreeNode.new(1)
root.right = TreeNode.new(2)
root.right.left = TreeNode.new(3)

p inorder_traversal(root)
p inorder_traversal2(root)

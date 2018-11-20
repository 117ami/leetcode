# Given a binary tree, return the preorder traversal of its nodes&#39; values.
# Example:
# Input:&nbsp;[1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output:&nbsp;[1,2,3]
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
def preorder_traversal(root)
  return [] unless root
  stack = [root]
  res = []
  until stack.empty?
    r = stack.pop
    next if r.nil?
    if r.instance_of?(TreeNode)
      stack.concat([r.right, r.left, r.val])
    else
      res << r
    end
  end
  res
end

require './leetcodes/parse_tree.rb'
arr = [1, 2, 5, 3, 4, nil, 6]
arr = [1, nil, 2, 3]
root = array2tree(arr)
p preorder_traversal(root)

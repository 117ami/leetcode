
# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.
#
# Example :
#
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
#
# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
# Note:
#
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.
# Discuss

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
def min_diff_in_bst(root)
  return 0 if root.nil?
  values = []
  rec = lambda do |tree|
    return if tree.nil?
    values << tree.val
    rec.call(tree.left)
    rec.call(tree.right)
  end
  rec.call(root)
  values.sort!
  r = 1_234_678_999
  (1..values.size - 1).each do |i|
    r = [r, values[i] - values[i - 1]].min
  end
  r
end

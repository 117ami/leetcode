# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
# Example 2:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False

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
# @param {Integer} k
# @return {Boolean}
def find_target(root, k)
  return false if root.nil?
  trees = [root]
  nums = []
  until trees.empty?
    t = trees.shift
    next if t.nil?
    nums << t.val
    trees << t.left
    trees << t.right
  end
  h = {}
  nums.each_with_index do |n, i|
    return true if h.key?(k - n)
    h[n] = i
  end
  false
end

# You are given a binary tree in which each node contains an integer value.
# Find the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
# Example:
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# Return 3. The paths that sum to 8 are:
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
#
# Definition for a binary tree node.
require './leetcodes/parse_tree.rb'

class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

# @param {TreeNode} root
# @param {Integer} sum
# @return {Integer}
def path_sum(root, sum)
  res = 0
  helper = lambda do |r, n|
    return 0 if r.nil?
    res += 1 if n == r.val
    helper.call(r.left, n - r.val)
    helper.call(r.right, n - r.val)
  end
  return 0 if root.nil?
  helper.call(root, sum)
  res += path_sum(root.left, sum)
  res += path_sum(root.right, sum)
end

root = [10, 5, -3, 3, 2, nil, 11, 3, -2, nil, 1]
root = [1, -2, -3, 1, 3, -2, nil, -1]
root = array2tree(root)
# p root
p path_sum(root, -1)

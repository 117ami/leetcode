# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
# Note: The length of path between two nodes is represented by the number of edges between them.
# Example 1:
# Input:
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
# 2
# Example 2:
# Input:
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
# 2
# Note:
# The given binary tree has not more than 10000 nodes.  The height of the tree is not more than 1000.
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
# @return {Integer}
def longest_univalue_path(root)
  return 0 if root.nil?
  helper = lambda do |r, n|
    return -1 if r.nil? || r.val != n
    return [helper.call(r.left, n), helper.call(r.right, n)].max + 1
  end
  xmax = 2 + helper.call(root.left, root.val) + helper.call(root.right, root.val)
  [longest_univalue_path(root.right), longest_univalue_path(root.left), xmax].max
end

def longest_univalue_path2(root)
  @xmax = 0
  univalue(root)
  @xmax
end

def univalue(r)
  return 0 if r.nil?
  a = univalue(r.left)
  b = univalue(r.right)
  a = r.left && r.left.val == r.val ? a + 1 : 0
  b = r.right && r.right.val == r.val ? b + 1 : 0
  @xmax = [@xmax, a + b].max
  [a, b].max
end

require './leetcodes/parse_tree.rb'
root = array2tree([5, 4, 5, 1, 1, nil, 5])
root = array2tree([1, 4, 5, 4, 3, nil, 5])
p longest_univalue_path(root)
p longest_univalue_path2(root)

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
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
# @return {Integer[][]}
def level_order(root)
  res = []
  helper = lambda do |r, d|
    return unless r
    if res[d].nil?
      res[d] = [r.val]
    else
      res[d] << r.val
    end
    helper.call(r.left, d + 1)
    helper.call(r.right, d + 1)
  end
  helper.call(root, 0)
  res
end

require './leetcodes/parse_tree.rb'
arr = [3, 9, 20, nil, nil, 15, 7]
arr = [0, 1, 2, 10, 11, 20, nil, 100, 101]
tree = array2tree(arr)
p level_order(tree)

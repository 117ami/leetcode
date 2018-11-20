# Given a binary tree and a sum, find all root-to-leaf paths where each path&#39;s sum equals the given sum.
# Note:&nbsp;A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
# [
#    [5,4,11,2],
#    [5,8,4,5]
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
# @param {Integer} sum
# @return {Integer[][]}
def path_sum(root, sum)
  helper = lambda do |r, n|
    return [[[], false]] if r.nil?
    if r.left.nil? && r.right.nil?
      return [[[r.val], true]] if r.val == n
      return [[[], false]]
    end
    helper.call(r.left, n - r.val).concat(helper.call(r.right, n - r.val)).select(&:last).map { |arr| [arr[0].unshift(r.val), arr[1]] }
  end
  helper.call(root, sum).map(&:first).reject(&:empty?)
end

root = TreeNode.new(5)
root.left = TreeNode.new(4)
root.left.left = TreeNode.new(11)
root.left.left.left = TreeNode.new(7)
root.left.left.right = TreeNode.new(2)
root.right = TreeNode.new(8)
root.right.left = TreeNode.new(13)
root.right.right = TreeNode.new(4)
root.right.right.left = TreeNode.new(5)
root.right.right.right = TreeNode.new(1)

root = nil
p path_sum(root, 200)

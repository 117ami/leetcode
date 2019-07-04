#
# Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
# Examples 1
# Input:
#   5
#  /  \
# 2   -3
# return [2, -3, 4], since all the values happen only once, return all of them in any order.
# Examples 2
# Input:
#   5
#  /  \
# 2   -5
# return [2], since 2 happens twice, however -5 only occur once.
# Note:
# You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
#
#  https://leetcode.com/problems/most-frequent-subtree-sum/description/

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
def find_frequent_tree_sum(root)
  freq = Hash.new(0)
  treesum = lambda do |r|
    return 0 if r.nil?
    xn = r.val + treesum.call(r.left) + treesum.call(r.right)
    freq[xn] += 1
    return xn
  end
  treesum.call(root)
  vmax = freq.values.max
  freq.keys.map { |k| freq[k] == vmax }
end

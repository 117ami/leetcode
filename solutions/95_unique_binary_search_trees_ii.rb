# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ...n.
# Example:
# Input: 3
# Output:
# [
#  [1,null,3,2],
#  [3,2,null,1],
#  [3,1,null,null,2],
#  [2,1,3],
#  [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#  https://leetcode.com/problems/unique-binary-search-trees-ii/description/
require './aux.rb'

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer} n
# @return {TreeNode[]}
def generate_trees(n)
  return [] if n.zero?
  arr = (1..n).to_a
  helper = lambda do |arr|
    return [nil] if arr.empty?
    return [TreeNode.new(arr.first)] if arr.size == 1
    res = []
    arr.each_with_index do |v, i|
      r = TreeNode.new(v)
      leftc = i.zero? ? [nil] : helper.call(arr[0..i - 1])
      rightc = i == arr.size - 1 ? [nil] : helper.call(arr[i + 1..-1])
      leftc.product(rightc).each do |pair|
        dupr = r.dup
        dupr.left = pair.first
        dupr.right = pair.last
        res << dupr
      end
    end
    res
  end
  helper.call(arr)
end

p generate_trees(3).size

x = [nil]
y = [3, 4, 4]
p x.product(y)

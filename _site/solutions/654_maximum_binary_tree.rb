# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
#     The root is the maximum number in the array.
#     The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
#     The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
#
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example 1:
#
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

# @param {Integer[]} nums
# @return {TreeNode}
def construct_maximum_binary_tree(nums)
  return nil if nums.empty?
  return TreeNode.new(nums[0]) if nums.size == 1
  maxnum, maxid = nums.each_with_index.max
  root = TreeNode.new(maxnum)
  root.left = construct_maximum_binary_tree(nums[0..maxid - 1]) if maxid > 0
  root.right = construct_maximum_binary_tree(nums[maxid + 1..nums.size - 1])
  root
end

nums = [3, 2, 1, 6, 0, 5]
p nums.each_with_index.max
p construct_maximum_binary_tree(nums)

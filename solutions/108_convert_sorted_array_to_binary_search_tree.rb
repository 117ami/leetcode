# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example:
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#  https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

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
def sorted_array_to_bst(nums)
  return nil if nums.empty?
  return TreeNode.new(nums.first) if nums.size == 1
  root = TreeNode.new(nums[nums.size / 2])
  root.left = sorted_array_to_bst(nums[0..nums.size / 2 - 1]) if nums.size / 2 >= 1
  root.right = sorted_array_to_bst(nums[nums.size / 2 + 1..-1])
  root
end

nums = [-10,-3,0,5,9]
p sorted_array_to_bst(nums)
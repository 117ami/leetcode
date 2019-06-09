#
# @lc app=leetcode id=129 lang=ruby
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (42.52%)
# Total Accepted:    186.2K
# Total Submissions: 437.3K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
# Example 2:
#
#
# Input: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer}
def sum_numbers(root)
  res = 0
  dfs = lambda do |prev, r|
    return if r.nil?

    curv = prev * 10 + r.val
    if r.left.nil? && r.right.nil?
      res += curv
      return
    end
    dfs.call(curv, r.left)
    dfs.call(curv, r.right)
  end
  dfs.call(0, root)
  res
end

def construct_tree(arr)
  root = TreeNode.new(arr.shift)
  xtd = [root]
  while !xtd.empty? && !arr.empty?
    cur_node = xtd.shift
    a, b = arr.shift(2) # doesn't matter if arr.size < 2. in this case, a, b might be nil
    cur_node.left = a.nil? ? nil : TreeNode.new(a)
    cur_node.right = b.nil? ? nil : TreeNode.new(b)
    xtd << cur_node.left unless cur_node.left.nil?
    xtd << cur_node.right unless cur_node.right.nil?
  end
  root
end

root = construct_tree([4, 9, 0, nil, 1])
p root
p sum_numbers(root)

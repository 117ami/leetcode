#
# @lc app=leetcode id=530 lang=ruby
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (49.19%)
# Total Accepted:    51.8K
# Total Submissions: 104.7K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
#
# Example:
#
#
# Input:
#
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
#
#
#
#
# Note: There are at least two nodes in this BST.
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
def get_minimum_difference(root)
  vs = []
  travel = lambda do |r|
    return if r.nil?

    vs << r.val
    travel.call(r.left)
    travel.call(r.right)
  end
  travel.call(root)
  vs.sort!
  0.upto(vs.size - 2).map { |i| vs[i + 1] - vs[i] }.min
end

#
# @lc app=leetcode id=1026 lang=ruby
#
# [1026] Maximum Difference Between Node and Ancestor
#
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
#
# algorithms
# Medium (56.72%)
# Total Accepted:    4.2K
# Total Submissions: 7.3K
# Testcase Example:  '[8,3,10,1,6,null,14,null,null,4,7,13]'
#
# Given the root of a binary tree, find the maximum value V for which there
# exists different nodes A and B where V = |A.val - B.val| and A is an ancestor
# of B.
#
# (A node A is an ancestor of B if either: any child of A is equal to B, or any
# child of A is an ancestor of B.)
#
#
#
# Example 1:
#
#
#
#
# Input: [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation:
# We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1|
# = 7.
#
#
#
#
# Note:
#
#
# The number of nodes in the tree is between 2 and 5000.
# Each node will have value between 0 and 100000.
#
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
def max_ancestor_diff(root)
  stack = [[root, root.val, root.val]]
  ans = 0
  until stack.empty?
    curnode, cmn, cmx = stack.pop
    stack << [curnode.left, [cmn, curnode.left.val].min, [cmx, curnode.left.val].max] if curnode.left
    stack << [curnode.right, [cmn, curnode.right.val].min, [cmx, curnode.right.val].max] if curnode.right
    ans = [cmx - cmn, ans].max if curnode.left.nil? && curnode.right.nil?
  end
  ans
end


#
# @lc app=leetcode id=968 lang=ruby
#
# [968] Binary Tree Cameras
#
# https://leetcode.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (34.96%)
# Total Accepted:    5.7K
# Total Submissions: 16.4K
# Testcase Example:  '[0,0,null,0,0]'
#
# Given a binary tree, we install cameras on the nodes of the tree. 
#
# Each camera at a node can monitor its parent, itself, and its immediate
# children.
#
# Calculate the minimum number of cameras needed to monitor all nodes of the
# tree.
#
#
#
# Example 1:
#
#
#
# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
#
#
# Example 2:
#
#
# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.
#
#
#
# Note:
#
#
# The number of nodes in the given tree will be in the range [1, 1000].
# Every node has value 0.
#
#
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

# require './aux.rb'

def min_camera_cover(root)
  res = 0
  dfs = lambda do |r|
    return 2 if r.nil?

    lv = dfs.call(r.left)
    rv = dfs.call(r.right)
    if lv * rv == 0
      res += 1
      return 1
    end
    return lv == 1 || rv == 1 ? 2 : 0
  end
  (dfs.call(root).zero? ? 1 : 0) + res
end

# tree = construct_tree([0, 0, nil, 0, nil, 0, nil, nil, 0])
# p tree
# p min_camera_cover(tree)

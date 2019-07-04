# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
# The encoded string should be as compact as possible.
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
#
#  https://leetcode.com/problems/serialize-and-deserialize-bst/description/
require './aux.rb'

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# Encodes a tree to a single string.
#
# @param {TreeNode} root
# @return {string}
def serialize(root)
	return "" if root.nil?
  res = []
  parse = lambda do |r, depth|
    if r.nil?
      res[depth] = (res[depth] || []) << nil
    else
      res[depth] = (res[depth] || []) << r.val
      parse.call(r.left, depth + 1)
      parse.call(r.right, depth + 1)
     end
  end
  parse.call(root, 0)
  res.flatten!
  res.pop until res.last
  res.join('#')
end

# Decodes your encoded data to tree.
#
# @param {string} data
# @return {TreeNode}
def deserialize(data)
	return nil if data.length.zero?
  arr = data.split('#').map { |i| i == '' ? nil : i.to_i }
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

# Your functions will be called as such:
# deserialize(serialize(data))

data = [2, 2, 2, 3, nil, 3].join('#')
p data
p deserialize(data)
p serialize(deserialize(data))
# p data.split("#").map{|i| i == "" ? nil : i.to_i}

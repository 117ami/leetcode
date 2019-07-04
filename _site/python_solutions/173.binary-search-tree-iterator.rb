#
# @lc app=leetcode id=173 lang=ruby
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (48.17%)
# Total Accepted:    199.7K
# Total Submissions: 414.1K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Note:
# 
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
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

class BSTIterator

=begin
    :type root: TreeNode
=end
    def initialize(root)
        @values = []
        traversal = lambda do |r|
            return if r.nil?
            @values << r.val 
            traversal.call(r.left)
            traversal.call(r.right)            
        end 
        traversal.call(root)

        @values.sort!
        @cter = -1
    end


=begin
    @return the next smallest number
    :rtype: Integer
=end
    def next()
        @cter += 1
        @values[@cter]
    end


=begin
    @return whether we have a next smallest number
    :rtype: Boolean
=end
    def has_next()
        @cter < @values.size - 1
    end

end

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator.new(root)

# param_1 = obj.next()
# param_2 = obj.has_next()

# require './aux.rb'
# root = construct_tree([7, 3, 15, 9, 20])
# obj = BSTIterator.new(root)
# p obj.next()
# require './aux.rb'
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end
class CBTInserter
  #     :type root: TreeNode
  def initialize(root)
    @root = root
    @stacks = []
    helper = lambda do |r, depth|
      return if r.nil?

      @stacks[depth] = [] if @stacks[depth].nil?
      @stacks[depth] << r
      helper.call(r.left, depth + 1)
      helper.call(r.right, depth + 1)
    end
    helper.call(root, 0)
    @stacks.flatten!
  end

  #     :type v: Integer
  #     :rtype: Integer
  def insert(v)
    @stacks.shift until @stacks.first.right.nil?
    t = @stacks.first
    @stacks << TreeNode.new(v)
    if t.left.nil?
      t.left = @stacks.last
    else
      t.right = @stacks.last
    end
    t.val
  end

  #     :rtype: TreeNode
  def get_root
    @root
  end
end
# Your CBTInserter object will be instantiated and called as such:
# root = construct_tree([1, 2, 3, 4])
# p CBTInserter.new(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
# [919] Complete Binary Tree Inserter
# https://leetcode.com/problems/complete-binary-tree-inserter/description/
# * algorithms
# * Medium (53.74%)
# * Total Accepted:    4.3K
# * Total Submissions: 8K
# * Testcase Example:  '["CBTInserter","insert","get_root"]\n[[[1]],[2],[]]'
# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
# Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:
#   CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
#   CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
#   CBTInserter.get_root() will return the head node of the tree.
# Example 1:
# Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# Output: [null,1,[1,2]]
# Example 2:
# Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
# Output: [null,3,4,[1,2,3,4,5,6,7,8]]
# Note:
#   The initial given tree is complete and contains between 1 and 1000 nodes.
#   CBTInserter.insert is called at most 10000 times per test case.
#   Every value of a given or inserted node is between 0 and 5000.

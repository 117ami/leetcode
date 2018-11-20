# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example:
# Given the sorted linked list: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#  https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

# @param {ListNode} head
# @return {TreeNode}
def sorted_list_to_bst(head)
  arr = []
  while head
    arr << head.val
    head = head.next
  end
  helper(arr)
end

def helper(arr)
  return nil if arr.empty?
  return TreeNode.new(arr.first) if arr.size == 1
  root = TreeNode.new(arr[arr.size / 2])
  root.left = helper(arr[0..arr.size / 2 - 1]) if arr.size / 2 >= 1
  root.right = helper(arr[arr.size / 2 + 1..-1])
  root
end

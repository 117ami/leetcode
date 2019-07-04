# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  arr = (helper(l1) + helper(l2)).to_s.each_char.map { |i| ListNode.new(i) }
  arr.each_with_index { |node, i| node.next = arr[i + 1] }
  arr.first
end

def helper(head)
  res = head.val
  res = res * 10 + head.val while head && (head = head.next)
  res
end

require './tools.rb'
l1 = array_linklist([7, 2, 4, 3])
l2 = array_linklist([5, 6, 4])
p add_two_numbers(l1, l2)

#!/usr/bin/ruby -w

# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode[]} lists
# @return {ListNode}
def merge_k_lists(lists)
  return nil if lists.empty?
  arr = []
  lists.each do |head|
    while head
      arr.push(head.val)
      head = head.next
    end
  end

  dummy = head = ListNode.new(nil)
  return head if arr.sort!.empty?
  arr.each do |i|
    head.next = ListNode.new(i)
    head = head.next
  end
  dummy.next
end

h = ListNode.new(0)
p merge_k_lists([])

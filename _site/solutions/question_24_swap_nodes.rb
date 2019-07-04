#!/usr/bin/ruby -w
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
# =

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} head
# @return {ListNode}
def swap_pairs(head)
  return head if head.nil?
  newhead = head.next ? head.next : head
  cur = head
  head = ListNode.new(0)

  until cur.nil? || cur.next.nil?
    head.next = cur.next
    suc = cur.next
    cur.next = suc.next
    suc.next = cur
    head = cur
    cur = cur.next
  end
  newhead
end

head = ListNode.new(1)
tmp = head
(2..10).each do |i|
  tmp.next = ListNode.new(i)
  tmp = tmp.next
end
swap_pairs(head)

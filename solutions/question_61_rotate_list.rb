# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# Example:
#
# Given 1->2->3->4->5->NULL and k = 2,
#
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def rotate_right(head, k)
  return head if head.nil? || k.zero?
  r = []
  until head.nil?
    r << head.val
    head = head.next
  end
  k = k % r.size
  k.times { r.unshift(r.pop) }

  dummy = head = ListNode.new(r[0])
  r[1..-1].each do |v|
    dummy.next = ListNode.new(v)
    dummy = dummy.next
  end
  head
end

head = ListNode.new(1)
head.next = ListNode.new(2)
head.next.next = ListNode.new(3)
head.next.next.next = ListNode.new(4)
head.next.next.next.next = ListNode.new(5)

p rotate_right(head, 2)

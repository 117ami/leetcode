# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} head
# @param {Integer} x
# @return {ListNode}
def partition(head, x)
  arr = []
  while head
    arr << head.val
    head = head.next
  end

  arr.dup.each_with_index do |v, i|
    if v >= x
      arr[i] = '*'
      arr.push(v)
    end
  end

  dummy = head = ListNode.new(nil)
  arr.each do |v|
    next if v == '*'
    dummy.next = ListNode.new(v)
    dummy = dummy.next
  end
  head.next
end

h = ListNode.new(1)
h.next = ListNode.new(4)
h.next.next = ListNode.new(3)
h.next.next.next = ListNode.new(2)
h.next.next.next.next = ListNode.new(5)
h.next.next.next.next.next = ListNode.new(2)
p partition(h, 3)

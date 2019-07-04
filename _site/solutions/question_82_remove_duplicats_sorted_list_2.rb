
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

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
def delete_duplicates(head)
  r = Hash.new(0)
  while head
    r[head.val] += 1
    head = head.next
  end

  head = dummy = ListNode.new(-1)

  r.each_pair do |k, v|
    next if v > 1
    head.next = ListNode.new(k)
    head = head.next
  end
  dummy.next
end

list = ListNode.new(1)
list.next = ListNode.new(1)
list.next.next = ListNode.new(1)
list.next.next.next = ListNode.new(2)
list.next.next.next.next = ListNode.new(2)
list.next.next.next.next.next = ListNode.new(3)

p delete_duplicates(list)

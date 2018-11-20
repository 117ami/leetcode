# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

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
  return head unless head && head.next
  dummy = ListNode.new(-1)
  dummy.next = head
  seen = head.val
  until head.nil? || head.next.nil?
    if seen == head.next.val
      head.next = head.next.next
    else
      seen = head.next.val
      head = head.next
    end
  end
  dummy.next
end

h = ListNode.new(1)
h.next = ListNode.new(1)
h.next.next = ListNode.new(1)
h.next.next.next = ListNode.new(1)
h.next.next.next.next = ListNode.new(1)
p delete_duplicates(h)

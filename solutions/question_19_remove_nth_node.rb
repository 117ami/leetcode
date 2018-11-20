
# Given a linked list, remove the nth node from the end of list and return its head.
# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note: Given n will always be valid. Try to do this in one pass.
# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} head
# @param {Integer} n
# @return {ListNode}
def list_to_array(head)
  nodes = []
  while head
    nodes.push(head)
    head = head.next
  end
  nodes
end

def remove_nth_from_end(head, n)
  nodes = list_to_array(head)
  case n
  when nodes.size
    return nodes[1]
  when 1
    nodes[-2].next = nil
  else
    nodes[-n - 1].next = nodes[-n + 1]
  end
  nodes[0]
end

head = ListNode.new(1)
tmp = ListNode.new(2)
head.next = tmp
(3..5).each do |i|
  tmp.next = ListNode.new(i)
  tmp = tmp.next
end

p remove_nth_from_end(head, 1)

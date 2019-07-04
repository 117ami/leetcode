
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# You may not alter the values in the nodes, only nodes itself may be changed.
#
# Only constant memory is allowed.
#
# For example,
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5

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
def reverse_k_group(head, k)
  return head if k <= 1 || head.nil?
  nodes = []
  while head
    nodes << head
    head = head.next
  end
  return nodes[0] if k > nodes.size
  i = 0
  dummy = head = ListNode.new(nil)
  while (i + 1) * k <= nodes.size
    Array(i * k..(i + 1) * k - 1).reverse.each do |j|
      head.next = nodes[j]
      head = head.next
    end
    i += 1
  end
  j = i * k
  while j < nodes.size
    head.next = nodes[j]
    head = head.next
    j += 1
  end
  dummy.next
end

def reverse2(head, k)
  swap = lambda do |first, last|
    prev = last
    while first != last         # Last.prev.next is still last
      tmp = first.next
      first.next = prev
      prev = first
      first = tmp
    end
    prev
  end

  node = head
  (1..k).each do |_i|
    return head unless node     # List is too short
    node = node.next
  end

  new_head = swap.call(head, node)
  head.next = reverse2(node, k)
  new_head
end

n1 = ListNode.new(1)
n1.next = ListNode.new(2)
n1.next.next = ListNode.new(3)
n1.next.next.next = ListNode.new(4)

# p reverse_k_group(n1, 4)
p reverse2(n1, 3)

# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# Note:
#   The relative order inside both the even and odd groups should remain as it was in the input.
#   The first node is considered odd, the second node even and so on ...
#
#  https://leetcode.com/problems/odd-even-linked-list/description/
require './aux.rb'

# @param {ListNode} head
# @return {ListNode}
def odd_even_list(head)
  a, b, c = reccur(head)
  return nil if a.nil?
  b.next = c
  a
end

def reccur(head)
  return [nil, nil, nil] if head.nil?
  return [head, head, nil] if head.next.nil?

  na = head
  nb = head.next
  return [na, na, nb] if nb.next.nil?

  mh, mt, mnh = reccur(nb.next)
  na.next = mh
  nb.next = mnh
  [na, mt, nb]
end

head = arr2list([2, 1, 3, 5, 6, 4, 7])
head = arr2list([1, 2, 3])
p odd_even_list(head)

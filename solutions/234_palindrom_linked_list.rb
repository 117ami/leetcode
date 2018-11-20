require 'pp'
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
#
# Example 2:
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} head
# @return {Boolean}
def is_palindrome(head)
  slow = fast = head
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end

  node = nil
  while slow
    nxt = slow.next
    slow.next = node
    node = slow
    slow = nxt
  end

  while node
    return false unless node.val == head.val
    node = node.next
    head = head.next
  end
  true
end

head = ListNode.new(1)
head.next = ListNode.new(2)
head.next.next = ListNode.new(3)
head.next.next.next = ListNode.new(1)
# head.next.next.next.next = ListNode.new(1)
p is_palindrome(head)

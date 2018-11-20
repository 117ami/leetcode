# Remove all elements from a linked list of integers that have value val.
# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#

require './tools.rb'

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} head
# @param {Integer} val
# @return {ListNode}
def remove_elements(head, val)
  head = head.next while head && head.val == val 
  dummy = head
  while dummy
    dummy.next = dummy.next.next while dummy.next && dummy.next.val == val
    dummy = dummy.next
  end
  head
end

arr = [6, 1, 2, 6, 6, 6, 6, 3, 4, 5, 6, 6, 6]
head = array_linklist(arr)
h = remove_elements(head, 6)
print_linklist(h)

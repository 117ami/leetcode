# Definition for singly-linked list.
require './aux.rb'

# @param {ListNode} head
# @return {Void} Do not return anything, modify head in-place instead.
def reorder_list(head)
  return if head.nil? || head.next.nil?
  slow = head
  fast = head.next
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end

  h2 = slow.next
  slow.next = nil

  cur = h2.next
  h2.next = nil
  while cur
    slow = cur.next
    cur.next = h2
    h2 = cur
    cur = slow
  end

  dm = head
  while dm
    t = dm.next
    dm.next = h2
    dm = dm.next
    h2 = t
  end
  list2arr(head)
end

arr = (1..5).to_a
head = arr2list(arr)
p reorder_list(head)


# You are given two non-empty linked lists representing two non-negative
#  integers. The digits are stored in reverse order and each of their nodes
#  contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the
#  number 0 itself.

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
# return the value of list
def value(list)
  v = 0
  base = 1
  while list
    v += base * list.val.to_i
    base *= 10
    list = list.next
  end
  v
end

def add_two_numbers(l1, l2)
  su = value(l1) + value(l2)
  arr = su.to_s.reverse.split('')
  res = ListNode.new(arr[0])
  head = res

  arr[1..-1].each do |v|
    head.next = ListNode.new(v.to_i)
    head = head.next
  end

  res
end

l1 = ListNode.new(2)
l1.next = ListNode.new(4)
l1.next.next = ListNode.new(3)

l2 = ListNode.new(5)
l2.next = ListNode.new(6)
l2.next.next = ListNode.new(4)

add_two_numbers(l1, l2)

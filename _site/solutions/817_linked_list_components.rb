
# We are given head, the head node of a linked list containing unique integer values.
#
# We are also given the list G, a subset of the values in the linked list.
#
# Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.
#
# Example 1:
#
# Input:
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2
# Explanation:
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
# Example 2:
#
# Input:
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# Output: 2
# Explanation:
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
# Note:
#
# If N is the length of the linked list given by head, 1 <= N <= 10000.
# The value of each node in the linked list will be in the range [0, N - 1].
# 1 <= G.length <= 10000.
# G is a subset of all values in the linked list.

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} head
# @param {Integer[]} g
# @return {Integer}
def num_components(head, g)
  items = []
  until head.nil?
    items << head.val
    head = head.next
  end

  ret = 0
  vvs = g.zip([]).to_h
  flag = false
  items.each do |i|
    if vvs.key?(i)
      flag = true
      vvs.delete(i)
    else
      ret += 1 if flag
      flag = false
    end
  end
  ret += 1 if flag
  ret
end

head = ListNode.new(0)
head.next = ListNode.new(1)
head.next.next = ListNode.new(2)
head.next.next.next = ListNode.new(3)
head.next.next.next.next = ListNode.new(4)

g = [0, 3, 1, 4]
p num_components(head, g)

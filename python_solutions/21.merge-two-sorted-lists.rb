#
# @lc app=leetcode id=21 lang=ruby
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (44.65%)
# Total Accepted:    465.6K
# Total Submissions: 1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#
#
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
def merge_two_lists(l1, l2)
  res = prev = ListNode.new(0)
  while l1 && l2
    l1, l2 = l2, l1 if l1.val > l2.val
    prev.next = l1
    prev = prev.next
    l1 = l1.next
  end
  prev.next = l1 || l2 
  res.next 
end

#
# @lc app=leetcode id=21 lang=python
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
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		res = prev = ListNode(0)
		while l1 and l2:
			if l1.val > l2.val:
				prev.next = l2
				l2 = l2.next
			else:
				prev.next = l1
				l1 = l1.next 
			prev = prev.next 

		prev.next = l1 or l2
		return res.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# from pprint import pprint
# res = Solution().mergeTwoLists(l1, l2)
# print(res.next.val)



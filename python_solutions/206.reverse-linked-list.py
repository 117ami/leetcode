#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (55.31%)
# Total Accepted:    616.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
#
#
# Definition for singly-linked list.
from pprint import pprint


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def arr2linkedlist(arr):
    if len(arr) == 0:
        return
    head = ListNode(arr[0])
    tail = head
    for i in arr[1:]:
        tail.next = ListNode(i)
        tail = tail.next
    return head


def linkedlist2arr(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans


class Solution:
    def reverseList(self, head):
        if not head:
            return head
        pre = head
        head = head.next
        pre.next = None
        while head is not None:
            cur = head.next
            head.next = pre
            pre = head
            head = cur
        return pre


s = Solution()
arr = [1, 2, 3, 4, 5]
head = arr2linkedlist(arr)
head = s.reverseList(head)
print(linkedlist2arr(head))

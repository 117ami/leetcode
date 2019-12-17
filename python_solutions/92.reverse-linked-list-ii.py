#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (36.70%)
# Total Accepted:    229.5K
# Total Submissions: 625.3K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        pre = dummy
        for _ in range(m - 1): pre = pre.next 
        cur = pre.next 
        tail = None 
        for _ in range(n-m+1):
            nxt = cur.next 
            cur.next = tail 
            tail = cur 
            cur = nxt 
        pre.next.next = cur 
        pre.next = tail 
        return dummy.next 

# s = Solution()
# from aux import *

# arr = [1,2,3,4,5]
# head = arr2linkedlist(arr)
# res = s.reverseBetween(head, 2, 4)
# arr = linkedlist2arr(res)
# print(arr)



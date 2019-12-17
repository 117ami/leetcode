#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (52.16%)
# Total Accepted:    120.2K
# Total Submissions: 230.4K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_value(self, tmp: ListNode) -> int:
        res = 0
        head = tmp
        while head:
            res = res * 10 + head.val 
            head = head.next 
        return res 

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        vs = [int(i) for i in  list(str(self.get_value(l1) + self.get_value(l2)))]
        head = ListNode(vs[0])
        tmp = head
        for i in vs[1:]:
            tmp.next = ListNode(i)
            tmp = tmp.next 
        return head 
        

# if __name__ == "__main__":
#     from aux import * 
#     l1 = arr2linkedlist([7,2,4,3])        
#     l2 = arr2linkedlist([5,6,4])        
#     s = Solution()
#     print(linkedlist2arr(s.addTwoNumbers(l1, l2)))



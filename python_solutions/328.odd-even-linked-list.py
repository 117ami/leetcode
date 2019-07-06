#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (49.53%)
# Total Accepted:    153K
# Total Submissions: 308.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# 
# 
# Example 2:
# 
# 
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# 
# 
# Note:
# 
# 
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...
# 
# 
#
# Definition for singly-linked list.
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
    cnt = 0
    while head:
        ans.append(head.val)
        # print(head.val)        
        head = head.next
        # cnt += 1
        # if cnt>10: break
    return ans


class Solution:
    def oddEvenList(self, head):
    	if not head: return head
    	odd = head
    	even = head.next
    	evenhead = even
    	while even and even.next:
    		odd.next = even.next
    		odd = even.next
    		even.next = odd.next
    		even = odd.next
    	odd.next = evenhead
    	return head


# s = Solution()
# arr = [2,1,3,5,6,4,7]
# head = arr2linkedlist(arr)
# newhead = s.oddEvenList(head)
# newhead = head
# print(linkedlist2arr(newhead))



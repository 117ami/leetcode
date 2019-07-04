from collections import OrderedDict
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = OrderedDict()
        while head:
            v = head.val
            r[v] = r[v] + 1 if v in r else 1
            head = head.next

        dummy = head = ListNode(-1)
        for k, v in r.items():
            if v == 1:
                head.next = ListNode(k)
                head = head.next
        return dummy.next

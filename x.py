from collections import Counter

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        dummy = head 
        while dummy:
            dummy = dummy.next 
            n += 1 
        n = n // 2 
        dummy = head
        while n > 0:
            dummy = dummy.next 
            n -= 1
        return dummy
        
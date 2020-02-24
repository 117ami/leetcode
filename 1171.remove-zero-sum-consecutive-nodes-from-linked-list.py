from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/
#
# algorithms
# Medium (41.69%)
# Total Accepted:    10.8K
# Total Submissions: 25.8K
# Testcase Example:  '[1,2,-3,3,1]'
#
# Given the head of a linked list, we repeatedly delete consecutive sequences
# of nodes that sum to 0 until there are no such sequences.
#
# After doing so, return the head of the final linked list.  You may return any
# such answer.
#
#
# (Note that in the examples below, all sequences are serializations of
# ListNode objects.)
#
# Example 1:
#
#
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
#
#
# Example 3:
#
#
# Input: head = [1,2,3,-3,-2]
# Output: [1]
#
#
#
# Constraints:
#
#
# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.
#
#
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def linkedlist2arr(self, head):
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans

    def arr2linkedlist(self, arr):
        if len(arr) == 0:
            return
        head = ListNode(arr[0])
        tail = head
        for i in arr[1:]:
            tail.next = ListNode(i)
            tail = tail.next
        return head

    def removeZeroSumSublists(self, head):
        arr = self.linkedlist2arr(head)
        seen = set([0])
        st = [0]
        for i, n in enumerate(arr):
            cur = n + st[-1]
            # print(i, n, cur, st)
            if cur in seen:
                while st and st[-1] != cur:
                    seen.remove(st[-1])
                    st.pop()
            else:
                seen.add(cur)
                st.append(cur)
        st.pop(0)
        print(st)
        for i in range(len(st) - 1, 0, -1):
            st[i] -= st[i - 1]

        return self.arr2linkedlist(st)


sol = Solution()
arr = [1, 2, 3, -3, 4]
# arr = [1,2,-3,3,1]
# arr = [1,2,3,-3,-2]
head = sol.arr2linkedlist(arr)
print(sol.removeZeroSumSublists(head))

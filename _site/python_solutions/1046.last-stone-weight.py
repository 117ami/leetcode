#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
# https://leetcode.com/problems/last-stone-weight/description/
#
# algorithms
# Easy (64.22%)
# Total Accepted:    5.1K
# Total Submissions: 7.9K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# We have a collection of rocks, each rock has a positive integer weight.
#
# Each turn, we choose the two heaviest rocks and smash them together.  Suppose
# the stones have weights x and y with x <= y.  The result of this smash
# is:
#
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of
# weight y has new weight y-x.
#
#
# At the end, there is at most 1 stone left.  Return the weight of this stone
# (or 0 if there are no stones left.)
#
#
#
# Example 1:
#
#
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the
# value of last stone.
#
#
#
# Note:
#
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
#
#

from bisect import bisect_left


class PriorityQueue(object):
    def __init__(self, li=[]):
        self.queue = []
        for i in li:
            self.push(i)

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for return the size of queue
    def size(self):
        return len(self.queue)

    # for inserting an element in the queue
    def push(self, data):
        insert_idx = bisect_left(self.queue, data)
        self.queue.insert(insert_idx, data)

    # for popping an element based on Priority
    def pop(self):
        return self.queue.pop()


class Solution:
    def lastStoneWeight(self, stones):
        pq = PriorityQueue(stones)

        while pq.size() > 1:
            pq.push(pq.pop() - pq.pop())

        return 0 if pq.isEmpty() else pq.queue[0]


s = Solution()
stones = [2, 7, 4, 1, 8, 1]
print(s.lastStoneWeight(stones))

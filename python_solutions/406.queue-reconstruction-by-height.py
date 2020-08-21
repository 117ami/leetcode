from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import heapq 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (63.47%)
# Total Accepted:    121.1K
# Total Submissions: 189K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
# 
# Note:
# The number of people is less than 1,100.
# 
# 
# Example
# 
# 
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# 
# 
# 
#
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda e: (-e[0], e[1]) )
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

sol = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(sol.reconstructQueue(people))


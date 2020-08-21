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
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/
#
# algorithms
# Easy (86.29%)
# Total Accepted:    7.8K
# Total Submissions: 9K
# Testcase Example:  '[1,2,3]\n[3,2,7]\n4'
#
# Given two integer arrays startTime and endTime and given an integer
# queryTime.
# 
# The ith student started doing their homework at the time startTime[i] and
# finished it at time endTime[i].
# 
# Return the number of students doing their homework at time queryTime. More
# formally, return the number of students where queryTime lays in the interval
# [startTime[i], endTime[i]] inclusive.
# 
# 
# Example 1:
# 
# 
# Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# Output: 1
# Explanation: We have 3 students where:
# The first student started doing homework at time 1 and finished at time 3 and
# wasn't doing anything at time 4.
# The second student started doing homework at time 2 and finished at time 2
# and also wasn't doing anything at time 4.
# The third student started doing homework at time 3 and finished at time 7 and
# was the only student doing homework at time 4.
# 
# 
# Example 2:
# 
# 
# Input: startTime = [4], endTime = [4], queryTime = 4
# Output: 1
# Explanation: The only student was doing their homework at the queryTime.
# 
# 
# Example 3:
# 
# 
# Input: startTime = [4], endTime = [4], queryTime = 5
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
# Output: 0
# 
# 
# Example 5:
# 
# 
# Input: startTime = [9,8,7,6,5,4,3,2,1], endTime =
# [10,10,10,10,10,10,10,10,10], queryTime = 5
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# startTime.length == endTime.length
# 1 <= startTime.length <= 100
# 1 <= startTime[i] <= endTime[i] <= 1000
# 1 <= queryTime <= 1000
# 
# 
#
class Solution:
    def busyStudent(self, st, et, q):
        return sum(1 for s, e in zip(st, et) if s <= q <= e)
        
sol = Solution()
st, et, q = [9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5
print(sol.busyStudent(st,et,q))


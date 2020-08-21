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
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (41.64%)
# Total Accepted:    369K
# Total Submissions: 884.9K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
#
#
#
# Constraints:
#
#
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input
# prerequisites.
# 1 <= numCourses <= 10^5
#
#
#


class Solution:
    def canFinish(self, n, pre):
        depends = defaultdict(list)
        for a, b in pre:
            depends[a].append(b)
        visited = [0] * n

        def dfs(k):
            if visited[k] == -1:
                return False
            if visited[k] == 1:
                return True
            visited[k] = -1
            for v in depends.get(k, []):
                if not dfs(v):
                    return False
            visited[k] = 1
            return True

        return all(dfs(i) for i in range(n))


sol = Solution()
arr = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
arr = [[0, 1], [3, 1], [1, 3], [3, 2]]
print(sol.canFinish(4, arr))

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
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007
#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (39.65%)
# Total Accepted:    261.2K
# Total Submissions: 657.3K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
#
# Example 1:
#
#
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished
# course 0. So the correct course order is [0,1] .
#
# Example 2:
#
#
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
#
# Note:
#
#
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
#
#
#


def kahn(graph, indegree):
    '''Kahn's topological sorting algorithm, https://bit.ly/2zVkzK4 .
    Parammeters:
    - graph, Adjacency matrix representing a graph
    - indegree, the number of edges directed into a vertex
    '''
    sorted_nodes = []
    stack = [node for node in range(len(graph)) if indegree[node] == 0]
    while stack:
        u = stack.pop()
        sorted_nodes.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                stack.append(v)

    """ If the graph is a DAG, a solution will be contained in the list sorted_nodes.
    Otherwise, the graph must have at least one cycle and therefore a topological sort
    is impossible."""

    return sorted_nodes if len(sorted_nodes) == len(graph) else []


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        sn = kahn(graph, indegree)
        return sn[::-1]


sol = Solution()
n, p = 2, [[1, 0]]
# n, p =   4, [[1,0],[2,0],[3,1],[3,2], [0,3]]
print(sol.findOrder(n, p))

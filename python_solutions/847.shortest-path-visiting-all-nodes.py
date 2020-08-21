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
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/
#
# algorithms
# Hard (52.03%)
# Total Accepted:    16.7K
# Total Submissions: 32.2K
# Testcase Example:  '[[1,2,3],[0],[0],[0]]'
#
# An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is
# given as graph.
#
# graph.length = N, and j != i is in the list graph[i] exactly once, if and
# only if nodes i and j are connected.
#
# Return the length of the shortest path that visits every node. You may start
# and stop at any node, you may revisit nodes multiple times, and you may reuse
# edges.
#
#
#
#
#
#
# Example 1:
#
#
# Input: [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
#
# Example 2:
#
#
# Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
#
#
#
#
# Note:
#
#
# 1 <= graph.length <= 12
# 0 <= graph[i].length < graph.length
#
#
#
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        mask = list(map(lambda i: 1 << i, range(N)))
        final_status = (1 << N) - 1
        queue = deque((i, mask[i]) for i in range(N))
        steps = 0

        # Store visited status not node cause nodes can be revisited.
        # E.g., (0, {1111})
        cc = [{mask[i]} for i in range(N)]

        while queue:
            for _ in range(len(queue)):
                i, cur_status = queue.popleft()
                if cur_status == final_status:
                    return steps

                for suc in graph[i]:
                    next_status = cur_status | mask[suc]
                    if next_status == final_status:
                        return steps + 1
                    if next_status not in cc[suc]:
                        cc[suc].add(next_status)
                        queue.append((suc, next_status))
            steps += 1
        return math.inf


sol = Solution()

inputs = [[1, 2, 3], [0], [0], [0]]
inputs = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
print(sol.shortestPathLength(inputs))

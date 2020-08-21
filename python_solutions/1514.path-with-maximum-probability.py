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
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#
# https://leetcode.com/problems/path-with-maximum-probability/description/
#
# algorithms
# Medium (36.48%)
# Total Accepted:    10.3K
# Total Submissions: 28.3K
# Testcase Example:  '3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.2]\n0\n2'
#
# You are given an undirected weighted graph of n nodes (0-indexed),
# represented by an edge list where edges[i] = [a, b] is an undirected edge
# connecting the nodes a and b with a probability of success of traversing that
# edge succProb[i].
#
# Given two nodes start and end, find the path with the maximum probability of
# success to go from start to end and return its success probability.
#
# If there is no path from start to end, return 0. Your answer will be accepted
# if it differs from the correct answer by at most 1e-5.
#
#
# Example 1:
#
#
#
#
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start =
# 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability
# of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
#
#
# Example 2:
#
#
#
#
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start =
# 0, end = 2
# Output: 0.30000
#
#
# Example 3:
#
#
#
#
# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.
#
#
#
# Constraints:
#
#
# 2 <= n <= 10^4
# 0 <= start, end < n
# start != end
# 0 <= a, b < n
# a != b
# 0 <= succProb.length == edges.length <= 2*10^4
# 0 <= succProb[i] <= 1
# There is at most one edge between every two nodes.
#
#


class Solution:
    def maxProbability(self,
                       n: int,
                       edges: List[List[int]],
                       succProb: List[float],
                       start: int,
                       end: int) -> float:
        g = [[] for _ in range(n)]
        for (a, b), prob in zip(edges, succProb):
            g[a].append((b, prob))
            g[b].append((a, prob))

        # Negative prob to change minheap to maxheap  
        heap = [(-1, start)]
        visited = [False] * n
        while heap:
            prob, node = heapq.heappop(heap)
            if node == end:
                return -prob
            if not visited[node]:
                visited[node] = True
                for nx_node, trans_prob in g[node]:
                    if not visited[nx_node]:
                        nx_prob = prob * trans_prob
                        heapq.heappush(heap, (nx_prob, nx_node))
        return 0


sol = Solution()


# n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0,
# end = 2
n, edges, succProb, start, end = 3, [
    [0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2
# n = 3; edges = [[0,1]]; succProb = [0.5]; start = 0; end = 2
print(sol.maxProbability(n, edges, succProb, start, end))

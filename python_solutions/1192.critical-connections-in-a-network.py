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
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (48.72%)
# Total Accepted:    50.4K
# Total Submissions: 103.3K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n-1 connected by undirected
# server-to-server connections forming a network where connections[i] = [a, b]
# represents a connection between servers a and b. Any server can reach any
# other server directly or indirectly through the network.
#
# A critical connection is a connection that, if removed, will make some server
# unable to reach some other server.
#
# Return all critical connections in the network in any order.
#
#
# Example 1:
#
#
#
#
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.
#
#
#


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        N = len(connections)
        lev = [None] * N
        low = [None] * N

        @lru_cache(None)
        def dfs(node, par, level):
            # already visited
            if lev[node] is not None:
                return

            lev[node] = low[node] = level
            for nei in g[node]:
                if not lev[nei]:
                    dfs(nei, node, level + 1)

            # minimal level in the neignbors, exclude the parent
            cur = min([level] + [low[nei] for nei in g[node] if nei != par])
            low[node] = cur
            # print(low, lev)

        dfs(0, None, 0)

        return [[u, v] for u, v in connections if low[u] > lev[v] or low[v] > lev[u]]


sol = Solution()
print(sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))

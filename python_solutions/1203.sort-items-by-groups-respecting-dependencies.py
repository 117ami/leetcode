import collections
from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache, cmp_to_key
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1203 lang=python3
#
# [1203] Sort Items by Groups anspecting Dependencies
#
# https://leetcode.com/problems/sort-items-by-groups-anspecting-dependencies/description/
#
# algorithms
# Hard (47.11%)
# Total Accepted:    5.3K
# Total Submissions: 11.4K
# Testcase Example:  '8\n2\n[-1,-1,1,0,0,1,0,-1]\n[[],[6],[5],[6],[3,6],[],[],[]]'
#
# There are n items each belonging to zero or one of m groups where group[i] is
# the group that the i-th item belongs to and it's equal to -1 if the i-th item
# belongs to no group. The items and the groups are zero indexed. A group can
# have no item belonging to it.
#
# Return a sorted list of the items such that:
#
#
# The items that belong to the same group are next to each other in the sorted
# list.
# There are some relations between these items where beforeItems[i] is a list
# containing all the items that should come before the i-th item in the sorted
# array (to the left of the i-th item).
#
#
# Return any solution if there is more than one solution and return an empty
# list if there is no solution.
#
#
# Example 1:
#
#
#
#
# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3,6],[],[],[]]
# Output: [6,3,4,1,5,2,0,7]
#
#
# Example 2:
#
#
# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3],[],[4],[]]
# Output: []
# Explanation: This is the same as example 1 except that 4 needs to be before 6
# in the sorted list.
#
#
#
# Constraints:
#
#
# 1 <= m <= n <= 3*10^4
# group.length == beforeItems.length == n
# -1 <= group[i] <= m-1
# 0 <= beforeItems[i].length <= n-1
# 0 <= beforeItems[i][j] <= n-1
# i != beforeItems[i][j]
# beforeItems[i] does not contain duplicates elements.
#
#
#


class Solution:
    def sortItems(self,
                  n: int,
                  m: int,
                  group: List[int],
                  beforeItems: List[List[int]]) -> List[int]:

        # Helper function: returns topological order of a graph, if it exists.
        def topological_sort(graph, indegree):
            list_sorted = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                v = stack.pop()
                list_sorted.append(v)
                for u in graph[v]:
                    indegree[u] -= 1
                    if indegree[u] == 0:
                        stack.append(u)
            return list_sorted if len(list_sorted) == len(graph) else []

        # STEP 1: Create a new group for each item that belongs to no group.
        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m += 1

        # STEP 2: Build directed graphs for items and groups.
        graph_items = [[] for _ in range(n)]
        indegree_items = [0] * n
        graph_groups = [[] for _ in range(m)]
        indegree_groups = [0] * m
        for u in range(n):
            for v in beforeItems[u]:
                graph_items[v].append(u)
                indegree_items[u] += 1
                if group[u] != group[v]:
                    graph_groups[group[v]].append(group[u])
                    indegree_groups[group[u]] += 1

        # STEP 3: Find topological orders of items and groups.
        item_order = topological_sort(graph_items, indegree_items)
        group_order = topological_sort(graph_groups, indegree_groups)
        if not item_order or not group_order:
            return []

        # STEP 4: Find order of items within each group.
        order_within_group = collections.defaultdict(list)
        for v in item_order:
            order_within_group[group[v]].append(v)

        # STEP 5. Combine ordered groups.
        ans = []
        for group in group_order:
            ans += order_within_group[group]
        return ans


sol = Solution()
n = 8
m = 2
group = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
# n, m, group, beforeItems= 8, 2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3],[],[4],[]]
print(sol.sortItems(n, m, group, beforeItems))

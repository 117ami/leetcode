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
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#
# https://leetcode.com/problems/bus-routes/description/
#
# algorithms
# Hard (42.57%)
# Total Accepted:    38.7K
# Total Submissions: 90.8K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
# repeats forever. For example if routes[0] = [1, 5, 7], this means that the
# first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->...
# forever.
#
# We start at bus stop S (initially not on a bus), and we want to go to bus
# stop T. Travelling by buses only, what is the least number of buses we must
# take to reach our destination? Return -1 if it is not possible.
#
#
# Example:
# Input:
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation:
# The best strategy is take the first bus to the bus stop 7, then take the
# second bus to the bus stop 6.
#
#
#
# Constraints:
#
#
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10^5.
# 0 <= routes[i][j] < 10 ^ 6.
#
#
#
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int,
                              T: int) -> int:
        n = len(routes)
        if S == T: return 0
        stop_to_bus = defaultdict(set)
        for i in range(n):
            for j in routes[i]:
                stop_to_bus[j].add(i)

        queue = deque(stop_to_bus[S])
        step = 1
        print(queue)
        print(stop_to_bus)
        visited = [False] * len(routes)
        while queue:
            for _ in range(len(queue)):
                bus = queue.popleft()

                if visited[bus]: continue
                visited[bus] = True
                for stop in routes[bus]:
                    if T == stop: return step
                    for next_bus in stop_to_bus[stop]:
                        queue.append(next_bus)

            step += 1

        return -1


sol = Solution()
inputs = [[1, 3, 7], [2, 4, 7], [2, 4, 9], [9, 3, 11]]
print(sol.numBusesToDestination(inputs, 1, 11))

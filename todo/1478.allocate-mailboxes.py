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
# @lc app=leetcode id=1478 lang=python3
#
# [1478] Allocate Mailboxes
#
# https://leetcode.com/problems/allocate-mailboxes/description/
#
# algorithms
# Hard (35.67%)
# Total Accepted:    637
# Total Submissions: 1.6K
# Testcase Example:  '[1,4,8,10,20]\n3'
#
# Given the array houses and an integer k. where houses[i] is the location of
# the ith house along a street, your task is to allocate k mailboxes in the
# street.
#
# Return the minimum total distance between each house and its nearest
# mailbox.
#
# The answer is guaranteed to fit in a 32-bit signed integer.
#
#
# Example 1:
#
#
#
#
# Input: houses = [1,4,8,10,20], k = 3
# Output: 5
# Explanation: Allocate mailboxes in position 3, 9 and 20.
# Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3|
# + |9-8| + |10-9| + |20-20| = 5
#
#
# Example 2:
#
#
#
#
# Input: houses = [2,3,5,12,18], k = 2
# Output: 9
# Explanation: Allocate mailboxes in position 3 and 14.
# Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3|
# + |5-3| + |12-14| + |18-14| = 9.
#
#
# Example 3:
#
#
# Input: houses = [7,4,6,1], k = 1
# Output: 8
#
#
# Example 4:
#
#
# Input: houses = [3,6,14,10], k = 4
# Output: 0
#
#
#
# Constraints:
#
#
# n == houses.length
# 1 <= n <= 100
# 1 <= houses[i] <= 10^4
# 1 <= k <= n
# Array houses contain unique integers.
#
#


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses = sorted(houses)
        # Cost to put a mail box among house[i:j]
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                # The best way is put the mail box at median position among
                # houses[i:j]
                median = houses[(i + j) // 2]
                costs[i][j] = sum(map(lambda t: abs(median - houses[t]), range(i, j+1)))

        @lru_cache(None)
        def dp(k, i):
            if k == 0 and i == n:
                return 0
            ans = math.inf
            for j in range(i, n):
                cost = costs[i][j]
                ans = min(ans, cost + dp(k - 1, j + 1))
            return ans

        return dp(k, 0)


sol = Solution()
houses = [2, 3, 5, 12, 18]
k = 2
print(sol.minDistance(houses, k))

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
# @lc app=leetcode id=1547 lang=python3
#
# [1547] Minimum Cost to Cut a Stick
#
# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/
#
# algorithms
# Hard (36.84%)
# Total Accepted:    2.1K
# Total Submissions: 5.1K
# Testcase Example:  '7\n[1,3,4,5]'
#
# Given a wooden stick of length n units. The stick is labelled from 0 to n.
# For example, a stick of length 6 is labelled as follows:
#
# Given an integer array cuts where cuts[i] denotes a position you should
# perform a cut at.
#
# You should perform the cuts in order, you can change the order of the cuts as
# you wish.
#
# The cost of one cut is the length of the stick to be cut, the total cost is
# the sum of costs of all cuts. When you cut a stick, it will be split into two
# smaller sticks (i.e. the sum of their lengths is the length of the stick
# before the cut). Please refer to the first example for a better explanation.
#
# Return the minimum total cost of the cuts.
#
#
# Example 1:
#
#
# Input: n = 7, cuts = [1,3,4,5]
# Output: 16
# Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the
# following scenario:
#
# The first cut is done to a rod of length 7 so the cost is 7. The second cut
# is done to a rod of length 6 (i.e. the second part of the first cut), the
# third is done to a rod of length 4 and the last cut is to a rod of length 3.
# The total cost is 7 + 6 + 4 + 3 = 20.
# Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario
# with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).
#
# Example 2:
#
#
# Input: n = 9, cuts = [5,6,1,4,2]
# Output: 22
# Explanation: If you try the given cuts ordering the cost will be 25.
# There are much ordering with total cost <= 25, for example, the order [4, 6,
# 5, 2, 1] has total cost = 22 which is the minimum possible.
#
#
#
# Constraints:
#
#
# 2 <= n <= 10^6
# 1 <= cuts.length <= min(n - 1, 100)
# 1 <= cuts[i] <= n - 1
# All the integers in cuts array are distinct.
#
#


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts += [0, n]
        cuts.sort()
        _size = len(cuts)
        dp = [[float('inf')] * _size for _ in range(_size)]

        for d in range(1, _size):
            for i in range(_size - d):
                if d == 1:
                    dp[i][i + d] = 0
                else:
                    dp[i][i + d] = min((dp[i][j] + dp[j][i + d])
                                       for j in range(i + 1, i + d)) + cuts[i + d] - cuts[i]
        return dp[0][_size - 1]


sol = Solution()


n = 7
cuts = [1, 3, 4, 5]
n = 9
cuts = [5, 6, 1, 4, 2]
print(sol.minCost(n, cuts))

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
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (31.59%)
# Total Accepted:    133.3K
# Total Submissions: 421.8K
# Testcase Example:  '[1,0,2]'
#
# There are N children standing in a line. Each child is assigned a rating
# value.
#
# You are giving candies to these children subjected to the following
# requirements:
#
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
#
# What is the minimum candies you must give?
#
# Example 1:
#
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
#
#
# Example 2:
#
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# ⁠            The third child gets 1 candy because it satisfies the above two
# conditions.
#
#
#


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n
        # res = reduce(lambda r, i: r + ([r[-1] + 1] if ratings[i]
        #                                > ratings[i - 1] else [res[i]]), range(1, n), [1])

        # # print(res)
        # res = reduce(lambda r, i: r + ([max(res[i], r[-1] + 1)] if ratings[i]
        #                > ratings[i + 1] else [res[i]] ), range(n - 2, -1, -1), [res[-1]])
        # return sum(res)
        # # print(res)
        # res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
                
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                res[i - 1] = max(res[i - 1], res[i] + 1)
        # print(res)
        return sum(res)


sol = Solution()


inputs = [1, 0, 2]
# inputs =   [1,2,2]
inputs = [1, 3, 2, 2, 1]
# inputs = [1, 2, 87, 87, 87, 2, 1]
print(sol.candy(inputs))

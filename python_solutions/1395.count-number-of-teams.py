from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#
# https://leetcode.com/problems/count-number-of-teams/description/
#
# algorithms
# Medium (81.24%)
# Total Accepted:    6.3K
# Total Submissions: 7.8K
# Testcase Example:  '[2,5,3,4,1]\r'
#
# There are n soldiers standing in a line. Each soldier is assigned a unique
# rating value.
#
# You have to form a team of 3 soldiers amongst them under the following
# rules:
#
#
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j],
# rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] >
# rating[j] > rating[k]) where (0 <= i < j < k < n).
#
#
# Return the number of teams you can form given the conditions. (soldiers can
# be part of multiple teams).
#
#
# Example 1:
#
#
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1),
# (5,3,1).
#
#
# Example 2:
#
#
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
#
#
# Example 3:
#
#
# Input: rating = [1,2,3,4]
# Output: 4
#
#
#
# Constraints:
#
#
# n == rating.length
# 1 <= n <= 200
# 1 <= rating[i] <= 10^5
#
#


class Solution:
    def numTeams(self, rating):
        larger = defaultdict(int)
        smaller = defaultdict(int)
        n = len(rating)
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    larger[i] += 1
                elif rating[j] < rating[i]:
                    smaller[i] += 1
        res = 0
        # print(larger)
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    res += larger[j]
                elif rating[j] < rating[i]:
                    res += smaller[j]
        return res


sol = Solution()
rating = [2, 5, 3, 4, 1]
rating = [1, 2, 3, 4]
print(sol.numTeams(rating))

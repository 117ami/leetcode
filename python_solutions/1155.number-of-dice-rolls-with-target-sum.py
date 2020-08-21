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
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (48.89%)
# Total Accepted:    44K
# Total Submissions: 90.1K
# Testcase Example:  '1\n6\n3'
#
# You have d dice, and each die has f faces numbered 1, 2, ..., f.
#
# Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to
# roll the dice so the sum of the face up numbers equals target.
#
#
# Example 1:
#
#
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation:
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
#
#
# Example 2:
#
#
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation:
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
#
#
# Example 3:
#
#
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation:
# You throw two dice, each with 5 faces.  There is only one way to get a sum of
# 10: 5+5.
#
#
# Example 4:
#
#
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation:
# You throw one die with 2 faces.  There is no way to get a sum of 3.
#
#
# Example 5:
#
#
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation:
# The answer must be returned modulo 10^9 + 7.
#
#
#
# Constraints:
#
#
# 1 <= d, f <= 30
# 1 <= target <= 1000
#
#


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # return self.test(d, f, target)
        if d * f < target: return 0
        dp = [[0] * (target + 1) for _ in range(d + 1)]

        for i in range(1, d + 1):
            for j in range(i, target + 1):
                n = 0
                if i == 1:
                    dp[i][j] = int(j > 0 and j <= f)
                else:
                    for k in range(1, min(j + 1, f + 1)):
                        # if j - k >= i - 1:
                        n += dp[i - 1][j - k]
                dp[i][j] += n % MOD
        return dp[-1][-1] % MOD


sol = Solution()

d, f, target = 2, 2, 4
d, f, target = 3, 6, 10

d, f, target = 2, 6, 7
# d = 1, f = 2, target = 3
# d, f, target = 30, 30, 500
print(sol.numRollsToTarget(d, f, target))

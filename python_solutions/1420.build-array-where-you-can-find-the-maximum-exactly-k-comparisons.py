from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1420 lang=python3
#
# [1420] Build Array Where You Can Find The Maximum Exactly K Comparisons
#
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/description/
#
# algorithms
# Hard (63.06%)
# Total Accepted:    1.8K
# Total Submissions: 2.7K
# Testcase Example:  '2\n3\n1'
#
# Given three integers n, m and k. Consider the following algorithm to find the
# maximum element of an array of positive integers:
#
# You should build the array arr which has the following properties:
#
#
# arr has exactly n integers.
# 1 <= arr[i] <= m where (0 <= i < n).
# After applying the mentioned algorithm to arr, the value search_cost is equal
# to k.
#
#
# Return the number of ways to build the array arr under the mentioned
# conditions. As the answer may grow large, the answer must be computed modulo
# 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 2, m = 3, k = 1
# Output: 6
# Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2]
# [3, 3]
#
#
# Example 2:
#
#
# Input: n = 5, m = 2, k = 3
# Output: 0
# Explanation: There are no possible arrays that satisify the mentioned
# conditions.
#
#
# Example 3:
#
#
# Input: n = 9, m = 1, k = 1
# Output: 1
# Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
#
#
# Example 4:
#
#
# Input: n = 50, m = 100, k = 25
# Output: 34549172
# Explanation: Don't forget to compute the answer modulo 1000000007
#
#
# Example 5:
#
#
# Input: n = 37, m = 17, k = 7
# Output: 418930126
#
#
#
# Constraints:
#
#
# 1 <= n <= 50
# 1 <= m <= 100
# 0 <= k <= n
#
#


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        i32_mod = 10 ** 9+ 7
        cc = [[0] * (k+1) for _ in range(m+1)]
        

    def numOfArrays_2(self, n: int, m: int, k: int) -> int:
        i32_mod = 10**9 + 7
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        @lru_cache(None)
        def dfs(i, curmax, curcost):
            if i == n:
                return 1 if k == curcost else 0

            if dp[i][curmax][curcost] > 0:
                return dp[i][curmax][curcost]

            res = curmax * dfs(i + 1, curmax, curcost) % i32_mod

            if curcost < k:
                for next_max in range(curmax + 1, m + 1):
                    res += dfs(i + 1, next_max, curcost + 1)
                    res %= i32_mod

            dp[i][curmax][curcost] = res
            return res
        return dfs(0, 0, 0)


sol = Solution()
print(sol.numOfArrays(50, 100, 25))

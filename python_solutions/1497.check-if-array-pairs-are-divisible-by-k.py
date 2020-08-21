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
# @lc app=leetcode id=1497 lang=python3
#
# [1497] Check If Array Pairs Are Divisible by k
#
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/
#
# algorithms
# Medium (37.34%)
# Total Accepted:    5.3K
# Total Submissions: 12.6K
# Testcase Example:  '[1,2,3,4,5,10,6,7,8,9]\n5'
#
# Given an array of integers arr of even length n and an integer k.
#
# We want to divide the array into exactly n / 2 pairs such that the sum of
# each pair is divisible by k.
#
# Return True If you can find a way to do that or False otherwise.
#
#
# Example 1:
#
#
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
#
#
# Example 2:
#
#
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
#
#
# Example 3:
#
#
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to
# divide arr into 3 pairs each with sum divisible by 10.
#
#
# Example 4:
#
#
# Input: arr = [-10,10], k = 2
# Output: true
#
#
# Example 5:
#
#
# Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
# Output: true
#
#
#
# Constraints:
#
#
# arr.length == n
# 1 <= n <= 10^5
# n is even.
# -10^9 <= arr[i] <= 10^9
# 1 <= k <= 10^5
#
#


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cc = [0] * (1 + k)
        for a in arr:
            x = (a % k)
            if cc[k - x] > 0:
                cc[k - x] -= 1
            else:
                cc[x] += 1
        return cc[0] % 2 == 0 and all(n == 0 for n in cc[1:])


sol = Solution()

arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k = 5
# arr = [1, 2, 3, 4, 5, 6]; k = 7
# arr = [1,2,3,4,5,6]; k = 10
# arr = [-10,10]; k = 2
# arr=[-1,1,-2,2,-3,3,-4,4];k = 3
print(sol.canArrange(arr, k))

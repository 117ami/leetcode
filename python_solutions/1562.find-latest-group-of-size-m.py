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
# @lc app=leetcode id=1562 lang=python3
#
# [1562] Find Latest Group of Size M
#
# https://leetcode.com/problems/find-latest-group-of-size-m/description/
#
# algorithms
# Medium (21.84%)
# Total Accepted:    1.4K
# Total Submissions: 6.5K
# Testcase Example:  '[3,5,1,2,4]\n1'
#
# Given an array arr that represents a permutation of numbers from 1 to n. You
# have a binary string of size n that initially has all its bits set to zero.
#
# At each step i (assuming both the binary string and arr are 1-indexed) from 1
# to n, the bit at position arr[i] is set to 1. You are given an integer m and
# you need to find the latest step at which there exists a group of ones of
# length m. A group of ones is a contiguous substring of 1s such that it cannot
# be extended in either direction.
#
# Return the latest step at which there exists a group of ones of length
# exactly m. If no such group exists, return -1.
#
#
# Example 1:
#
#
# Input: arr = [3,5,1,2,4], m = 1
# Output: 4
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "00101", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "11101", groups: ["111", "1"]
# Step 5: "11111", groups: ["11111"]
# The latest step at which there exists a group of size 1 is step 4.
#
# Example 2:
#
#
# Input: arr = [3,1,5,4,2], m = 2
# Output: -1
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "10100", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "10111", groups: ["1", "111"]
# Step 5: "11111", groups: ["11111"]
# No group of size 2 exists during any step.
#
#
# Example 3:
#
#
# Input: arr = [1], m = 1
# Output: 1
#
#
# Example 4:
#
#
# Input: arr = [2,1], m = 2
# Output: 2
#
#
#
# Constraints:
#
#
# n == arr.length
# 1 <= n <= 10^5
# 1 <= arr[i] <= n
# All integers in arr are distinct.
# 1 <= m <= arr.length
#
#
#
class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def merge(self, x, y, greater):
        px, py = self.find(x), self.find(y)
        if greater:
            self.p[px] = self.p[py] = max(px, py)
        else:
            self.p[px] = self.p[py] = min(px, py)

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        left, right = UF(n + 1), UF(n + 1)
        cc = [0] * (n + 1)
        seen = [False] * (n + 1)
        res = -1
        for i, a in enumerate(arr):
            seen[a] = True
            if seen[a - 1]:
                left.merge(a, a - 1, False)
                right.merge(a, a - 1, True)

            if a < n and seen[a + 1]:
                left.merge(a + 1, a, False)
                right.merge(a, a + 1, True)

            la, ra = left.find(a), right.find(a)
            cc[a - la] -= 1
            cc[ra - a] -= 1
            cc[ra - la + 1] += 1
            if cc[m] > 0:
                res = i + 1
        return res


sol = Solution()

arr, m = [3, 5, 1, 2, 4], 1
# arr, m = [3, 1, 5, 4, 2], 2
# arr, m = [1], 1
# arr, m = [2, 1], 2
print(sol.findLatestStep(arr, m))

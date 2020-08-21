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
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/
#
# algorithms
# Medium (55.12%)
# Total Accepted:    6.3K
# Total Submissions: 11.3K
# Testcase Example:  '3\n1'
#
# Given two positive integers n and k, the binary string  Sn is formed as
# follows:
#
#
# S1 = "0"
# Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
#
#
# Where + denotes the concatenation operation, reverse(x) returns the reversed
# string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1
# changes to 0).
#
# For example, the first 4 strings in the above sequence are:
#
#
# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
#
#
# Return the k^th bit in Sn. It is guaranteed that k is valid for the given
# n.
#
#
# Example 1:
#
#
# Input: n = 3, k = 1
# Output: "0"
# Explanation: S3 is "0111001". The first bit is "0".
#
#
# Example 2:
#
#
# Input: n = 4, k = 11
# Output: "1"
# Explanation: S4 is "011100110110001". The 11th bit is "1".
#
#
# Example 3:
#
#
# Input: n = 1, k = 1
# Output: "0"
#
#
# Example 4:
#
#
# Input: n = 2, k = 3
# Output: "1"
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
# 1 <= k <= 2^n - 1
#
#


class Solution:
    def __init__(self):
        self.map = {'0': '1', '1': '0'}

    def findKthBit(self, n: int, k: int) -> str:
        mid = 1 << (n-1)
        if n == 1 or k == 1: return '0'
        if k == mid: return '1'
        if k < mid: return self.findKthBit(n - 1, k)
        else:
            sbit = self.findKthBit(n - 1, 2**n - k)
            return self.map[sbit]


sol = Solution()


n = 3
k = 1
# n = 4; k = 11
# n = 1; k = 1
# n = 2; k = 3
print(sol.findKthBit(n, k))
# for k in range(8, 16):
# print(k, sol.findKthBit(n, k))

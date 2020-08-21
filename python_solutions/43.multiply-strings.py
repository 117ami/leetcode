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
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (33.92%)
# Total Accepted:    304.1K
# Total Submissions: 896.2K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
# Example 1:
#
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
#
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Note:
#
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#
#
#
def ctoi(c):
    return ord(c) - ord('0')


class Solution:
    def multiply(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        pos = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = ctoi(s[i]) * ctoi(t[j])
                p1, p2 = i + j, i + j + 1
                sum = mul + pos[p2]
                print(i, j, mul, pos[p2])

                pos[p1] += sum // 10
                pos[p2] = sum % 10
                print(pos)
        r = ''.join(map(str, pos)).lstrip('0')
        # The case when one of them is zero 
        return r if r else '0'


sol = Solution()

ssss, tttt = "123", "456"

print(sol.multiply(ssss, tttt))

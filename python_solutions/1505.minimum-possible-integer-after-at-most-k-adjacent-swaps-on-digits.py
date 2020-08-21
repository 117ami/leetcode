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
# @lc app=leetcode id=1505 lang=python3
#
# [1505] Minimum Possible Integer After at Most K Adjacent Swaps On Digits
#
# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/description/
#
# algorithms
# Hard (36.15%)
# Total Accepted:    3.8K
# Total Submissions: 10.5K
# Testcase Example:  '"4321"\n4'
#
# Given a string num repccenting the digits of a very large integer and an
# integer k.
#
# You are allowed to swap any two adjacent digits of the integer at most k
# times.
#
# Return the minimum integer you can obtain also as a string.
#
#
# Example 1:
#
#
# Input: num = "4321", k = 4
# Output: "1342"
# Explanation: The steps to obtain the minimum integer from 4321 with 4
# adjacent swaps are shown.
#
#
# Example 2:
#
#
# Input: num = "100", k = 1
# Output: "010"
# Explanation: It's ok for the output to have leading zeros, but the input is
# guaranteed not to have any leading zeros.
#
#
# Example 3:
#
#
# Input: num = "36789", k = 1000
# Output: "36789"
# Explanation: We can keep the number without any swaps.
#
#
# Example 4:
#
#
# Input: num = "22", k = 22
# Output: "22"
#
#
# Example 5:
#
#
# Input: num = "9438957234785635408", k = 23
# Output: "0345989723478563548"
#
#
#
# Constraints:
#
#
# 1 <= num.length <= 30000
# num contains digits only and doesn't have leading zeros.
# 1 <= k <= 10^9
#
#
#


class Solution:
    def _move_forward(self, d, k, ns):
        if k <= 0:
            return k, ns
        cc = []
        for i, n in enumerate(ns):
            if n == d:
                if i > 0 and n > ns[i - 1]:
                    break
                cc.append(i)

        for cnt, idx in enumerate(cc):
            if idx - cnt <= k:
                k -= idx - cnt
                self.pre.append(d)
                ns[idx] = -1
            else:
                break
        ns = list(filter(lambda x: x > -1, ns))
        return k, ns

    def minInteger(self, num: str, k: int) -> str:
        ns = list(map(int, list(num)))
        self.pre = []
        for i in range(10):
            k, ns = self._move_forward(i, k, ns)
            # print(i, self.pre, k, ns)
        # print(k, self.pre, ns)
        if k > 0 and ns:
            x = ns[0]
            ns[0] = self.pre[-1]
            self.pre.insert(-k, x)
            self.pre.pop()
        # print(k, self.pre, ns)
        return ''.join(map(str, self.pre + ns))


sol = Solution()

num, k = "4321", 4
num, k = "100", 1
num, k = "36789", 1000
# num, k = "22", 22
# num, k = "9438957234785635408", 23
num, k = "9000900", 3
num,k="3112056788886886880368579471175675",40
# num, k = "294984148179", 11
# num, k = "9989150892151",5
print(sol.minInteger(num, k))

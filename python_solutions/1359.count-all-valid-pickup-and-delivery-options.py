from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
#
# algorithms
# Hard (56.56%)
# Total Accepted:    2.1K
# Total Submissions: 3.7K
# Testcase Example:  '1'
#
# Given n orders, each order consist in pickup and delivery services. 
#
# Count all valid pickup/delivery possible sequences such that delivery(i) is
# always after of pickup(i). 
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: 1
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
#
#
# Example 2:
#
#
# Input: n = 2
# Output: 6
# Explanation: All possible orders:
# (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and
# (P2,D2,P1,D1).
# This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery
# 2.
#
#
# Example 3:
#
#
# Input: n = 3
# Output: 90
#
#
#
# Constraints:
#
#
# 1 <= n <= 500
#
#
mod = 10**9 + 7
memo = {1: 1, 2: 6}
for j in range(3, 501):
    memo[j] = j * (memo[j - 1] * (2 * j - 1)) % mod

class Solution:
    def countOrders(self, n: int) -> int:
        return memo[n]


sol = Solution()
for i in range(1, 5):
    print(i, sol.countOrders(i))
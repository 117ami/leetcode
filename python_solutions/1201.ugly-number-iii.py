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
# @lc app=leetcode id=1201 lang=python3
#
# [1201] Ugly Number III
#
# https://leetcode.com/problems/ugly-number-iii/description/
#
# algorithms
# Medium (25.25%)
# Total Accepted:    7.4K
# Total Submissions: 29.2K
# Testcase Example:  '3\n2\n3\n5'
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive integers which are divisible by a or b or c.
#
#
# Example 1:
#
#
# Input: n = 3, a = 2, b = 3, c = 5
# Output: 4
# Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
#
# Example 2:
#
#
# Input: n = 4, a = 2, b = 3, c = 4
# Output: 6
# Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
#
#
# Example 3:
#
#
# Input: n = 5, a = 2, b = 11, c = 13
# Output: 10
# Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is
# 10.
#
#
# Example 4:
#
#
# Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
# Output: 1999999984
#
#
#
# Constraints:
#
#
# 1 <= n, a, b, c <= 10^9
# 1 <= a * b * c <= 10^18
# It's guaranteed that the result will be in range [1, 2 * 10^9]
#
#
#


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = c * b // math.gcd(c, b)
        abc = ab * c // math.gcd(ab, c)
        lo, hi = 1, 2 * 10**9 
        while lo < hi:
            mid = lo + (hi - lo) // 2
            cnt = mid // a + mid // b + mid // c + mid // abc - mid // ac - mid // ab - mid // bc
            if cnt < n:
                lo = mid + 1
            else:
                hi = mid
        return lo


sol = Solution()
print(sol.nthUglyNumber(1000000000, 2, 217983653, 336916467))

from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Medium (30.86%)
# Total Accepted:    52.9K
# Total Submissions: 171.3K
# Testcase Example:  '3'
#
# Find the n^th digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 2^31).
#
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
#
#
#
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
#
#
#


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        base, bit, cc = 1, 1, 0
        while true:
            cc += (base * 9) * bit
            if cc == n:
                return 9
            elif cc > n:
                break
            base *= 10
            bit += 1
        cc -= (base * 9) * bit
        q, r = divmod(n - cc, bit)

        q += pow(10, bit - 1) - 1
        # print(cc, base, bit, q, r)
        if r == 0:
            return int(str(q)[-1])
        else:
            return int(str(q + 1)[r - 1])


sol = Solution()
n = 1000
print(sol.findNthDigit(n))
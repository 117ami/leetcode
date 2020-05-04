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
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (63.38%)
# Total Accepted:    134.6K
# Total Submissions: 211.4K
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
#
#
#
# Example 1:
#
#
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
#
#
#
#
# Example 2:
#
#
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
#
#
#
#
# Note:
#
#
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
# This question is the same as 1009:
# https://leetcode.com/problems/complement-of-base-10-integer/
#
#
#


class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join('1' if i == '0' else '0' for i in bin(num)[2:]), 2)


sol = Solution()
print(sol.findComplement(1))
# print(int("0101", 2))

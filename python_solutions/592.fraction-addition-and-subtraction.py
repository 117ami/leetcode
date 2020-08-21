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
# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#
# https://leetcode.com/problems/fraction-addition-and-subtraction/description/
#
# algorithms
# Medium (49.00%)
# Total Accepted:    18.3K
# Total Submissions: 37.3K
# Testcase Example:  '"-1/2+1/2"'
#
# Given a string representing an expression of fraction addition and
# subtraction, you need to return the calculation result in string format. The
# final result should be irreducible fraction. If your final result is an
# integer, say 2, you need to change it to the format of fraction that has
# denominator 1. So in this case, 2 should be converted to 2/1.
#
# Example 1:
#
# Input:"-1/2+1/2"
# Output: "0/1"
#
#
#
# Example 2:
#
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
#
#
#
# Example 3:
#
# Input:"1/3-1/2"
# Output: "-1/6"
#
#
#
# Example 4:
#
# Input:"5/3+1/3"
# Output: "2/1"
#
#
#
# Note:
#
# The input string only contains '0' to '9', '/', '+' and '-'. So does the
# output.
# Each fraction (input and output) has format ±numerator/denominator. If the
# first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and
# denominator of each fraction will always be in the range [1,10]. If the
# denominator is 1, it means this fraction is actually an integer in a fraction
# format defined above.
# The number of given fractions will be in the range [1,10].
# The numerator and denominator of the final result are guaranteed to be valid
# and in the range of 32-bit int.
#
#
#
class Solution:
    def fractionAddition(self, expression: str) -> str:
        import re
        ints = map(int, re.findall('[+-]?\d+', expression))
        a, b = 0, 1
        for c in ints:
            d = next(ints)
            a = a * d + b * c
            b *= d
            g = math.gcd(a, b)
            a //= g
            b //= g
        return f'{a}/{b}'


sol = Solution()

inputs = "-1/2+1/2"
inputs = "-1/2+1/2+1/3"
# inputs =  "1/3-1/2"
# inputs =  "5/3+1/3"
inputs = "-5/2+10/3+7/9"
print(sol.fractionAddition(inputs))

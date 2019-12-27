from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
true = True
false = False
#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (45.48%)
# Total Accepted:    48.2K
# Total Submissions: 105.9K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
#
# Example 1:
#
# Input: 100
# Output: "202"
#
#
#
# Example 2:
#
# Input: -7
# Output: "-10"
#
#
#
# Note:
# The input will be in range of [-1e7, 1e7].
#
#


class Solution:
    def convertToBase7(self, num: int) -> str:
        res = []
        sign = "" if num > 0 else "-"
        num = abs(num)
        if num == 0: return "0" 
        while num > 0:
            res.append(num % 7)
            num = num // 7
        return sign + ''.join([str(i) for i in res[::-1]])


s = Solution()
print(s.convertToBase7(100))

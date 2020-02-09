from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#
# https://leetcode.com/problems/angle-between-hands-of-a-clock/description/
#
# algorithms
# Medium (61.17%)
# Total Accepted:    3K
# Total Submissions: 4.9K
# Testcase Example:  '12\n30'
#
# Given two numbers, hour and minutes. Return the smaller angle (in sexagesimal
# units) formed between the hour and the minute hand.
#
#
# Example 1:
#
#
#
#
# Input: hour = 12, minutes = 30
# Output: 165
#
#
# Example 2:
#
#
#
#
# Input: hour = 3, minutes = 30
# Output: 75
#
#
# Example 3:
#
#
#
#
# Input: hour = 3, minutes = 15
# Output: 7.5
#
#
# Example 4:
#
#
# Input: hour = 4, minutes = 50
# Output: 155
#
#
# Example 5:
#
#
# Input: hour = 12, minutes = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.
#
#
#


class Solution:
    def angleClock(self, h: int, m: int) -> float:
        ang = m / 60.0 * 360 - (h + m / 60.0) / 12.0 * 360
        return min(abs(ang), 360 - abs(ang))


sol = Solution()
h, m = 4, 50
h, m = 3, 15
h, m = 12, 0
print(sol.angleClock(h, m))

from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=1124 lang=python3
#
# [1124] Longest Well-Performing Interval
#
# https://leetcode.com/problems/longest-well-performing-interval/description/
#
# algorithms
# Medium (32.09%)
# Total Accepted:    7.8K
# Total Submissions: 24.3K
# Testcase Example:  '[9,9,6,0,6,6,9]'
#
# We are given hours, a list of the number of hours worked per day for a given
# employee.
#
# A day is considered to be a tiring day if and only if the number of hours
# worked is (strictly) greater than 8.
#
# A well-performing interval is an interval of days for which the number of
# tiring days is strictly larger than the number of non-tiring days.
#
# Return the length of the longest well-performing interval.
#
#
# Example 1:
#
#
# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].
#
#
#
# Constraints:
#
#
# 1 <= hours.length <= 10000
# 0 <= hours[i] <= 16
#
#
#


class Solution:
    def longestWPI(self, hours):
        mm = defaultdict(int)
        best, n = 0, 0
        for i, h in enumerate(hours):
            n += (1 if h > 8 else -1)
            if n not in mm:
                mm[n] = i
            if n > 0 and i + 1 > best:
                best = i + 1
            elif n <= 0 and n - 1 in mm and i - mm[n - 1] > best:
                best = i - mm[n - 1]

        return best


sol = Solution()
hours = [9, 9, 6, 0, 6, 6, 9]
# hours = [-6, -6, -6, 9, 9, -6, 9]
# hours = [6, 6, 9]
print(sol.longestWPI(hours))

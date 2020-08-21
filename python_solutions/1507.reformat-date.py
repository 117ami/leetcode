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
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#
# https://leetcode.com/problems/reformat-date/description/
#
# algorithms
# Easy (60.02%)
# Total Accepted:    6.6K
# Total Submissions: 10.8K
# Testcase Example:  '"20th Oct 2052"'
#
# Given a date string in the form Day Month Year, where:
#
#
# Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
# "Sep", "Oct", "Nov", "Dec"}.
# Year is in the range [1900, 2100].
#
#
# Convert the date string to the format YYYY-MM-DD, where:
#
#
# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.
#
#
#
# Example 1:
#
#
# Input: date = "20th Oct 2052"
# Output: "2052-10-20"
#
#
# Example 2:
#
#
# Input: date = "6th Jun 1933"
# Output: "1933-06-06"
#
#
# Example 3:
#
#
# Input: date = "26th May 1960"
# Output: "1960-05-26"
#
#
#
# Constraints:
#
#
# The given dates are guaranteed to be valid, so no error handling is
# necessary.
#
#
#


class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        hm = dict(zip(months, range(1, 13)))
        d, m, y = date.split(' ')
        for suf in ['st', 'nd', 'rd', 'th']:
            if suf in d:
                d = ('0' + d.replace(suf, ''))[-2:]

        m = ('0' + str(hm[m]))[-2:]
        return '-'.join([y, m, d])


sol = Solution()


date = "20th Oct 2052"
# date = "6th Jun 1933"
date = "26th May 1960"
print(sol.reformatDate(date))

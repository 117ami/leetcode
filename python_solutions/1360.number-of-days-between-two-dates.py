from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1360 lang=python3
#
# [1360] Number of Days Between Two Dates
#
# https://leetcode.com/problems/number-of-days-between-two-dates/description/
#
# algorithms
# Easy (47.88%)
# Total Accepted:    3.9K
# Total Submissions: 8.2K
# Testcase Example:  '"2019-06-29"\n"2019-06-30"'
#
# Write a program to count the number of days between two dates.
# 
# The two dates are given as strings, their format is YYYY-MM-DD as shown in
# the examples.
# 
# 
# Example 1:
# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:
# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
# 
# 
# Constraints:
# 
# 
# The given dates are valid dates between the years 1971 and 2100.
# 
# 
#
import datetime
import time 
class Solution:
    def daysBetweenDates(self, d1, d2):
        x = time.mktime(datetime.datetime.strptime(d1, "%Y-%m-%d").timetuple())
        y = time.mktime(datetime.datetime.strptime(d2, "%Y-%m-%d").timetuple())
        return int(abs(x-y)) // (3600 * 24)
        

sol = Solution()

date = "2020-02-09"
date2 = "2020-02-29"
d1, d2 = "1971-06-29", "2010-09-23"
d1, d2 = "2074-09-12", "1983-01-08"
print(sol.daysBetweenDates(d1, d2))




from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
true = True
false = False
#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
# https://leetcode.com/problems/minimum-cost-for-tickets/description/
#
# algorithms
# Medium (57.94%)
# Total Accepted:    27.3K
# Total Submissions: 47.1K
# Testcase Example:  '[1,4,6,7,8,20]\n[2,7,15]'
#
# In a country popular for train travel, you have planned some train travelling
# one year in advance.  The days of the year that you will travel is given as
# an array days.  Each day is an integer from 1 to 365.
#
# Train tickets are sold in 3 different ways:
#
#
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
#
#
# The passes allow that many days of consecutive travel.  For example, if we
# get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6,
# 7, and 8.
#
# Return the minimum number of dollars you need to travel every day in the
# given list of days.
#
#
#
# Example 1:
#
#
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation:
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4,
# ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.
#
#
#
# Example 2:
#
#
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation:
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1,
# 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total you spent $17 and covered all the days of your travel.
#
#
#
#
#
# Note:
#
#
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000
#
#
#


class Solution:
    def mincostTickets(self, days, costs):
        self.n = len(days)
        memo = {}

        def rec(i):
            if i in memo:
                return memo[i]
            if i >= self.n:
                return 0
            if i == self.n - 1:
                return min(costs)

            j = bisect_right(days[i:], days[i] + 29)
            c3 = costs[2] + rec(i + j)

            j = bisect_right(days[i:], days[i] + 6)
            c2 = costs[1] + rec(i + j)

            c1 = costs[0] + rec(i + 1)

            r = min(c1, c2, c3)
            memo[i] = r
            return r
        return rec(0)


s = Solution()
days, costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 32], [2, 7, 15]
# days, costs = [1,4,6,7,8,20], [2,7,15]
# days, costs = [1, 4, 6, 7, 8, 20], [7, 2, 15]
days, costs = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 41, 43,
               44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134]
days, costs = [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29], [3,14,50]               
print(s.mincostTickets(days, costs))

# print(bisect_right(days, 30))

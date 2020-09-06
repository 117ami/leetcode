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
# @lc app=leetcode id=1575 lang=python3
#
# [1575] Count All Possible Routes
#
# https://leetcode.com/problems/count-all-possible-routes/description/
#
# algorithms
# Hard (59.30%)
# Total Accepted:    1.7K
# Total Submissions: 2.8K
# Testcase Example:  '[2,3,6,8,4]\n1\n3\n5'
#
# You are given an array of distinct positive integers locations where
# locations[i] represents the position of city i. You are also given integers
# start, finish and fuel representing the starting city, ending city, and the
# initial amount of fuel you have, respectively.
#
# At each step, if you are at city i, you can pick any city j such that j != i
# and 0 <= j < locations.length and move to city j. Moving from city i to city
# j reduces the amount of fuel you have by |locations[i] - locations[j]|.
# Please notice that |x| denotes the absolute value of x.
#
# Notice that fuel cannot become negative at any point in time, and that you
# are allowed to visit any city more than once (including start and finish).
#
# Return the count of all possible routes from start to finish.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
# Output: 4
# Explanation: The following are all possible routes, each uses 5 units of
# fuel:
# 1 -> 3
# 1 -> 2 -> 3
# 1 -> 4 -> 3
# 1 -> 4 -> 2 -> 3
#
#
# Example 2:
#
#
# Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
# Output: 5
# Explanation: The following are all possible routes:
# 1 -> 0, used fuel = 1
# 1 -> 2 -> 0, used fuel = 5
# 1 -> 2 -> 1 -> 0, used fuel = 5
# 1 -> 0 -> 1 -> 0, used fuel = 3
# 1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5
#
#
# Example 3:
#
#
# Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
# Output: 0
# Explanation: It's impossible to get from 0 to 2 using only 3 units of fuel
# since the shortest route needs 4 units of fuel.
#
# Example 4:
#
#
# Input: locations = [2,1,5], start = 0, finish = 0, fuel = 3
# Output: 2
# Explanation: There are two possible routes, 0 and 0 -> 1 -> 0.
#
# Example 5:
#
#
# Input: locations = [1,2,3], start = 0, finish = 2, fuel = 40
# Output: 615088286
# Explanation: The total number of possible routes is 2615088300. Taking this
# number modulo 10^9 + 7 gives us 615088286.
#
#
#
# Constraints:
#
#
# 2 <= locations.length <= 100
# 1 <= locations[i] <= 10^9
# All integers in locations are distinct.
# 0 <= start, finish < locations.length
# 1 <= fuel <= 200
#
#
#
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int,
                    fuel: int) -> int:
        @lru_cache(None)
        def dp(i, f):
            if f < 0: return 0
            if f == 0: return i == finish
            ans = 1 if i == finish else 0
            for j in range(0, len(locations)):
                if j != i and f >= abs(locations[j] - locations[i]):
                    ans += dp(j, f - abs(locations[i] - locations[j])) % MOD

            return ans % MOD

        return dp(start, fuel)


sol = Solution()

locations, start, finish, fuel = [2, 3, 6, 8, 4], 1, 3, 5
# locations, start, finish, fuel = [4,3,1], 1, 0, 6
# locations, start, finish, fuel = [5,2,1], 0, 2, 3
# locations, start, finish, fuel = [2,1,5], 0, 0, 3
locations, start, finish, fuel = [1, 2, 3], 0, 2, 40
print(sol.countRoutes(locations, start, finish, fuel))

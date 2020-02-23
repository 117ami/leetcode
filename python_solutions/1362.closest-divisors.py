from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import string
import math 
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1362 lang=python3
#
# [1362] Closest Divisors
#
# https://leetcode.com/problems/closest-divisors/description/
#
# algorithms
# Medium (48.87%)
# Total Accepted:    4.2K
# Total Submissions: 8.3K
# Testcase Example:  '8'
#
# Given an integer num, find the closest two integers in absolute difference
# whose product equals num + 1 or num + 2.
# 
# Return the two integers in any order.
# 
# 
# Example 1:
# 
# 
# Input: num = 8
# Output: [3,3]
# Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 =
# 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
# 
# 
# Example 2:
# 
# 
# Input: num = 123
# Output: [5,25]
# 
# 
# Example 3:
# 
# 
# Input: num = 999
# Output: [40,25]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 10^9
# 
# 
#
class Solution:
    def closestDivisors(self, num):
        x = int(math.sqrt(num + 2))
        while x > 0:
            y = num % x
            if x - y == 1:
                return [x, (num + 1) // x]
            if x - y == 2:
                return [x, (num + 2) // x]
            x -= 1

sol = Solution()
print(sol.closestDivisors(123))



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
# @lc app=leetcode id=1553 lang=python3
#
# [1553] Minimum Number of Days to Eat N Oranges
#
# https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/description/
#
# algorithms
# Hard (20.36%)
# Total Accepted:    3.9K
# Total Submissions: 18.9K
# Testcase Example:  '10'
#
# There are n oranges in the kitchen and you decided to eat some of these
# oranges every day as follows:
#
#
# Eat one orange.
# If the number of remaining oranges (n) is divisible by 2 then you can eat
# n/2 oranges.
# If the number of remaining oranges (n) is divisible by 3 then you can eat
# 2*(n/3) oranges.
#
#
# You can only choose one of the actions per day.
#
# Return the minimum number of days to eat n oranges.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: You have 10 oranges.
# Day 1: Eat 1 orange,  10 - 1 = 9.
# Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
# Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1.
# Day 4: Eat the last orange  1 - 1  = 0.
# You need at least 4 days to eat the 10 oranges.
#
#
# Example 2:
#
#
# Input: n = 6
# Output: 3
# Explanation: You have 6 oranges.
# Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
# Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
# Day 3: Eat the last orange  1 - 1  = 0.
# You need at least 3 days to eat the 6 oranges.
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 1
#
#
# Example 4:
#
#
# Input: n = 56
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= n <= 2*10^9
#
#
cc = {1: 1, 2: 2, 3: 2}


class BS:
    '''General template for binary search 
    '''
    def search(self, lv: int, rv: int, bool_func, arg):
        left, right = lv, rv
        while left < right:
            mid = (left + right) // 2
            if bool_func(mid, *arg):
                left = mid + 1
            else:
                right = mid
        return left - 1


class Solution:
    @lru_cache()
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3));  
sol = Solution()

n = 10
n = 6
n = 1
n = 56
n = 6128305
print(sol.minDays(n))

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
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#
# https://leetcode.com/problems/water-bottles/description/
#
# algorithms
# Easy (65.56%)
# Total Accepted:    9.8K
# Total Submissions: 15K
# Testcase Example:  '9\n3'
#
# Given numBottles full water bottles, you can exchange numExchange empty water
# bottles for one full water bottle.
# 
# The operation of drinking a full water bottle turns it into an empty bottle.
# 
# Return the maximum number of water bottles you can drink.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: numBottles = 9, numExchange = 3
# Output: 13
# Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 9 + 3 + 1 = 13.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: numBottles = 15, numExchange = 4
# Output: 19
# Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
# Number of water bottles you can drink: 15 + 3 + 1 = 19.
# 
# 
# Example 3:
# 
# 
# Input: numBottles = 5, numExchange = 5
# Output: 6
# 
# 
# Example 4:
# 
# 
# Input: numBottles = 2, numExchange = 3
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numBottles <= 100
# 2 <= numExchange <= 100
# 
#
class Solution:
    def numWaterBottles(self, m, n):
        ans = 0 
        while m >= n:
            a, b = divmod(m, n)
            ans += a * n 
            m = b + a 
            # print(a, b, m, ans)
        return ans + m 
        

sol = Solution()
numBottles = 9; numExchange = 3
# numBottles = 15; numExchange = 4
# numBottles = 5; numExchange = 5
# numBottles = 2; numExchange = 3
print(sol.numWaterBottles(numBottles, numExchange))

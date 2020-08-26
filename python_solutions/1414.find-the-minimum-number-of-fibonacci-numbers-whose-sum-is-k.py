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
# @lc app=leetcode id=1414 lang=python3
#
# [1414] Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
#
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/description/
#
# algorithms
# Medium (63.44%)
# Total Accepted:    14K
# Total Submissions: 22.1K
# Testcase Example:  '7'
#
# Given the number k, return the minimum number of Fibonacci numbers whose sum
# is equal to k, whether a Fibonacci number could be used multiple times.
# 
# The Fibonacci numbers are defined as:
# 
# 
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 , for n > 2.
# 
# It is guaranteed that for the given constraints we can always find such
# fibonacci numbers that sum k.
# 
# Example 1:
# 
# 
# Input: k = 7
# Output: 2 
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
# For k = 7 we can use 2 + 5 = 7.
# 
# Example 2:
# 
# 
# Input: k = 10
# Output: 2 
# Explanation: For k = 10 we can use 2 + 8 = 10.
# 
# 
# Example 3:
# 
# 
# Input: k = 19
# Output: 3 
# Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= 10^9
# 
#
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        

sol = Solution()


k = 7
k = 10
k = 19
print(sol.findMinFibonacciNumbers(k))

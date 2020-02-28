from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#
# https://leetcode.com/problems/maximum-69-number/description/
#
# algorithms
# Easy (78.99%)
# Total Accepted:    20.9K
# Total Submissions: 26.5K
# Testcase Example:  '9669'
#
# Given a positive integer num consisting only of digits 6 and 9.
# 
# Return the maximum number you can get by changing at most one digit (6
# becomes 9, and 9 becomes 6).
# 
# 
# Example 1:
# 
# 
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666. 
# The maximum number is 9969.
# 
# 
# Example 2:
# 
# 
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# 
# Example 3:
# 
# 
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 10^4
# num's digits are 6 or 9.
# 
#
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
        

sol = Solution()
print(sol.maximum69Number(669696))



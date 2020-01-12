from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (33.46%)
# Total Accepted:    10.4K
# Total Submissions: 31K
# Testcase Example:  '1'
#
# Given a positive integer n, find the number of non-negative integers less
# than or equal to n, whose binary representations do NOT contain consecutive
# ones.
# 
# Example 1:
# 
# Input: 5
# Output: 5
# Explanation: 
# Here are the non-negative integers 
# 
# 
# Note:
# 1 
# 
#
class Solution:
    def findIntegers(self, num):
        memo = {0:1, 1:2}
        for i in range(2, 32):
            memo[i] = memo[i-1] + memo[i-2]
        
        res, k, pre = 0, 30, 0
        while k >= 0:
            if num & (1<<k):
                res += memo[k]
                if pre: return res 
                pre = 1 
            else:
                pre = 0
            k -= 1
        return res + 1

sol = Solution()
print(sol.findIntegers(5))


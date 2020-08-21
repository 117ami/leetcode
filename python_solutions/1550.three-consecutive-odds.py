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
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#
# https://leetcode.com/problems/three-consecutive-odds/description/
#
# algorithms
# Easy (68.73%)
# Total Accepted:    8K
# Total Submissions: 11.7K
# Testcase Example:  '[2,6,4,1]'
#
# Given an integer array arr, return true if there are three consecutive odd
# numbers in the array. Otherwise, return false.
#
# Example 1:
#
#
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
#
#
# Example 2:
#
#
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
#
#
#
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return '111' in ''.join(map(lambda n: '1' if n & 1 else '0', arr))
        # cnt = 0
        # for n in arr:
        #     if n & 1: cnt += 1
        #     else:
        #         cnt = 0
        #     if cnt >= 3: return True
        # return False


sol = Solution()

arr = [2, 6, 4, 1]
arr = [1,2,34,3,4,5,7,23,12]
print(sol.threeConsecutiveOdds(arr))

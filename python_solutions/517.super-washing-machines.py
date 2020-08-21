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
# @lc app=leetcode id=517 lang=python3
#
# [517] Super Washing Machines
#
# https://leetcode.com/problems/super-washing-machines/description/
#
# algorithms
# Hard (38.31%)
# Total Accepted:    16.9K
# Total Submissions: 44.1K
# Testcase Example:  '[1,0,5]'
#
# You have n super washing machines on a line. Initially, each washing machine
# has some dresses or is empty.
#
#
# For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass
# one dress of each washing machine to one of its adjacent washing machines  at
# the same time .
#
# Given an integer array representing the number of dresses in each washing
# machine from left to right on the line, you should find the minimum number of
# moves to make all the washing machines have the same number of dresses. If it
# is not possible to do it, return -1.
#
# Example1
#
# Input: [1,0,5]
#
# Output: 3
#
# Explanation:
# 1st move:    1     0     1     1     4
# 2nd move:    1     2     1     3
# 3rd move:    2     1     2     2     2
#
#
# Example2
#
# Input: [0,3,0]
#
# Output: 2
#
# Explanation:
# 1st move:    0     1     2     0
# 2nd move:    1     2 --> 0    =>    1     1     1
#
#
# Example3
#
# Input: [0,2,0]
#
# Output: -1
#
# Explanation:
# It's impossible to make all the three washing machines have the same number
# of dresses.
#
#
#
#
# Note:
#
# The range of n is [1, 10000].
# The range of dresses number in a super washing machine is [0, 1e5].
#
#
#
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        __sum, n = sum(machines), len(machines)
        if __sum % n > 0: return -1
        avg = __sum // n
        __max, cnt = 0, 0
        for load in machines:
            cnt += load - avg
            __max = max(__max, abs(cnt), load - avg)
        return __max


sol = Solution()

inputs = [1, 0, 5]
inputs = [0, 3, 0]
# inputs =   [0,2,0]
inputs = [4, 0, 0, 4]
inputs = [0, 0, 11, 5]
inputs=[4,0,5]
print(sol.findMinMoves(inputs))

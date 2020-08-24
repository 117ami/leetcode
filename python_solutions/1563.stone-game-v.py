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
# @lc app=leetcode id=1563 lang=python3
#
# [1563] Stone Game V
#
# https://leetcode.com/problems/stone-game-v/description/
#
# algorithms
# Hard (27.84%)
# Total Accepted:    3.5K
# Total Submissions: 8.8K
# Testcase Example:  '[6,2,3,4,5,5]'
#
# There are several stones arranged in a row, and each stone has an associated
# value which is an integer given in the array stoneValue.
#
# In each round of the game, Alice divides the row into two non-empty rows
# (i.e. left row and right row), then Bob calculates the value of each row
# which is the sum of the values of all the stones in this row. Bob throws away
# the row which has the maximum value, and Alice's score increases by the value
# of the remaining row. If the value of the two rows are equal, Bob lets Alice
# decide which row will be thrown away. The next round starts with the
# remaining row.
#
# The game ends when there is only one stone remaining. Alice's is initially
# zero.
#
# Return the maximum score that Alice can obtain.
#
#
# Example 1:
#
#
# Input: stoneValue = [6,2,3,4,5,5]
# Output: 18
# Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5].
# The left row has the value 11 and the right row has value 14. Bob throws away
# the right row and Alice's score is now 11.
# In the second round Alice divides the row to [6], [2,3]. This time Bob throws
# away the left row and Alice's score becomes 16 (11 + 5).
# The last round Alice has only one choice to divide the row which is [2], [3].
# Bob throws away the right row and Alice's score is now 18 (16 + 2). The game
# ends because only one stone is remaining in the row.
#
#
# Example 2:
#
#
# Input: stoneValue = [7,7,7,7,7,7,7]
# Output: 28
#
#
# Example 3:
#
#
# Input: stoneValue = [4]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= stoneValue.length <= 500
# 1 <= stoneValue[i] <= 10^6
#
#
#
class Solution:
    def stoneGameV(self, ns: List[int]) -> int:
        n = len(ns)
        presum = [ns[0]] * n
        for i in range(1, n):
            presum[i] = presum[i - 1] + ns[i]

        @lru_cache(None)
        def solve(l, r):
            if l == r: return 0
            ret = 0
            for i in range(l, r):
                x = presum[i] - presum[l] + ns[l]
                y = presum[r] - presum[i]
                if x <= y:
                    ret = max(ret, x + solve(l, i))
                if y <= x:
                    ret = max(ret, y + solve(i + 1, r))
            return ret

        return solve(0, n - 1)


sol = Solution()

stoneValue = [6, 2, 3, 4, 5, 5]
# stoneValue = [7, 7, 7, 7, 7, 7, 7]
# stoneValue = [4]
print(sol.stoneGameV(stoneValue))

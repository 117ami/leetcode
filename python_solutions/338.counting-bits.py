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
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (67.55%)
# Total Accepted:    245K
# Total Submissions: 361.7K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
#
# Example 1:
#
#
# Input: 2
# Output: [0,1,1]
#
# Example 2:
#
#
# Input: 5
# Output: [0,1,1,2,1,2]
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
#
#


class Solution:
    def countBits(self, num: int) -> List[int]:
        # return list(bin(n).count('1') for n in range(num + 1))
        """ Explaination.
            Take number 10011001 for example.
            Divide it in 2 parts:
            1. the last digit ( 1 or 0, which is " i&1 ", equivalent to " i%2 " )
            2. the other digits ( the number of 1, which is " f[i >> 1] ", equivalent to " f[i/2] " )
        """
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res


sol = Solution()
print(sol.countBits(300))

import random
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
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#
# https://leetcode.com/problems/random-pick-with-weight/description/
#
# algorithms
# Medium (43.79%)
# Total Accepted:    67.1K
# Total Submissions: 153K
# Testcase Example:  '["Solution", "pickIndex"]\n[[[1]], []]'
#
# Given an array w of positive integers, where w[i] describes the weight of
# index i, write a function pickIndex which randomly picks an index in
# proportion to its weight.
#
# Note:
#
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
#
#
# Example 1:
#
#
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
#
#
#
# Example 2:
#
#
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
#
#
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array w. pickIndex has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
#
#


class Solution:
    def __init__(self, w: List[int]):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.w, random.randint(1, self.w[-1]))


# Your Solution object will be instantiated and called as such:
w = [1, 3, 10]
obj = Solution(w)
for i in range(10):
    print(obj.pickIndex())

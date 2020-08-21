import math
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
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (36.08%)
# Total Accepted:    180.2K
# Total Submissions: 494.4K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# Given n and k, return the k^th permutation sequence.
#
# Note:
#
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
#
#
# Example 1:
#
#
# Input: n = 3, k = 3
# Output: "213"
#
#
# Example 2:
#
#
# Input: n = 4, k = 9
# Output: "2314"
#
#
#


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation


sol = Solution()
print(sol.getPermutation(3, 2))

print(math.factorial(5))
print(divmod(10, 3))
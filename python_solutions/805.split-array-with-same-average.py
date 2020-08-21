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
# @lc app=leetcode id=805 lang=python3
#
# [805] Split Array With Same Average
#
# https://leetcode.com/problems/split-array-with-same-average/description/
#
# algorithms
# Hard (26.35%)
# Total Accepted:    15.4K
# Total Submissions: 58.5K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# In a given integer array A, we must move every element of A to either list B
# or list C. (B and C initially start empty.)
#
# Return true if and only if after such a move, it is possible that the average
# value of B is equal to the average value of C, and B and C are both
# non-empty.
#
#
# Example :
# Input:
# [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of
# them have the average of 4.5.
#
#
# Note:
#
#
# The length of A will be in the range [1, 30].
# A[i] will be in the range of [0, 10000].
#
#
#
#
#


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        ''' Use Python's big number to solve the problem. 
        Given A = [1, 2, 3, 4, 5], all possible sums of all sublists are  
        {1} = 1, {2} = 2, ...
        {1, 2} = 3, {1, 3} = 4, ...
        {1, 2, 3} = 6, {1, 2, 4} = 7, ...
        We can compress the sums of lists with same length k in a single number s_k by
        doing 'bit or' operation. For A = [1,2,3,4,5], sums of lists with length 1 is
        1, 2, 3, 4, 5, which can be independently represented by 1<<1, 1<<2, 1<<3, 1<<4,
        1<<5. The sum is 62, which is stored in cc[1] = 62 

        Compressed sums of lists with length 2 is stored in cc[2] = 1016. In detail
        1016 = 1 << 3 + 1 << 4 + 1 << 5 * 2 + 1 << 6 * 2 + 1 << 7 + 1 << 8 + 1 << 9 
        ... 
        
        Finally, to check if there is a sublist with length k and sum M, we can simply do
        cc[k] & (1 << M).
        '''
        _sum, n = sum(A), len(A)
        cc = [1] + [0] * n
        for a in A:
            for k in range(n - 1, 0, -1):
                cc[k] |= cc[k - 1] << a
                print(cc)

        return any(_sum * i % n == 0 and cc[i] & (1 << (_sum * i // n))
                   for i in range(1, n))


sol = Solution()
inputs = list(range(1, 6))
# inputs = [18, 10, 3, 5]
# inputs = [5, 3, 11, 19, 2]
inputs.sort()
print(sol.splitArraySameAverage(inputs))

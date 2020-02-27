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
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#
# https://leetcode.com/problems/tallest-billboard/description/
#
# algorithms
# Hard (38.71%)
# Total Accepted:    6K
# Total Submissions: 15.4K
# Testcase Example:  '[1,2,3,6]'
#
# You are installing a billboard and want it to have the largest height.  The
# billboard will have two steel supports, one on each side.  Each steel support
# must be an equal height.
#
# You have a collection of rods which can be welded together.  For example, if
# you have rods of lengths 1, 2, and 3, you can weld them together to make a
# support of length 6.
#
# Return the largest possible height of your billboard installation.  If you
# cannot support the billboard, return 0.
#
#
#
# Example 1:
#
#
# Input: [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the
# same sum = 6.
#
#
#
# Example 2:
#
#
# Input: [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the
# same sum = 10.
#
#
#
#
# Example 3:
#
#
# Input: [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.
#
#
#
#
#
# Note:
#
#
# 0 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# The sum of rods is at most 5000.
#
#
#


class Solution:
    def tallestBillboard(self, rods):
        rods.sort(reverse=True)
        for l in range(len(rods), 1, -1):
            for comb in itertools.combinations(rods, l):
                s = sum(comb)
                if s % 2 == 0:
                    s //= 2
                    X = set([s])
                    for x in comb:
                        # print(X)
                        if x in X:
                            return s
                        else:
                            Y = [y - x for y in X if y > x]
                            X.update(Y)
        return 0


sol = Solution()
rods = [1, 4, 2, 3, 4, 5, 6]
rods = [96,112,101,100,104,93,106,99,114,81,94]
print(sol.tallestBillboard(rods))
# for c in itertools.combinations([4,3,2,1], 2):
#     print(c)

def find_two_equal_subarr_max_sum(arr) -> bool:
    # Search in arr to find two sub-arrays with max sum 
    # E.g., [1,2,3,4,5,6] -> [2,3,5], [4,6]
    arr.sort(reverse=1)
    for size in range(len(arr), 1, -1):
        for c in itertools.combinations(arr, size):
            _sum = sum(c)
            if _sum % 2 == 0:
                _sum = _sum // 2
                memo = set([_sum])
                for n in c:
                    print(n, memo)
                    if n in memo: return true 
                    else:
                        memo.update([m - n for m in memo if m > n])
    return false 

arr = [2,4,3,3,5,6]
print(find_two_equal_subarr_max_sum(arr))


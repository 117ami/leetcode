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
# @lc app=leetcode id=1521 lang=python3
#
# [1521] Find a Value of a Mysterious Function Closest to Target
#
# https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/description/
#
# algorithms
# Hard (38.78%)
# Total Accepted:    3.1K
# Total Submissions: 7.6K
# Testcase Example:  '[9,12,3,7,15]\n5'
#
#
#
# Winston was given the above mysterious function func. He has an integer array
# arr and an integer target and he wants to find the values l and r that make
# the value |func(arr, l, r) - target| minimum possible.
#
# Return the minimum possible value of |func(arr, l, r) - target|.
#
# Notice that func should be called with the values l and r where 0 <= l, r <
# arr.length.
#
#
# Example 1:
#
#
# Input: arr = [9,12,3,7,15], target = 5
# Output: 2
# Explanation: Calling func with all the pairs of [l,r] =
# [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]],
# Winston got the following results [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0]. The
# value closest to 5 is 7 and 3, thus the minimum difference is 2.
#
#
# Example 2:
#
#
# Input: arr = [1000000,1000000,1000000], target = 1
# Output: 999999
# Explanation: Winston called the func with all possible values of [l,r] and he
# always got 1000000, thus the min difference is 999999.
#
#
# Example 3:
#
#
# Input: arr = [1,2,4,8,16], target = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^6
# 0 <= target <= 10^7
#
#
#


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        # _set = {}
        # ans = float('inf')
        # for n in arr:
        #     _set = {n & m for m in _set} | {n}
        #     for c in _set:
        #         ans = min(ans, abs(c - target))
        # return ans

        # Method 2, 780 ms, beats 90 % of Python3 submissions       
        ans = float('inf')
        tmp = arr[0]
        for n in arr:
            tmp = n if tmp < target else tmp
            tmp &= n
            ans = ans if ans < abs(
                target - tmp) else min(ans, abs(target - tmp))
        return ans


sol = Solution()

arr = [9, 12, 3, 7, 15]
target = 5
print(sol.closestToTarget(arr, target))

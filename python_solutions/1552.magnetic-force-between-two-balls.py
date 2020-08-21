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
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#
# https://leetcode.com/problems/magnetic-force-between-two-balls/description/
#
# algorithms
# Medium (38.24%)
# Total Accepted:    3.3K
# Total Submissions: 8.7K
# Testcase Example:  '[1,2,3,4,7]\n3'
#
# In universe Earth C-137, Rick discovered a special form of magnetic force
# between two balls if they are put in his new invented basket. Rick has n
# empty baskets, the i^th basket is at position[i], Morty has m balls and needs
# to distribute the balls into the baskets such that the minimum magnetic force
# between any two balls is maximum.
#
# Rick stated that magnetic force between two different balls at positions x
# and y is |x - y|.
#
# Given the integer array position and the integer m. Return the required
# force.
#
#
# Example 1:
#
#
# Input: position = [1,2,3,4,7], m = 3
# Output: 3
# Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the
# magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3.
# We cannot achieve a larger minimum magnetic force than 3.
#
#
# Example 2:
#
#
# Input: position = [5,4,3,2,1,1000000000], m = 2
# Output: 999999999
# Explanation: We can use baskets 1 and 1000000000.
#
#
#
# Constraints:
#
#
# n == position.length
# 2 <= n <= 10^5
# 1 <= position[i] <= 10^9
# All integers in position are distinct.
# 2 <= m <= position.length
#
#
#
class BS:
    '''General template for binary search 
    '''
    def search(lv: int, rv: int, bool_func):
        left, right = lv, rv
        while left < right:
            mid = (left + right) // 2
            if bool_func(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1


class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        def __okay(distance):
            i32m, loc = m, p[0]
            while i32m > 0:
                i = bisect_left(p, loc)
                if i == len(p): return False
                loc = p[i] + distance
                i32m -= 1
            return True

        p.sort()
        return BS.search(1, p[-1], __okay)


sol = Solution()

position, m = [1, 2, 3, 4, 7], 3
position, m = [5, 4, 3, 2, 1, 1000000000], 2
print(sol.maxDistance(position, m))

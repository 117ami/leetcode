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
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#
# https://leetcode.com/problems/build-an-array-with-stack-operations/description/
#
# algorithms
# Easy (68.07%)
# Total Accepted:    6.6K
# Total Submissions: 9.7K
# Testcase Example:  '[1,3]\r\n3\r'
#
# Given an array target and an integer n. In each iteration, you will read a
# number from  list = {1,2,3..., n}.
#
# Build the target array using the following operations:
#
#
# Push: Read a new element from the beginning list, and push it in the
# array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
#
#
# You are guaranteed that the target array is strictly increasing, only
# containing numbers between 1 to n inclusive.
#
# Return the operations to build the target array.
#
# You are guaranteed that the answer is unique.
#
#
# Example 1:
#
#
# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation:
# Read number 1 and automatically push in the array -> [1]
# Read number 2 and automatically push in the array then Pop it -> [1]
# Read number 3 and automatically push in the array -> [1,3]
#
#
# Example 2:
#
#
# Input: target = [1,2,3], n = 3
# Output: ["Push","Push","Push"]
#
#
# Example 3:
#
#
# Input: target = [1,2], n = 4
# Output: ["Push","Push"]
# Explanation: You only need to read the first 2 numbers and stop.
#
#
# Example 4:
#
#
# Input: target = [2,3,4], n = 4
# Output: ["Push","Pop","Push","Push","Push"]
#
#
#
# Constraints:
#
#
# 1 <= target.length <= 100
# 1 <= target[i] <= 100
# 1 <= n <= 100
# target is strictly increasing.
#
#
#


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        return list(sum([("Push",) if i in set(target) else ("Push", "Pop")
                         for i in range(1, 1 + min(n, max(target)))], ()))


sol = Solution()
target = [2, 3, 4]
n = 4
print(sol.buildArray(target, n))

def flatten(nested_list):
    res = []
    for e in nested_list:
        if type(e) == list or type(e) == tuple:
            res.extend(flatten(e))
        else:
            res.append(e)
    return res 
        
nested = [[[[1,2,3,[1,2,[4,3,4,[3,43]]]]]]]
nested = [(1, 2, [2, (9, 28), [2,3,4]]), (8, 9)]
print(flatten(nested))
nested = ('P',)
print(type(nested).__name__)




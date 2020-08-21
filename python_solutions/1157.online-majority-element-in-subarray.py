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
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007
#
# @lc app=leetcode id=1157 lang=python3
#
# [1157] Online Majority Element In Subarray
#
# https://leetcode.com/problems/online-majority-element-in-subarray/description/
#
# algorithms
# Hard (38.85%)
# Total Accepted:    7.2K
# Total Submissions: 18.5K
# Testcase Example:  '["MajorityChecker","query","query","query"]\n' +
# '[[[1,1,2,2,1,1]],[0,5,4],[0,3,3],[2,3,2]]'
#
# Implementing the class MajorityChecker, which has the following API:
#
#
# MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the
# given array arr;
# int query(int left, int right, int threshold) has arguments such
# that:
#
# 0 <= left <= right < arr.length representing a subarray of arr;
# 2 * threshold > right - left + 1, ie. the threshold is always a strict
# majority of the length of the subarray
#
#
#
#
# Each query(...) returns the element in arr[left], arr[left+1], ...,
# arr[right] that occurs at least threshold times, or -1 if no such element
# exists.
#
#
#
# Example:
#
#
# MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // returns 1
# majorityChecker.query(0,3,3); // returns -1
# majorityChecker.query(2,3,2); // returns 2
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 20000
# 1 <= arr[i] <= 20000
# For each query, 0 <= left <= right < len(arr)
# For each query, 2 * threshold > right - left + 1
# The number of queries is at most 10000
#
#


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.loc = defaultdict(list)
        for i, n in enumerate(arr):
            self.loc[n].append(i)
        self.nums = sorted(self.loc.keys(), key=lambda n: len( self.loc[n]),reverse=True)
        print(self.nums)

    def query(self, left: int, right: int, threshold: int) -> int:
        for n in self.nums:
            if self.loc[n].__len__() < threshold:
                return -1
            l = bisect_left(self.loc[n], left)
            r = bisect_right(self.loc[n], right)
            if r - l >= threshold:
                return n
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
m = MajorityChecker([1, 1, 2, 2, 1, 1])
print(m.query(0, 5, 4))
print(m.query(2, 3, 3))

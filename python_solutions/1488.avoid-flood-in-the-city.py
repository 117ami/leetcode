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
# @lc app=leetcode id=1488 lang=python3
#
# [1488] Avoid Flood in The City
#
# https://leetcode.com/problems/avoid-flood-in-the-city/description/
#
# algorithms
# Medium (25.27%)
# Total Accepted:    9.6K
# Total Submissions: 38.1K
# Testcase Example:  '[1,2,3,4]'
#
# Your country has an infinite number of lakes. Initially, all the lakes are
# empty, but when it rains over the nth lake, the nth lake becomes full of
# water. If it rains over a lake which is full of water, there will be a flood.
# Your goal is to avoid the flood in any lake.
#
# Given an integer array rains where:
#
#
# rains[i] > 0 means there will be rains over the rains[i] lake.
# rains[i] == 0 means there are no rains this day and you can choose one lake
# this day and dry it.
#
#
# Return an array ans where:
#
#
# ans.length == rains.length
# ans[i] == -1 if rains[i] > 0.
# ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
#
#
# If there are multiple valid answers return any of them. If it is impossible
# to avoid flood return an empty array.
#
# Notice that if you chose to dry a full lake, it becomes empty, but if you
# chose to dry an empty lake, nothing changes. (see example 4)
#
#
# Example 1:
#
#
# Input: rains = [1,2,3,4]
# Output: [-1,-1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day full lakes are [1,2,3]
# After the fourth day full lakes are [1,2,3,4]
# There's no day to dry any lake and there is no flood in any lake.
#
#
# Example 2:
#
#
# Input: rains = [1,2,0,0,2,1]
# Output: [-1,-1,2,1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day, we dry lake 2. Full lakes are [1]
# After the fourth day, we dry lake 1. There is no full lakes.
# After the fifth day, full lakes are [2].
# After the sixth day, full lakes are [1,2].
# It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another
# acceptable scenario.
#
#
# Example 3:
#
#
# Input: rains = [1,2,0,1,2]
# Output: []
# Explanation: After the second day, full lakes are  [1,2]. We have to dry one
# lake in the third day.
# After that, it will rain over lakes [1,2]. It's easy to prove that no matter
# which lake you choose to dry in the 3rd day, the other one will flood.
#
#
# Example 4:
#
#
# Input: rains = [69,0,0,0,69]
# Output: [-1,69,1,1,-1]
# Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1]
# or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9
#
#
# Example 5:
#
#
# Input: rains = [10,20,20]
# Output: []
# Explanation: It will rain over lake 20 two consecutive days. There is no
# chance to dry any lake.
#
#
#
# Constraints:
#
#
# 1 <= rains.length <= 10^5
# 0 <= rains[i] <= 10^9
#
#
class DisjointSet():
    def __init__(self, size=10):
        self.data = list(range(size))

    def find(self, i):
        if i == self.data[i]: return i
        else:
            j = self.find(self.data[i])
            self.data[i] = j
            return j

    def merge(self, i):
        self.data[i] = i + 1


class Solution:
    def method2(self, rains: List[int]) -> List[int]:
        # Using disjoint set to sole the problem. check the C++ solution
        # to see how this method work
        n = len(rains)
        cc = {}
        ds = DisjointSet(n)
        i = 0
        while i < n:
            if rains[i] == 0:
                rains[i] = 1
            else:
                lake = rains[i]
                if lake in cc:
                    available_dry_day = ds.find(cc[lake])
                    # otherwise there is no available day to dry a lake before i
                    if available_dry_day < i:
                        rains[available_dry_day] = lake
                        ds.merge(available_dry_day)
                    else:
                        return []
                cc[lake] = i
                ds.merge(i)
                # Modify rain in place and return it on exiting the program to avoid
                # allocating extra space.
                rains[i] = -1
            i+=1
        return rains

    def avoidFlood(self, rains: List[int]) -> List[int]:
        return self.method2(rains)

        n = len(rains)
        cc = defaultdict(int)
        dry = list()
        res = []
        for i, r in enumerate(rains):
            if r == 0:
                dry.append(i)
                res.append(1)
            else:
                if r not in cc:
                    cc[r] = i
                else:
                    print(i, r, dry)
                    last_idx = cc[r]
                    j = bisect_left(dry, last_idx)
                    if j == len(dry): return []
                    day = dry[j]
                    del dry[j]
                    res[day] = r
                    cc[r] = i
                res.append(-1)
        print(res, dry)
        return res


sol = Solution()

rains = [1, 2, 3, 4]
# rains = [1,2,0,0,2,1]
# rains = [1,2,0,1,2]
rains = [69, 0, 0, 0, 69]
# rains = [10,20,20]
rains = [1, 0, 2, 3, 0, 1, 2]
rains = [1, 2, 0, 0, 2, 1]
print(sol.avoidFlood(rains))

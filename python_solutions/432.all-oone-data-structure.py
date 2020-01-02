from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
# https://leetcode.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (31.04%)
# Total Accepted:    24.8K
# Total Submissions: 80K
# Testcase Example:  '["AllOne","getMaxKey","getMinKey"]\n[[],[],[]]'
#
# Implement a data structure supporting the following operations:
#
#
#
# Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by
# 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise
# decrements an existing key by 1. If the key does not exist, this function
# does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element
# exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element
# exists, return an empty string "".
#
#
#
#
# Challenge: Perform all these in O(1) time complexity.
#
#


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = defaultdict(int)
        # self.ss = defaultdict(set())

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        # if key in self.ds[key]:
        #     self.ds[key].erase(key)

        self.ds[key] += 1
        # self.ss[self.ds[key]].add(key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        self.ds[key] -= 1
        if self.ds[key] < 1:
            del self.ds[key]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        res = ""
        mx = 0
        for k, v in self.ds.items():
            if v > mx:
                res, mx = k, v
        return res

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        res = ""
        mx = 0x3f3f3f3f
        for k, v in self.ds.items():
            if v < mx:
                res, mx = k, v
        return res


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# sol = Solution()

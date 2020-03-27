from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right, insort
from functools import reduce, lru_cache
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (58.67%)
# Total Accepted:    41.6K
# Total Submissions: 70.8K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
# '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
#
# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in
# the HashSet, do nothing.
#
#
#
# Example:
#
#
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);
# hashSet.add(2);
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)
#
#
#
# Note:
#
#
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
#
#
#


class MyHashSet:

		def __init__(self):
				"""
				Initialize your data structure here.
				"""
				self.ds = bytearray(1000001)

		def add(self, key: int) -> None:
			# i = bisect_left(self.ds, key)
			# if len(self.ds) <= i or self.ds[i] != key:
			#   insort(self.ds, key)
			self.ds[key] = true

		def remove(self, key: int) -> None:
			# i = bisect_left(self.ds, key)
			# if len(self.ds) > i and self.ds[i] == key:
			#   self.ds = self.ds[:i] + self.ds[i+1:]
			self.ds[key] = false
				

		def contains(self, key: int) -> bool:
				"""
				Returns true if this set contains the specified element
				"""
				# i = bisect_left(self.ds, key)
				# return len(self.ds) > i and self.ds[i] == key 
				return self.ds[key] == 1


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(9)
obj.remove(19)

print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))

# obj.remove(key)
# param_3 = obj.contains(key)
arr = []
idx = bisect_left(arr, 4)
insort(arr, 4)


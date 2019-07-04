#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
#
# algorithms
# Hard (30.93%)
# Total Accepted:    35K
# Total Submissions: 113K
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n[[],[1],[1],[2],[],[1],[]]'
#
# Design a data structure that supports all following operations in average
# O(1) time.
# Note: Duplicate elements are allowed.
# 
# 
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The
# probability of each element being returned is linearly related to the number
# of same value the collection contains.
# 
# 
# 
# Example:
# 
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
# 
# // Inserts 1 to the collection. Returns true as the collection did not
# contain 1.
# collection.insert(1);
# 
# // Inserts another 1 to the collection. Returns false as the collection
# contained 1. Collection now contains [1,1].
# collection.insert(1);
# 
# // Inserts 2 to the collection, returns true. Collection now contains
# [1,1,2].
# collection.insert(2);
# 
# // getRandom should return 1 with the probability 2/3, and returns 2 with the
# probability 1/3.
# collection.getRandom();
# 
# // Removes 1 from the collection, returns true. Collection now contains
# [1,2].
# collection.remove(1);
# 
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();
# 
# 
#

import random 
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = defaultdict(lambda: list())
        self.arr = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        res = True
        if val in self.pos: res = False
        self.pos[val].append(len(self.arr))
        self.arr.append([val, len(self.pos[val]) - 1])
        return res
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos or not self.pos: return False 

        lastval, idx = self.arr[-1]
        self.pos[lastval][idx] = self.pos[val][-1]
        self.arr[self.pos[val][-1]] = [lastval, idx]
        self.pos[val].pop()
        if not self.pos[val]:
            self.pos.pop(val, []) 
        self.arr.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.arr[random.randint(0, len(self.arr)-1)][0]


        


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
for n in [9, 9, 1, 1, 2, 1]:
    obj.insert(n)

print(obj.remove(2))
print(obj.remove(1))
print(obj.remove(1))
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

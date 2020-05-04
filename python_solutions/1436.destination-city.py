from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#
# https://leetcode.com/problems/destination-city/description/
#
# algorithms
# Easy (80.55%)
# Total Accepted:    9.4K
# Total Submissions: 11.6K
# Testcase Example:  '[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]'
#
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there
# exists a direct path going from cityAi to cityBi. Return the destination
# city, that is, the city without any path outgoing to another city.
# 
# It is guaranteed that the graph of paths forms a line without any loop,
# therefore, there will be exactly one destination city.
# 
# 
# Example 1:
# 
# 
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao
# Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which
# is the destination city. Your trip consist of: "London" -> "New York" ->
# "Lima" -> "Sao Paulo".
# 
# 
# Example 2:
# 
# 
# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".
# 
# 
# Example 3:
# 
# 
# Input: paths = [["A","Z"]]
# Output: "Z"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= paths.length <= 100
# paths[i].length == 2
# 1 <= cityAi.length, cityBi.length <= 10
# cityAi != cityBi
# All strings consist of lowercase and uppercase English letters and the space
# character.
# 
# 
#
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sa, sb = set(), set()
        for p in paths:
            sa.add(p[0])
            sb.add(p[1])
        return (sb - sa).pop()

sol = Solution()
paths = [["B","C"],["D","B"],["C","A"]]
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(sol.destCity(paths))


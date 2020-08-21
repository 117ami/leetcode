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
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (50.64%)
# Total Accepted:    121.3K
# Total Submissions: 239.3K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
# '[2.0,3.0]\n' +
# '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
#
# According to the example above:
#
#
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ].
#
#
#
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
#
#


class UF():
    def __init__(self):
        self.root = defaultdict()

    def union(self, x, y, ratio):
        new = self.find(y)
        old = self.find(x)
        if old[0] == x:
            self.root[x] = (new[0], ratio * new[1])
        else:
            self.root[y] = (old[0], old[1] / ratio)

    def find(self, x):
        if x not in self.root or x == self.root[x][0]:
            self.root[x] = (x, 1)
            return self.root[x]

        p = self.find(self.root[x][0])
        q = self.root[x]
        # if x == 'b' : print(p, q)
        if q[0] == p[0]:
            return q
        self.root[x] = (p[0], q[1] * p[1])
        return self.root[x]


class Solution:
    def calcEquation(self,
                     equations: List[List[str]],
                     values: List[float],
                     queries: List[List[str]]) -> List[float]:
        uf = UF()
        for i, e in enumerate(equations):
            uf.union(e[0], e[1], values[i])
        ks = uf.root.keys()
        for k in ks:
            uf.find(k)

        res = []
        keys = set(uf.root.keys())
        for q in queries:
            a, b = q
            pa, pb = uf.find(a), uf.find(b)
            if pa[0] not in keys or pb[0] not in keys or pa[0] != pb[0]:
                res.append(-1)
            else:
                res.append(pa[1] / pb[1])
        print(uf.root)
        return res


sol = Solution()
e = [["a", "b"], ["b", "c"]]
v = [2.0, 3.0]
q = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(sol.calcEquation(e, v, q))
uf = UF()
# print(uf.find('a'))

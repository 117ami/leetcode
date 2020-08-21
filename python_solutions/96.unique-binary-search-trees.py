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
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (51.06%)
# Total Accepted:    278.6K
# Total Submissions: 544K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
cc = {1: 1, 2: 2, 0: 1}


class Solution:
    def numTrees(self, n: int) -> int:
        if n in cc:
            return cc[n]
        cc[n] = sum(map(lambda i: self.numTrees(i) *
                        self.numTrees(n - i - 1), range(n)))
        return cc[n]


sol = Solution()
n = 4
print(sol.numTrees(n))

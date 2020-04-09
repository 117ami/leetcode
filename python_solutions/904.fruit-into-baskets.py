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
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (42.17%)
# Total Accepted:    83.8K
# Total Submissions: 198.9K
# Testcase Example:  '[1,2,1]'
#
# In a row of trees, the i-th tree produces fruit with type tree[i].
#
# You start at any tree of your choice, then repeatedly perform the following
# steps:
#
#
# Add one piece of fruit from this tree to your baskets.  If you cannot,
# stop.
# Move to the next tree to the right of the current tree.  If there is no tree
# to the right, stop.
#
#
# Note that you do not have any choice after the initial choice of starting
# tree: you must perform step 1, then step 2, then back to step 1, then step 2,
# and so on until you stop.
#
# You have two baskets, and each basket can carry any quantity of fruit, but
# you want each basket to only carry one type of fruit each.
#
# What is the total amount of fruit you can collect with this procedure?
#
#
#
# Example 1:
#
#
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
#
#
#
# Example 2:
#
#
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
#
#
#
# Example 3:
#
#
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
#
#
#
# Example 4:
#
#
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4
# fruits.
#
#
#
#
#
#
#
# Note:
#
#
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length
#
#
#


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        cnt = 0
        arr = [0] * (1 + max(tree))
        i = res = 0
        for j, t in enumerate(tree):
            if arr[t] == 0:
                cnt += 1
            arr[t] += 1
            while cnt > 2:
                arr[tree[i]] -= 1
                if arr[tree[i]] == 0:
                    cnt -= 1
                i += 1
            res = max(res, j - i + 1)

        return res


tree = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
tree = [1, 2, 3, 2, 2]
# tree = [0, 1, 2, 2]
sol = Solution()
print(sol.totalFruit(tree))

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
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Deletion Cost to Avoid Repeating Letters
#
# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/description/
#
# algorithms
# Medium (56.92%)
# Total Accepted:    5.5K
# Total Submissions: 9.7K
# Testcase Example:  '"abaac"\n[1,2,3,4,5]'
#
# Given a string s and an array of integers cost where cost[i] is the cost of
# deleting the character i in s.
#
# Return the minimum cost of deletions such that there are no two identical
# letters next to each other.
#
# Notice that you will delete the chosen characters at the same time, in other
# words, after deleting a character, the costs of deleting other characters
# will not change.
#
#
# Example 1:
#
#
# Input: s = "abaac", cost = [1,2,3,4,5]
# Output: 3
# Explanation: Delete the letter "a" with cost 3 to get "abac" (String without
# two identical letters next to each other).
#
#
# Example 2:
#
#
# Input: s = "abc", cost = [1,2,3]
# Output: 0
# Explanation: You don't need to delete any character because there are no
# identical letters next to each other.
#
#
# Example 3:
#
#
# Input: s = "aabaa", cost = [1,2,3,4,1]
# Output: 2
# Explanation: Delete the first and the last character, getting the string
# ("aba").
#
#
#
# Constraints:
#
#
# s.length == cost.length
# 1 <= s.length, cost.length <= 10^5
# 1 <= cost[i] <= 10^4
# s contains only lowercase English letters.
#
#
#
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i, res, n = 0, 0, len(cost)
        while i < n - 1:
            if s[i] == s[i + 1]:
                j, total, n_max = i, 0, 0
                while j < n and s[i] == s[j]:
                    total += cost[j]
                    n_max = max(n_max, cost[j])
                    j += 1
                res += total - n_max
                i = j
            else:
                i += 1
        return res


sol = Solution()

s, cost = "abaac", [1, 2, 3, 4, 5]
s, cost = "abc", [1, 2, 3]
s, cost = "aabaa", [1, 2, 3, 4, 1]
print(sol.minCost(s, cost))

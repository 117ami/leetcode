from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#
# https://leetcode.com/problems/count-largest-group/description/
#
# algorithms
# Easy (59.01%)
# Total Accepted:    4.3K
# Total Submissions: 7.2K
# Testcase Example:  '13\r'
#
# Given an integer n. Each number from 1 to n is grouped according to the sum
# of its digits. 
# 
# Return how many groups have the largest size.
# 
# 
# Example 1:
# 
# 
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of
# its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups
# with largest size.
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
# 
# 
# Example 3:
# 
# 
# Input: n = 15
# Output: 6
# 
# 
# Example 4:
# 
# 
# Input: n = 24
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 
# 
#
class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = Counter(sum(int (e) for e in list(str(i))) for i in range(1, n + 1)).values()
        return list(cnt).count(max(cnt))

sol = Solution()
print(sol.countLargestGroup(24))




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
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#
# https://leetcode.com/problems/ipo/description/
#
# algorithms
# Hard (40.40%)
# Total Accepted:    18K
# Total Submissions: 44.5K
# Testcase Example:  '2\n0\n[1,2,3]\n[0,1,1]'
#
#
# Suppose LeetCode will start its IPO soon. In order to sell a good price of
# its shares to Venture Capital, LeetCode would like to work on some projects
# to increase its capital before the IPO. Since it has limited resources, it
# can only finish at most k distinct projects before the IPO. Help LeetCode
# design the best way to maximize its total capital after finishing at most k
# distinct projects.
#
#
#
# You are given several projects. For each project i, it has a pure profit Pi
# and a minimum capital of Ci is needed to start the corresponding project.
# Initially, you have W capital. When you finish a project, you will obtain its
# pure profit and the profit will be added to your total capital.
#
#
#
# To sum up, pick a list of at most k distinct projects from given projects to
# maximize your final capital, and output your final maximized capital.
#
#
# Example 1:
#
# Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].
#
# Output: 4
#
# Explanation: Since your initial capital is 0, you can only start the project
# indexed 0.
# ⁠            After finishing it you will obtain profit 1 and your capital
# becomes 1.
# ⁠            With capital 1, you can either start the project indexed 1 or
# the project indexed 2.
# ⁠            Since you can choose at most 2 projects, you need to finish the
# project indexed 2 to get the maximum capital.
# ⁠            Therefore, output the final maximized capital, which is 0 + 1 +
# 3 = 4.
#
#
#
# Note:
#
# You may assume all numbers in the input are non-negative integers.
# The length of Profits array and Capital array will not exceed 50,000.
# The answer is guaranteed to fit in a 32-bit signed integer.
#
#
#
class Solution:
    def findMaximizedCapital(self, k: int, w: int, p: List[int],
                             c: List[int]) -> int:
        ps = [-n for i, n in enumerate(p) if n >= 0 and c[i] <= w]
        cands = [i for i, n in enumerate(p) if n >= 0 and c[i] > w]
        cands.sort(key=lambda i: (-c[i], p[i]))

        heapq.heapify(ps)
        while k > 0 and ps:
            w -= heapq.heappop(ps)

            while cands and c[cands[-1]] <= w:
                heapq.heappush(ps, -p[cands[-1]])
                cands.pop()
            k -= 1
        return w


sol = Solution()

k, w, p, c = 2, 0, [1, 2, 3], [0, 1, 1]
k, w, p, c = 1, 2, [1, 2, 3], [1, 1, 2]
print(sol.findMaximizedCapital(k, w, p, c))

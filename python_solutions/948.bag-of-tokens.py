from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#
# https://leetcode.com/problems/bag-of-tokens/description/
#
# algorithms
# Medium (39.96%)
# Total Accepted:    8.8K
# Total Submissions: 21.9K
# Testcase Example:  '[100]\n50'
#
# You have an initial power P, an initial score of 0 points, and a bag of
# tokens.
#
# Each token can be used at most once, has a value token[i], and has
# potentially two ways to use it.
#
#
# If we have at least token[i] power, we may play the token face up, losing
# token[i] power, and gaining 1 point.
# If we have at least 1 point, we may play the token face down, gaining
# token[i] power, and losing 1 point.
#
#
# Return the largest number of points we can have after playing any number of
# tokens.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: tokens = [100], P = 50
# Output: 0
#
#
#
# Example 2:
#
#
# Input: tokens = [100,200], P = 150
# Output: 1
#
#
#
# Example 3:
#
#
# Input: tokens = [100,200,300,400], P = 200
# Output: 2
#
#
#
#
# Note:
#
#
# tokens.length <= 1000
# 0 <= tokens[i] < 10000
# 0 <= P < 10000
#
#
#
#
#
#


class Solution:
    def bagOfTokensScore(self, tokens, p):
        tokens.sort()
        i, j = 0, len(tokens) - 1
        maxpoints = curpoints = 0
        while i <= j:
            if p >= tokens[i]:
                p -= tokens[i]
                curpoints += 1
                maxpoints = max(maxpoints, curpoints)
                i += 1
            elif curpoints > 0:
                curpoints -= 1
                p += tokens[j]
                j -= 1
            else: break 
        return maxpoints


sol = Solution()
tokens, p = [100, 200, 300, 400], 200
# tokens, p = [100,200], 150
# tokens, p = [25, 91], 99
tokens, p = [71,55,82], 54
print(sol.bagOfTokensScore(tokens, p))

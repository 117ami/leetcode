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
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
#
# algorithms
# Medium (29.82%)
# Total Accepted:    4.6K
# Total Submissions: 14.5K
# Testcase Example:  '[1,2,3,4,5,6,1]\n3'
#
# There are several cards arranged in a row, and each card has an associated
# number of points The points are given in the integer array cardPoints.
#
# In one step, you can take one card from the beginning or from the end of the
# row. You have to take exactly k cards.
#
# Your score is the sum of the points of the cards you have taken.
#
# Given the integer array cardPoints and the integer k, return the maximum
# score you can obtain.
#
#
# Example 1:
#
#
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However,
# choosing the rightmost card first will maximize your total score. The optimal
# strategy is to take the three cards on the right, giving a final score of 1 +
# 6 + 5 = 12.
#
#
# Example 2:
#
#
# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Explanation: Regardless of which two cards you take, your score will always
# be 4.
#
#
# Example 3:
#
#
# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55
# Explanation: You have to take all the cards. Your score is the sum of points
# of all cards.
#
#
# Example 4:
#
#
# Input: cardPoints = [1,1000,1], k = 1
# Output: 1
# Explanation: You cannot take the card in the middle. Your best score is 1.
#
#
# Example 5:
#
#
# Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
# Output: 202
#
#
#
# Constraints:
#
#
# 1 <= cardPoints.length <= 10^5
# 1 <= cardPoints[i] <= 10^4
# 1 <= k <= cardPoints.length
#
#
#


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        j = len(cardPoints) - 1
        cur = ans = sum(cardPoints[:k])
        while k > 0:
            cur += cardPoints[j] - cardPoints[k-1]
            k -= 1
            j -= 1
            ans = max(ans, cur)
        return ans


sol = Solution()
cardPoints = [1, 79, 80, 1, 1, 1, 200, 1]
k = 3
print(sol.maxScore(cardPoints, k))

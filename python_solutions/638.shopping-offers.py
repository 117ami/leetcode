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
# @lc app=leetcode id=638 lang=python3
#
# [638] Shopping Offers
#
# https://leetcode.com/problems/shopping-offers/description/
#
# algorithms
# Medium (51.65%)
# Total Accepted:    31.5K
# Total Submissions: 60.9K
# Testcase Example:  '[2,5]\n[[3,0,5],[1,2,10]]\n[3,2]'
#
#
# In LeetCode Store, there are some kinds of items to sell. Each item has a
# price.
#
#
#
# However, there are some special offers, and a special offer consists of one
# or more different kinds of items with a sale price.
#
#
#
# You are given the each item's price, a set of special offers, and the number
# we need to buy for each item.
# The job is to output the lowest price you have to pay for exactly certain
# items as given, where you could make optimal use of the special offers.
#
#
#
# Each special offer is represented in the form of an array, the last number
# represents the price you need to pay for this special offer, other numbers
# represents how many specific items you could get if you buy this offer.
#
#
# You could use any of special offers as many times as you want.
#
# Example 1:
#
# Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
# Output: 14
# Explanation:
# There are two kinds of items, A and B. Their prices are $2 and $5
# respectively.
# In special offer 1, you can pay $5 for 3A and 0B
# In special offer 2, you can pay $10 for 1A and 2B.
# You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer
# #2), and $4 for 2A.
#
#
#
# Example 2:
#
# Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
# Output: 11
# Explanation:
# The price of A is $2, and $3 for B, $4 for C.
# You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
# You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer
# #1), and $3 for 1B, $4 for 1C.
# You cannot add more items, though only $9 for 2A ,2B and 1C.
#
#
#
# Note:
#
# There are at most 6 kinds of items, 100 special offers.
# For each item, you need to buy at most 6 of them.
# You are not allowed to buy more items than you want, even if that would lower
# the overall price.
#
#
#
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]],
                       needs: List[int]) -> int:
        memo = {0: 0}

        def dp(cur_needs):
            key = 0
            for n in cur_needs:
                if n < 0: return 0x3f3f3f3f
                key = key * 6 + n

            if key in memo:
                return memo[key]
            ans = sum((a * b for a, b in zip(price, cur_needs)))

            for s in special:
                tmp = [cur_needs[i] - s[i] for i in range(len(cur_needs))]
                ans = min(ans, s[-1] + dp(tmp))

            memo[key] = ans
            return ans

        return dp(needs)


sol = Solution()
price, special, needs = [2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]
price, special, needs = [2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]
print(sol.shoppingOffers(price, special, needs))

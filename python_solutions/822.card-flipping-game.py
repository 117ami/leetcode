from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
true = True
false = False
#
# @lc app=leetcode id=822 lang=python3
#
# [822] Card Flipping Game
#
# https://leetcode.com/problems/card-flipping-game/description/
#
# algorithms
# Medium (41.81%)
# Total Accepted:    7.6K
# Total Submissions: 18.1K
# Testcase Example:  '[1,2,4,4,7]\n[1,3,4,1,3]'
#
# On a table are N cards, with a positive integer printed on the front and back
# of each card (possibly different).
#
# We flip any number of cards, and after we choose one card. 
#
# If the number X on the back of the chosen card is not on the front of any
# card, then this number X is good.
#
# What is the smallest number that is good?  If no number is good, output 0.
#
# Here, fronts[i] and backs[i] represent the number on the front and back of
# card i. 
#
# A flip swaps the front and back numbers, so the value on the front is now on
# the back and vice versa.
#
# Example:
#
#
# Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
# Output: 2
# Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the
# backs are [1,2,4,1,3].
# We choose the second card, which has number 2 on the back, and it isn't on
# the front of any card, so 2 is good.
#
#
#
# Note:
#
#
# 1 <= fronts.length == backs.length <= 1000.
# 1 <= fronts[i] <= 2000.
# 1 <= backs[i] <= 2000.
#
#
#


class Solution:
    def flipgame(self, fs, bs):
        common = {f for f, b in zip(fs, bs)if f == b}
        return min((n for n in fs + bs if n not in common), default=0)


s = Solution()
fs, bs = [1, 2, 4, 4, 7], [1, 3, 4, 1, 3]
# fs,bs=[1],[1]
print(s.flipgame(fs, bs))

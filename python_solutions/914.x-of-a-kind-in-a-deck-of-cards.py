#
# @lc app=leetcode id=914 lang=python
#
# [914] X of a Kind in a Deck of Cards
#
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (33.98%)
# Total Accepted:    10.7K
# Total Submissions: 31.6K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# In a deck of cards, each card has an integer written on it.
#
# Return true if and only if you can choose X >= 2 such that it is possible to
# split the entire deck into 1 or more groups of cards, where:
#
#
# Each group has exactly X cards.
# All the cards in each group have the same integer.
#
#
#
#
# Example 1:
#
#
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
#
#
#
# Example 2:
#
#
# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
#
#
#
# Example 3:
#
#
# Input: [1]
# Output: false
# Explanation: No possible partition.
#
#
#
# Example 4:
#
#
# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
#
#
#
# Example 5:
#
#
# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
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
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
#
#
#
#
#
#
#
#
#
#
#
#
#
from collections import Counter

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        vs = Counter(deck).values()
        k = min(vs)
        for n in vs:
            k = self.gcd(k, n)
            if k == 1:
                return False

        return True

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)


deck = [2, 1, 1, 2, 2, 2, 1]
deck = [1, 1, 1, 2, 2, 2, 3, 3]
print(Solution().hasGroupsSizeX(deck))

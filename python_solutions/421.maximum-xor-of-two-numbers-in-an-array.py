from collections import Counter, defaultdict
true = True
false = False
#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (52.38%)
# Total Accepted:    43.8K
# Total Submissions: 83.5K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 2^31.
#
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
#
# Could you do this in O(n) runtime?
#
# Example:
#
#
# Input: [3, 10, 5, 25, 2, 8]
#
# Output: 28
#
# Explanation: The maximum result is 5 ^ 25 = 28.
#
#
#
#
#


class Solution:
    def findMaximumXOR(self, ns):
        xmax = msk = 0

        for i in range(31, -1, -1):
            msk |= (1 << i)
            cans = set([n & msk for n in ns])

            nmax = xmax | (1 << i)
            for n in cans:
                if n ^ nmax in cans:
                    xmax = nmax
                    break
        return xmax


s = Solution()
n = 15
ns = [3, 10, 5, 25, 2, 8]
# ns = [4, 6, 7]
print(s.findMaximumXOR(ns))

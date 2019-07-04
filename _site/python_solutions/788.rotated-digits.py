#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#
# https://leetcode.com/problems/rotated-digits/description/
#
# algorithms
# Easy (52.17%)
# Total Accepted:    20.8K
# Total Submissions: 39.6K
# Testcase Example:  '10'
#
# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.  Each digit must be rotated -
# we cannot choose to leave it alone.
# 
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8
# rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each
# other, and the rest of the numbers do not rotate to any other number and
# become invalid.
# 
# Now given a positive number N, how many numbers X from 1 to N are good?
# 
# 
# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
# 
# 
# Note:
# 
# 
# N  will be in range [1, 10000].
# 
# 
#
class Solution:
    def __init__(self):
        self.da = set([0, 1, 8])
        self.db = set([2, 5, 6, 9])
        self.memo = {0:'almost'}

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        return sum([1 if self.is_good(k) == 'good' else 0 for k in range(1, N+1)])


    def is_good(self, k):
        m, n = divmod(k, 10)
        if n not in self.da and n not in self.db or self.memo[m] == 'bad': 
            self.memo[k] = 'bad'
        elif n in self.da and self.memo[m] == 'almost':
            self.memo[k] = 'almost'
        else:
            self.memo[k] = 'good'

        return self.memo[k]



print(Solution().rotatedDigits(10))
